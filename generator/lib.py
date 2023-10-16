import requests
from tqdm import tqdm
import json
from .data import Category, factory
from .types import get_complex_type
from .utility import camelcase, snake_case, makesafe, instring
from .data import Definition, Objects
from . import types
import pathlib
import jinja2

CATEGORIES = (
    "users",
    "account",
    "addresses",
    "ads",
    "adsweb",
    "appWidgets",
    "apps",
    "audio",
    "auth",
    "base",
    "board",
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
    "tasks",
    "friends",
    "utils",
    "video",
    "wall",
    "newsfeed",
    "widgets",
)


URL = "https://raw.githubusercontent.com/VKCOM/vk-api-schema/master/{}/{}.json"
env = jinja2.Environment(loader=jinja2.FileSystemLoader("generator/templates"))
env.globals.update(
    {
        "snake_case": snake_case,
        "camelcase": camelcase,
        "is_int": lambda x: isinstance(x, int),
        "makesafe": makesafe,
        "instring": instring,
    }
)


def process_downloaded_category(dct: dict) -> Category:
    methods, objects, responses = dct["methods"], dct["objects"], dct["responses"]
    if methods:
        methods = methods["methods"]
        for method in methods:
            method["name"] = method["name"].split(".")[1]
        dct["methods"] = methods
    if objects:
        dct["objects"] = objects
    if responses:
        dct["responses"] = responses
    category = factory.load(dct, Category)
    return category


def process_schema(categories_dcts: list[dict]) -> list[Category]:
    print("Processing schema...")
    categories = []
    for dct in tqdm(categories_dcts):
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
        option = 1

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
        return
    with open(
        pathlib.Path(path, "methods", snake_case(category.name) + ".py"), "w"
    ) as fs:
        template = env.get_template("methods.jinja2")
        generated = template.render(category=category)
        fs.write(generated)


def generate_responses(category: Category, path: str):
    definitions = get_definitions(category.objects)
    types.IMPORTS_CACHE = set()
    with open(
        pathlib.Path(path, "responses", snake_case(category.name) + ".py"), "w"
    ) as fs:
        template = env.get_template("responses.jinja2")
        generated = template.render(definitions=definitions)
        generated = generated.replace(
            "### IMPORTS",
            ("from vkbottle_types.objects import " + ", ".join(types.IMPORTS_CACHE))
            if types.IMPORTS_CACHE
            else "",
        )
        fs.write(generated)


def reorder_definitions(
    definitions: list[tuple[str, Definition, Category]]
) -> list[tuple[str, Definition]]:
    l_bases_f = lambda d: len(d[1].allOf)
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

    with open(pathlib.Path(path, "objects.py"), "w") as file:
        template = env.get_template("objects.jinja2")
        generated = template.render(definitions=[(k, v) for (k, v, _) in definitions])
        file.write(generated)


def generate_category(category: Category, path: str) -> None:
    generate_methods(category, path)
    generate_responses(category, path)


def parse_properties(properties: dict) -> list[dict]:
    return [{"name": name, **v, "data": v} for name, v in properties.items()]


def get_definitions(objects: Objects) -> list[tuple[str, Definition]]:
    if not objects:
        return []

    definitions = {}

    for definition_name, definition in objects.definitions.items():
        if "properties" in definition:
            if isinstance(definition["properties"], dict):
                definition["properties"] = parse_properties(
                    definition.get("properties", {}) or {}
                )
            else:
                dct = {}
                for prop in definition["properties"]:
                    name = prop.pop("name")
                    dct[name] = prop
                definition["properties"] = parse_properties(dct)

        definitions.update({definition_name: factory.load(definition, Definition)})

    return [(k, v) for k, v in definitions.items()]


def generate_schema(schema: list[Category], folder: str) -> None:
    create_folders([(folder,), (folder, "methods"), (folder, "responses")])

    print("Generating schema...")

    for category in schema:
        print(f"Category: {category.name}")
        generate_category(category, folder)

    definitions = {}
    for category in schema:
        if not category.objects:
            continue

        definitions.update(
            {k: (v, category) for k, v in get_definitions(category.objects)}
        )

    generate_objects([(k, *v) for k, v in definitions.items()], folder)
