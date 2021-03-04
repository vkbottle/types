from .response_utils import (
    generate_response_dir,
    put_responses_by_filename
)
from .models import ResponseModel
from .models import jsonschema_object_factory
from utils.titles import Imports, UpdateForwardRefs
from utils.strings_util import get_type_from_reference


def write_response_alias(schema_body: dict, file: 'File') -> None:
    for classname, body in schema_body.items():
        annotation = f': Optional["{classname}Model"]'
        properties = {'response' + annotation: None}
        file.write(str(ResponseModel(classname, **properties)))


def parse_file(schema_path: str, filepath_to: str, **imports) -> None:
    files_dir = f'{filepath_to}/responses'
    filenames, json_dict = generate_response_dir(schema_path, files_dir)
    categorized_responses = {name: {} for name in sorted(filenames)}
    definitions = json_dict['definitions']

    responses_by_files = put_responses_by_filename(
                                                  definitions,
                                                  categorized_responses)

    for filename, schema_body in responses_by_files.items():
        with open(f'{filepath_to}/responses/{filename}.py', 'w') as file:
            file.write(str(Imports(**imports)))
            write_response_alias(schema_body, file)

            for classname, body in schema_body.items():
                schema_object = jsonschema_object_factory(classname + 'Model', body['properties'])

                file.write(str(schema_object))
            file.write('\n' + str(UpdateForwardRefs(**schema_body)))
