from .lib import get_schema_cli, apply_patches, generate_schema, process_schema


if __name__ == "__main__":
    schema = get_schema_cli()
    apply_patches(schema)
    generate_schema(schema, "codegen")
    print("All done! ^_^")
