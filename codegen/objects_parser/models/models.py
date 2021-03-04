import keyword
import string
import abc
from utils.strings_util import snake_case_to_camel_case
STANDART_TYPES = ('str', 'int', 'float')


class ObjectModel(abc.ABC):
    def __init__(self, classname: str, predecessor: str = 'BaseModel') -> None:
        self.params: dict = {}
        self.classname: str = classname
        self.predecessor: str = predecessor

    def add_param(self, param_name: str, param_value: str) -> None:
        self.params.update({param_name: param_value})

    def set_super_class(self, predecessor: str):
        self.predecessor = predecessor

    @abc.abstractmethod
    def __str__(self):
        pass


class Annotation(ObjectModel):
    def __init__(self,
                 classname: str,
                 predecessor: str = 'BaseModel',
                 list_inner_type: str = "default_name") -> None:
        super().__init__(classname, predecessor=predecessor)
        self.list_inner_type = list_inner_type

    @staticmethod
    def type_string_to_default_type(classname: str) -> str:
        classname_copy = classname.replace('"', '')
        classname_copy = classname_copy.lower()
        if classname_copy == 'integer':
            return 'int'
        elif classname_copy == 'string':
            return 'str'
        elif classname_copy == 'boolean':
            return 'bool'
        elif classname_copy == 'array':
            return 'list'
        else:
            return classname

    def __unpack_dict_values(self, dictionary):
        return ', '.join(
            self.type_string_to_default_type(v.strip("'"))
            for _, v in dictionary.items()
        )

    def __str__(self):
        camel_case_types = snake_case_to_camel_case(self.classname)
        if isinstance(camel_case_types, dict):
            camel_case_types = self.__unpack_dict_values(camel_case_types)
            self.classname = f'Union[{camel_case_types}]'
        elif camel_case_types == 'Array':
            self.list_inner_type = self.type_string_to_default_type(self.list_inner_type)
            if self.list_inner_type in STANDART_TYPES:
                self.classname = f'List[{self.list_inner_type}]'
            else:
                self.classname = f'List["{self.list_inner_type}"]'
        else:
            self.classname = '"' + camel_case_types + '"'

        self.classname = self.type_string_to_default_type(self.classname)

        label: str = f': Optional[{self.classname}]'
        return label


class Description(ObjectModel):
    def __str__(self):
        label: str = f'\t\"\"\"VK Object {self.classname}\n\n'
        if all(isinstance(desc, type(None)) for _, desc in self.params.items()):
            label += '\t\"\"\"\n'
            return label
        for name, description in self.params.items():
            if description is None:
                description = ""
            label += f'\t{name} - {description}\n'
        label += '\t\"\"\"\n'
        return label


class ClassForm(ObjectModel):
    def __init__(self, classname: str,
                 desc: Description = None,
                 predecessor: str = 'BaseModel'
                 ) -> None:
        super().__init__(classname, predecessor=predecessor)
        self.description = desc if desc else Description(self.classname)

    def add_description_row(self, name, text):
        self.description.add_param(name, text)

    def add_param(self,
                  param_name: str,
                  param_value: str,
                  annotation: str = None
                  ) -> None:
        if annotation is not None:
            if isinstance(annotation, list):
                param_name += str(Annotation("array", list_inner_type=annotation[0]))
            else:
                param_name += str(Annotation(annotation))

        self.params.update({param_name: param_value})

    def __str__(self):
        label = f'\n\nclass {self.classname}:\n'
        if self.predecessor is not None:
            label = f'\n\nclass {self.classname}({self.predecessor}):\n'    

        label += str(self.description)

        for name, value in self.params.items():
            is_keyword = ''
            if name in keyword.kwlist or name[0] in string.digits:
                is_keyword = '_'
            label += f'\t{is_keyword}{name} = {value}\n'
        return label
