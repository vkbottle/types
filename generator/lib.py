import builtins
import json  # type: ignore
import os
import pathlib
import typing

import jinja2
import requests  # type: ignore
from tqdm import tqdm  # type: ignore

from . import parse_types
from .data import Category, Definition, Objects, factory
from .parse_types import get_complex_type, transform_ref  # noqa: F401
from .utility import camelcase, instring, makesafe, snake_case

URL = "https://raw.githubusercontent.com/VKCOM/vk-api-schema/master/{}/{}.json"
CATEGORIES = (
    "base",
    "users",
    "account",
    "address",
    "addresses",
    "ads",
    "adsweb",
    "appWidgets",
    "apps",
    "asr",
    "audio",
    "auth",
    "board",
    "bugtracker",
    "callback",
    "calls",
    "client",
    "comment",
    "database",
    "docs",
    "donut",
    "downloadedGames",
    "events",
    "fave",
    "gifts",
    "groups",
    "leadForms",
    "likes",
    "link",
    "market",
    "messages",
    "notes",
    "notifications",
    "oauth",
    "orders",
    "owner",
    "pages",
    "photos",
    "podcast",
    "podcasts",
    "polls",
    "prettyCards",
    "search",
    "secure",
    "stats",
    "status",
    "stickers",
    "storage",
    "store",
    "stories",
    "streaming",
    "support",
    "tasks",
    "translations",
    "friends",
    "utils",
    "video",
    "wall",
    "newsfeed",
    "widgets",
)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(pathlib.Path(__file__).parent / "templates")
)
env.globals.update(
    {
        "snake_case": snake_case,
        "camelcase": camelcase,
        "is_int": lambda x: isinstance(x, int),
        "makesafe": makesafe,
        "instring": instring,
        "unique": lambda iterable: set(iterable),
    }
)


def process_downloaded_category(dct: dict) -> Category:
    for key in ("methods", "objects", "responses"):
        if not dct.get(key):
            dct.pop(key, None)

    if methods := dct.get("methods", {}).get("methods"):
        for method in methods:
            method["name"] = method["name"].split(".")[1]
        dct["methods"] = methods

    category = factory.load(dct, Category)
    return category


def process_schema(categories_dcts: list[dict]) -> list[Category]:
    print("Processing schema...")
    categories = []
    for dct in tqdm(categories_dcts):
        if not dct:
            continue
        processed = process_downloaded_category(dct)
        categories.append(processed)
    return categories


def download_schema() -> list[Category]:
    print("Downloading schema...")

    categories_dcts = []
    for category_name in tqdm(CATEGORIES):
        dct = {"name": category_name}
        for file in ("methods", "objects", "responses"):
            result = requests.get(URL.format(category_name, file))
            if result.status_code == 200:
                dct[file] = result.json()
            else:
                dct[file] = None
        categories_dcts.append(dct)

    with open("original-schema.json", "w") as fp:
        json.dump(categories_dcts, fp)

    return process_schema(categories_dcts)


def save_schema(schema: list[Category], filename: str = "schema.json") -> None:
    with open(filename, "w") as fp:
        json.dump([factory.dump(c) for c in schema], fp)


def load_schema(filename: str = "schema.json") -> list[Category]:
    with open(filename, "r") as fp:
        data = json.load(fp)
        return [factory.load(c, Category) for c in data]


def load_and_save() -> list[Category]:
    path = pathlib.Path(input("Enter path to schema: "))
    if not path.exists():
        print(f"Path ({path}) does not exist!")
        exit(0)
    with open(path) as file:
        schema_data = json.load(file)
    schema = process_schema(schema_data)
    save_schema(schema)
    return schema


def get_schema_cli() -> list[Category]:
    commands = {
        1: "Use it [default]",
        2: "Download it once again",
        3: "Process from path and rewrite",
    }
    if pathlib.Path("schema.json").exists():
        option = input(
            "Existing 'schema.json' found.\n    "
            + "\n    ".join(["({}) {}".format(i, s) for i, s in commands.items()])
            + "\n: "
        )

        if not option.strip() or int(option) == 1:
            return load_schema()

        match int(option):
            case 2:
                schema = download_schema()
                save_schema(schema)
            case 3:
                schema = load_and_save()
        return schema

    commands = {
        1: "Download official schema [default]",
        2: "Process from path and save",
    }

    option = input(
        "Should new schema be downloaded from source?\n    "
        + "\n    ".join(["({}) {}".format(i, s) for i, s in commands.items()])
        + "\n: "
    )

    if not option.strip():
        option = 1  # type: ignore

    match int(option):
        case 1:
            schema = download_schema()
            save_schema(schema)
        case 2:
            schema = load_and_save()

    return schema


