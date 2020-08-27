import json

with open("objects.json", "r") as file:
    objects = json.loads(file.read())["definitions"]
    ref_objects = {}
    for definition, def_object in objects.items():
        base_name = definition.split("_")[0]
        definition = "_".join(definition.split("_")[1:])
        name = "".join(
            s.upper() if i == 0 or list(definition)[i - 1] == "_" else s
            for i, s in enumerate(definition)
            if s != "_"
        )
        if base_name not in ref_objects:
            ref_objects[base_name] = {}
        ref_objects[base_name][name] = def_object

all_object_types = set(list(ref_objects.keys())[::-1])
RESERVED_NAMES = ["for", "from", "import", "class", "global"]
types = {
    "integer": "int",
    "string": "str",
    "boolean": "bool",
    "object": "typing.Dict[Any, Any]",
    "number": "float",
}

for base_name, definitions in ref_objects.items():
    with open(f"{base_name}.py", "w") as file:
        base_names_2_import = []
        lines = [
            "from .base_model import BaseObject\n",
            "",
            "from typing import Optional, Union, Any, List\nimport typing\nimport enum\n\n",
        ]
        descriptions = {}
        line_comment = None
        for definition_name, definition in definitions.items():
            if "type" not in definition:
                ref = definition["$ref"].split("/")[-1]
                ref_base_name = ref.split("_")[0]
                ref_definition = "_".join(ref.split("_")[1:])
                name = "".join(
                    s.upper() if i == 0 or list(ref_definition)[i - 1] == "_" else s
                    for i, s in enumerate(ref_definition)
                    if s != "_"
                )
                if ref_base_name != base_name:
                    base_names_2_import.append(ref_base_name)
                    line_comment = len(lines) + 2
                    lines.extend(
                        [
                            f"class {definition_name}({base_name}.{name}):\n",
                            f'\t""" VK Object {base_name}/{definition_name}\n',
                            f"\t#FIXME Comment is undefined",
                            f'\t"""\n',
                        ]
                    )
                else:
                    line_comment = len(lines) + 2
                    lines.extend(
                        [
                            f'class {definition_name}("{name}"):\n',
                            f'\t""" VK Object {base_name}/{definition_name}\n',
                            f"\t#FIXME Comment is undefined",
                            f'\t"""\n',
                        ]
                    )
                continue
            elif definition["type"] == "object":
                line_comment = len(lines) + 2
                lines.extend(
                    [
                        f"class {definition_name}(BaseObject):\n",
                        f'\t""" VK Object {base_name}/{definition_name}\n',
                        f"\t#FIXME Comment is undefined",
                        f'\t"""\n',
                    ]
                )
                if "properties" in definition:
                    for property_name, property_obj in definition["properties"].items():
                        if property_name[0].isdigit():
                            property_name = "_" + property_name
                        elif property_name in RESERVED_NAMES:
                            property_name = "_" + property_name
                        if "type" in property_obj:
                            if isinstance(property_obj["type"], list):
                                types_from_list = [
                                    types.get(t, "Any") for t in property_obj["type"]
                                ]
                                lines.append(
                                    f"\t{property_name}: Optional[Union[{', '.join(types_from_list)}]] = None\n"
                                )
                            elif (
                                "items" in property_obj
                                and property_obj["type"] == "array"
                            ):
                                items = property_obj["items"]
                                if "type" in items:
                                    if items["type"] == "array":
                                        lines.append(
                                            f"\t{property_name}: Optional[List[dict]] = None\n"
                                        )
                                    else:
                                        lines.append(
                                            f"\t{property_name}: Optional[List[{types[items['type']]}]] = None\n"
                                        )
                                elif "$ref" in items:
                                    ref = items["$ref"].split("/")[-1]
                                    ref_base_name = ref.split("_")[0]
                                    ref_definition = "_".join(ref.split("_")[1:])
                                    name = "".join(
                                        s.upper()
                                        if i == 0 or list(ref_definition)[i - 1] == "_"
                                        else s
                                        for i, s in enumerate(ref_definition)
                                        if s != "_"
                                    )
                                    if ref_base_name != base_name:
                                        base_names_2_import.append(ref_base_name)
                                        lines.append(
                                            f"\t{property_name}: Optional[List[{ref_base_name}.{name}]] = None\n"
                                        )
                                    else:
                                        lines.append(
                                            f'\t{property_name}: Optional[List["{name}"]] = None\n'
                                        )
                                else:
                                    raise ValueError
                            elif property_obj["type"] in types:
                                lines.append(
                                    f"\t{property_name}: Optional[{types[property_obj['type']]}] = None\n"
                                )
                            else:
                                raise ValueError
                        else:
                            ref = property_obj["$ref"].split("/")[-1]
                            ref_base_name = ref.split("_")[0]
                            ref_definition = "_".join(ref.split("_")[1:])
                            name = "".join(
                                s.upper()
                                if i == 0 or list(ref_definition)[i - 1] == "_"
                                else s
                                for i, s in enumerate(ref_definition)
                                if s != "_"
                            )

                            if ref_base_name != base_name:
                                base_names_2_import.append(ref_base_name)
                                lines.append(
                                    f"\t{property_name}: Optional[{ref_base_name}.{name}] = None\n"
                                )
                            else:
                                lines.append(
                                    f'\t{property_name}: Optional["{name}"] = None\n'
                                )
            else:
                if "enum" not in definition:
                    lines.append(
                        f"{definition_name} = Optional[{types[definition['type']]}] = None  # {definition['description']}"
                    )
                else:
                    if definition["type"] == "string" and all(
                        isinstance(e, str) for e in definition["enum"]
                    ):
                        lines.append(f"class {definition_name}(enum.Enum):\n")
                        lines.append(
                            f"\t\"\"\" {definition.get('description', f'{definition_name} enum')} \"\"\"\n"
                        )
                        for enum in definition["enum"]:
                            lines.append(f'\t{enum.upper()} = "{enum}"\n')
                    elif definition["type"] == "integer" or all(
                        isinstance(e, int) for e in definition["enum"]
                    ):
                        enum_names = [
                            n.replace(" ", "_").lower() for n in definition["enumNames"]
                        ]
                        lines.append(f"class {definition_name}(enum.IntEnum):\n")
                        lines.append(
                            f"\t\"\"\" {definition.get('description', f'{definition_name} enum')} \"\"\"\n"
                        )
                        for i, code in enumerate(definition["enum"]):
                            lines.append(f"\t{enum_names[i]} = {code}\n")
                    else:
                        print(definition)
                        raise ValueError
            if line_comment:
                line_comment_string = ""
                if definition.get("properties"):
                    for prop_name, prop in definition["properties"].items():
                        if "description" in prop:
                            line_comment_string += (
                                f"\n\t{prop_name} - {prop['description']}"
                            )
                line_comment_string += "\n"
                lines[line_comment] = line_comment_string
            lines.append("\n\n")
        if base_names_2_import:
            lines[1] = f"from . import {', '.join(list(set(base_names_2_import)))}\n"

        file.writelines(lines)
