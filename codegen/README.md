# vk_schema_codegen
Python codegeneration for vk objects json schema (https://json-schema.org/) 

## Setup
Before launching the codegeneration you should setup
json schema directory and imports in generated files.

Imports are configured in this way at config/config.yaml:
```yaml
object_models_imports:
  enum:
    None
  typing:
    - Any
    - List
    - Optional
    - Union
  pydantic:
    - BaseModel

```
which called in __main__.py file:
```python
objects_imports: dict = CONFIG['object_models_imports']
```

Filepaths are configured in this way at config/config.yaml:
```yaml
schema_objects_path:
  vk_schema/objects.json
schema_methods_path:
  vk_schema/methods.json
```

By default, files to parse comes from https://github.com/VKCOM/vk-api-schema
but you can pass your own files, if their structure is the same as VK's.

## Usage

Just
```bash
python __main__.py
```

Results of the codegeneration are stored in results/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Each *_parser mostly is an independable parser with a simple interface.
If you want to add your own parser make sure to make its interface like this:
```python
parse_file(filepath, imports)
```

## Details

Objects parser consists of three types of models:
1. Structure models - parse json schema into python classes with string representation. Those are stored in models/schema_objects
2. Representation models - string representation for writing, are included in structure models.
3. Titles - imports etc.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)