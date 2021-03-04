import json
from utils.strings_util import (
    categorize_methods_as_files,
    snake_case_to_camel_case
)
from utils.os_utils import create_results_dir, create_python_files


def get_responses_titles(json_schema) -> list:
    return [title for title in json_schema['definitions'].keys()]


def split_responses_names(json_titles: list) -> list:
    filenames = set()
    for title in json_titles:
        filenames.add(title.split("_")[0])
    return list(filenames)


def generate_response_dir(schema_path: str, destination_path: str) -> None:
    create_results_dir(destination_path)
    with open(schema_path, 'r') as schema:
        json_dict = json.load(schema)
        titles = get_responses_titles(json_dict)
        filenames = split_responses_names(titles)
        create_python_files(destination_path, filenames)
        return filenames, json_dict


def put_responses_by_filename(definitions: dict, categorized: dict) -> dict:
    for key, definition in definitions.items():
        filebound = key.split('_')[0]
        classname = snake_case_to_camel_case("_".join(key.split('_')[1:]))
        resp = {classname: definition}
        categorized[filebound].update(resp)
    return categorized