def apply_patches(schema: list[Category]) -> None:
    print("Applying patches...")
    # TODO


def create_folders(folders: list[tuple[str, ...]]) -> None:
    for folder in folders:
        pathlib.Path(*folder).mkdir(exist_ok=True)


def generate_methods(category: Category, path: str):
    if not category.methods:
        print("        - Methods not found!", end="\n\n")
        return

    imports = set()
    for method in category.methods:
        for response in typing.cast(dict, method.responses).values():
            if "response_hint" not in response:
                continue
            for t in response["response_hint"]["orig_types"]:
                if t["is_object"]:
                    imports.add(t["type"])
        for param in method.parameters:
            if "$ref" in param.items and "objects.json" in param.items["$ref"]:
                imports.add(transform_ref(param.items["$ref"]))

    template = env.get_template("methods.jinja2")
    generated = template.render(category=category)
    generated = generated.replace(
        "### IMPORTS",
        ("from vkbottle_types.objects import " + ", ".join(imports)) if imports else "",
    )
    pathlib.Path(path, "methods", snake_case(category.name) + ".py").write_text(generated)
    print("        + Methods successfully generated!", end="\n\n")


def generate_responses(category: Category, path: str) -> None:
    if not category.responses:
        print("        - Responses not found!")
        return

    definitions = get_definitions(category.responses)
    parse_types.IMPORTS_CACHE = set()
    template = env.get_template("responses.jinja2")
    generated = template.render(definitions=definitions)
    generated = generated.replace(
        "### IMPORTS",
        ("from vkbottle_types.objects import " + ", ".join(parse_types.IMPORTS_CACHE))
        if parse_types.IMPORTS_CACHE
        else "",
    )
    pathlib.Path(path, "responses", snake_case(category.name) + ".py").write_text(generated)
    print("        + Responses successfully generated!")


def process_responses(
    responses: dict[str, dict[str, str]], responses_definitions: dict[str, Definition]
) -> dict[str, dict[str, str]]:
    for response_name, response in responses.items():
        if "$ref" not in response:
            continue
        if (definition := responses_definitions.get(response["$ref"].split("/")[-1])) is not None:
            for prop in definition.properties:
                if prop.name == "response":
                    if (response_definition := definition.get_response_definition()) is not None:
                        if response_definition.properties or response_definition.enum:
                            hint = get_complex_type(response, response=True)
                        else:
                            hint = "typing.Dict[str, typing.Any]"
                    else:
                        hint = prop.get_type(response=True)

                    orig_type: str | list[str]
                    if "Literal[" in hint:
                        orig_type = hint
                    else:
                        orig_type = (
                            hint.replace("'", "")
                            .removeprefix("typing.")
                            .replace("List", "")
                            .replace("[", "")
                            .replace("]", "")
                            .strip()
                        )
                        if "Union" in orig_type:
                            orig_type = list(
                                map(str.strip, orig_type.replace("Union", "").split(","))
                            )
                        if "Dict" in orig_type:
                            orig_type = "dict"
                    responses[response_name]["response_hint"] = {  # type: ignore
                        "hint": hint,
                        "orig_types": [
                            {
                                "type": t,
                                "is_object": is_object(t, hint),
                            }
                            for t in orig_type
                        ]
                        if isinstance(orig_type, list)
                        else [
                            {
                                "type": orig_type,
                                "is_object": is_object(orig_type, hint),
                            }
                        ],
                    }

    return responses.copy()


def update_category_methods_responses(
    category: Category, responses_definitions: dict[str, Definition]
) -> None:
    for method in category.methods:
        responses = typing.cast(dict[str, dict[str, str]], method.responses)
        responses.update(process_responses(responses, responses_definitions))


