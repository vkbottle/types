import logging
import json
from utils.os_utils import create_results_dir
from utils.titles import Imports
from .models import ClassForm

logging.basicConfig(level=logging.INFO)


def parse_file(filepath: str, filepath_to: str, **imports) -> None:
    base_dir = create_results_dir(f'{filepath_to}/methods')
    categories = sort_jsonmethods_schema(filepath)

    for category, methods in categories.items():
        with open(f"{base_dir}/{category}.py", 'w') as pyfile:
            construct_schema(pyfile, category, methods, **imports)


def construct_schema(file, category, methods, **imports):
    file.write("from vkbottle_types.responses import %s, base\n" % category)
    file.write(str(Imports(**imports)))
    form = ClassForm(category)
    for method in methods:
        form.add_method(method['name'], method)
    file.write(str(form))


def sort_jsonmethods_schema(path: str) -> dict:
    with open(path, 'r') as f:
        json_dict = json.load(f)
    return collecter(json_dict['methods'])


def collecter(methods: dict) -> dict:
    result = {}
    for method in methods:
        method_name = method['name'].split('.')

        if result.get(method_name[0]):
            result[method_name[0]].append(method)
        else:
            result[method_name[0]] = [method]
    return result
