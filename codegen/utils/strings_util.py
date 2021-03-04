import json
import re


def get_type_from_reference(str_ref) -> str:
    pattern = r'.*/(.*)'
    ref_type = re.search(pattern, str_ref).group(1)
    return snake_case_to_camel_case(ref_type)


def output_switch_decorator(function):
    """ If input is dict, then return dict
        If input is a single element, return single element
    """
    def wrapper(arg):
        keys_type = type(dict().keys())
        if not isinstance(arg, (keys_type, list)):
            arg = {arg: arg}
        result = function(arg)
        if len(arg) == 1:
            # get first value in returned dict
            return result[next(iter(result))]
        return result

    return wrapper


def get_json_dict(path: str) -> dict:
    with open(path, 'r') as f:
        return json.loads(f.read())


@output_switch_decorator
def snake_case_to_camel_case(string_list: list) -> dict:
    words_list: list = []
    for word in string_list:
        init, *temp = word.split('_')
        word = ''.join([init, *map(str.title, temp)])
        word = word.replace(word[0], word[0].upper(), 1)

        words_list.append(word)
    return dict(zip(string_list, words_list))


def camel_case_to_snake_case(string: str) -> dict:
    return \
        ''.join(
            "_"+symbol.lower()
            if symbol.isupper() else symbol
            for symbol in list(string)
        )


def convert_to_python_type(field):
    if field == 'integer':
        return 'int'
    elif field == 'string':
        return 'str'
    elif field == 'boolean':
        return 'bool'
    elif field == 'array':
        return 'list'
    return str(field)


def shift_json_dict_names(plain_data: str, classnames: str) -> dict:
    return {v: plain_data[k] for k, v in classnames.items()}


def categorize_methods_as_files(json_dict: dict) -> dict:
    filenames = set()
    for method_dict in json_dict['methods']:
        method_name = method_dict['name'].split('.')[0]
        filenames.add(method_name)

    classified_dict = {name: {} for name in filenames}

    return classified_dict
