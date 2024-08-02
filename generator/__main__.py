from .lib import apply_patches, generate_schema, get_schema_cli

if __name__ == "__main__":
    schema = get_schema_cli()
    apply_patches(schema)
    generate_schema(schema, "codegen")
    print()
    print("All done! ^_^")