def reorder_definitions(
    definitions: list[tuple[str, Definition, Category]],
) -> list[tuple[str, Definition, Category]]:
    l_bases_f = lambda d: len(d[1].allOf)  # noqa: E731
    s = sorted(definitions, key=l_bases_f)
    s = sorted(
        definitions,
        key=lambda d: 0
        if not l_bases_f(d)
        else (
            1
            + CATEGORIES.index(d[2].name)
            + any(b.lower().startswith(d[2].name.lower()) for b in d[1].get_bases())
        ),
    )
    return s


def generate_objects(definitions: list[tuple[str, Definition, Category]], path: str):
    definitions = reorder_definitions(definitions)
    template = env.get_template("objects.jinja2")
    generated = template.render(definitions=[(k, v) for (k, v, _) in definitions])
    pathlib.Path(path, "objects.py").write_text(generated)


def is_object(t: str, hint: str) -> bool:
    return t not in builtins.__dict__ and "Response" not in t and "Literal[" not in hint


def generate_category(category: Category, path: str, responses_definitions: dict[str, Definition]):
    generate_responses(category, path)
    update_category_methods_responses(category, responses_definitions)
    generate_methods(category, path)


def parse_properties(properties: dict[str, dict]) -> list[dict]:
    return [{"name": name, **prop, "data": prop} for name, prop in properties.items()]


def get_definition(
    name: str, definitions: typing.Iterable[typing.Tuple[str, Definition]]
) -> typing.Optional[Definition]:
    for definition_name, definition in definitions:
        if definition_name == name:
            return definition
    return None


def get_definitions(objects: Objects) -> typing.List[typing.Tuple[str, Definition]]:
    if not objects.definitions:
        return []

    definitions: typing.Dict[str, Definition] = {}
    sub_definitions: typing.Dict[str, typing.List[str]] = {}

    for definition_name, definition in typing.cast(
        typing.Dict[str, dict], objects.definitions
    ).items():
        if "properties" in definition:
            properties: typing.Dict[str, dict] = {}

            if isinstance(definition["properties"], dict):
                properties = definition["properties"]
            else:
                for prop in definition["properties"]:
                    properties[prop.pop("name")] = prop

            definition["properties"] = parse_properties(properties)

        definitions.update({definition_name: factory.load(definition, Definition)})

    return list(definitions.items())


def generate_schema(schema: list[Category], folder: str) -> None:
    create_folders([(folder,), (folder, "methods"), (folder, "responses")])

    print("Generating schema...")

    responses_definitions: dict[str, Definition] = {}
    for c in schema:
        if c.responses and c.responses.definitions:
            responses_definitions.update(get_definitions(c.responses))

    for category in schema:
        print(f"    * Generating category: {category.name!r}...")
        generate_category(category, folder, responses_definitions)

    definitions: dict[str, tuple[Definition, Category]] = {}
    for category in schema:
        if not category.objects:
            continue

        definitions.update(
            {k: (v, category) for k, v in get_definitions(category.objects)},
        )

    sub_definitions: typing.Dict[str, typing.List[str]] = {}
    for def_name, (def_, _) in definitions.items():
        for base in def_.allOf:
            if base.ref:
                name = base.ref.split("/")[-1]
                if name not in sub_definitions:
                    sub_definitions[name] = []
                if def_name not in sub_definitions[name]:
                    sub_definitions[name].append(def_name)
                base.definition = get_definition(
                    name, list((n, x[0]) for n, x in definitions.items())
                )

    for definition_name, (def_, _) in definitions.items():
        if (sub_defs := sub_definitions.get(definition_name)) is None:
            continue
        for def_name in sub_defs:
            if (d := definitions.get(def_name)) is None:
                continue
            def_.sub_definitions[camelcase(def_name)] = d[0]

    generate_objects([(k, *v) for k, v in definitions.items()], folder)

    print("Run ruff isort...")
    os.system(f"ruff check {folder} --select I --select F401 --fix")

    print("Run fuff formatter...")
    os.system(f"ruff format {folder}")


__all__ = (
    "get_schema_cli",
    "generate_schema",
    "apply_patches",
    "save_schema",
    "load_schema",
    "process_schema",
    "download_schema",
    "Category",
    "Definition",
    "Objects",
    "factory",
)
