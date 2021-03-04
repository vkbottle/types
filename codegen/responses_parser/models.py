from utils.strings_util import get_type_from_reference
from objects_parser.models.models import Annotation


class ResponseModelBody:
    def __init__(self, annotations=None, **attributes) -> None:
        if annotations:
            temp = []
            for anno in annotations:
                if isinstance(anno, list):
                    anno = anno[0]
                    temp.append(Annotation('Array', list_inner_type=anno))
                else:
                    temp.append(Annotation(anno))

            annotations = temp
        else:
            annotations = ['' for _ in attributes]

        self.annotated_names = [
            name + str(annotation)
            for name, annotation in zip(attributes.keys(), annotations)
        ]
        self.attributes = {name: attributes[orig_name]
                           for name, orig_name in zip(
                                                     self.annotated_names,
                                                     attributes.keys()
                          )}

    def __repr__(self):
        return '\n\t'.join([f'{name} = {value}'
                           for name, value in self.attributes.items()])


class ResponseModel:
    def __init__(self,
                 classname: str,
                 annotations=None,
                 superclass="BaseResponse",
                 **variables):
        self.variables = variables
        self.classname = classname
        self.superclass = superclass
        self.annotations = annotations

    def __repr__(self):
        header = f'\n\n\nclass {self.classname}({self.superclass}):\n\t'
        body = str(ResponseModelBody(self.annotations, **self.variables))
        return header + body


class SingleTypeModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'\n\n\n{self.name} = {self.value}'


def jsonschema_object_factory(classname: str, json_properties: dict) -> 'Model':
    schema_type = json_properties['response'].get('type', '$ref')

    if schema_type == '$ref':
        t = get_type_from_reference(json_properties['response']['$ref'])
        t = Annotation.type_string_to_default_type(t)
        return SingleTypeModel(classname, f'Optional[{t}]')
    elif schema_type == 'integer':
        return SingleTypeModel(classname, 'int')
    elif schema_type == 'boolean':
        return SingleTypeModel(classname, 'bool')
    elif schema_type == 'array':
        type_ = None
        if json_properties['response']['items'].get('type'):
            type_ = json_properties['response']['items']['type']

            type_ = Annotation('Array', list_inner_type=type_)
        else:
            type_ = json_properties['response']['items']['$ref']
            type_ = get_type_from_reference(type_)

        return SingleTypeModel(classname, f'List[{type_}]')
    elif schema_type == 'string':
        return SingleTypeModel(classname, 'string')
    else:
        # HARDCODED THIS IS UNIQUE CASE
        if json_properties['response'].get('patternProperties'):
            return SingleTypeModel(classname, 'typing.Dict[str, int]')

        properties = json_properties['response']['properties']
        names = {name: None for name in properties.keys()}
        json_properties = {name: None for name in names}
        types = []
        for _, value in properties.items():
            if value.get('type'):
                property_type = value.get('type')
                if property_type == 'array':
                    ref_type = value['items'].get('$ref')
                    if ref_type:
                        types.append([get_type_from_reference(ref_type)])
                    else:
                        types.append([value['items']['type']])
                else:
                    types.append(value['type'])
            else:
                t = get_type_from_reference(value['$ref'])
                types.append(t)
        return ResponseModel(classname, types, **json_properties)
