from utils.strings_util import (
    convert_to_python_type,
    camel_case_to_snake_case,
    get_type_from_reference
)


response_models = {
    'base_bool_response': "base.Bool",
    'base_getUploadServer_response': "base.GetUploadServer",
    'base_ok_response': "base.Ok"
}

CLASSMETHOD_PATTERN = \
"""    async def {snake_name}(
        {args}
    ) -> {type}ResponseModel:
        {desc}
        params = self.get_set_params(locals())
        response = await self.api.request(\"{name}\", params)
        model = {type}Response
        return model(**response).response"""


class ObjectModel:
    def __init__(self, method_name: str = None, method: dict = None, **params):
        self.method = method
        self.method_name = method_name
        self.params = params


class Description(ObjectModel):
    def __str__(self):
        title = self.method.get(
            "description"
        ) or self.method_name + " method"

        description = '\n'.join(
            "\t\t:param %s: %s" % (param['name'], param.get("description", ''))
            for param in self.params['sorted_params']
        )
        if description:
            description = '\n' + description + '\n\t\t'
        return "\"\"\"%s%s\"\"\"\n" % (title, description)


class Annotation(ObjectModel):
    def __str__(self):
        items = self.params["items"]
        param_type = self.params["type"]
        param_annotate = convert_to_python_type(self.params['annotate'])

        if param_annotate == 'list' and items.get("$ref", items.get("type")):
            post_annotate = (
                get_type_from_reference(items["$ref"])
                if items.get("$ref") else
                items["type"]
            )
            param_annotate = "List[%s]" % convert_to_python_type(post_annotate)

        if param_type is False:
            return f"Optional[{param_annotate}] = None"
        return param_annotate


class ConvertToArgs(ObjectModel):
    def __str__(self):
        params = ['self']
        for param in self.params['sorted_params']:
            params.append(
                f"{param['name']}: " +
                str(Annotation(
                    annotate=param['type'],
                    type=param.get('required', False),
                    items=param.get("items", {})))
            )
        params.append('**kwargs')
        formatted = ', '.join(params)

        if len(formatted) >= 80:
            formatted = formatted.replace(', ', ',\n\t\t')

        return formatted


class MethodForm:
    def parse_return_type(m_name, type_response):
        category, name = m_name.split('.')
        method_name = f"{category}.{name[0].upper() + name[1:]}"
        return_type = type_response.split('/')[-1]
        return response_models.get(return_type, method_name)

    def costruct(**params):
        return CLASSMETHOD_PATTERN.format(**params)


class ClassForm:
    def __init__(self, classname, predproc = 'BaseCategory'):
        self.name = classname
        self.predproc = predproc
        self.constructed_methods = []

    def add_method(self, method_name, method):
        sorted_params = sorted(
            method.get('parameters', {}),
            key=lambda x: not x.get('required', False)
        )
        desc = Description(method_name, method, sorted_params=sorted_params)
        args = ConvertToArgs(sorted_params=sorted_params)
        return_type = MethodForm.parse_return_type(method_name, method['responses']['response']['$ref'])
        self.constructed_methods.append(
            MethodForm.costruct(
                name=method_name,
                snake_name=camel_case_to_snake_case(method_name.split('.')[1]),
                args=args,
                desc=desc,
                type=return_type
            )
        )

    def __str__(self):
        return (f"\n\n\nclass {self.name.capitalize()}Category({self.predproc}):\n" +
                "\n\n".join(self.constructed_methods)
            )
