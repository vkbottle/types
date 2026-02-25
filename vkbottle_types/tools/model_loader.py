import importlib
import sys
from types import ModuleType
from pydantic import BaseModel


class ModelLoader:
    """Dynamically load modules and rebuild Pydantic models when accessed."""

    def __init__(self, base_package: str, module_names: list[str]):
        """Initialize the loader with a base package and list of module names."""
        self.base_package = base_package
        self._module_names = module_names
        self._loaded: dict[str, ModuleType] = {}
        self._rebuilt: set[type] = set()


    def _build_namespace_for_model(self, model: type) -> dict:
        """Build a combined namespace for a model, including loaded modules."""
        ns = {}
        
        module = sys.modules.get(model.__module__)
        if module:
            ns.update(vars(module))
        
        for m in self._loaded.values():
            ns.update(vars(m))
        
        return ns


    def _merge_with_parent_model(self, model: type[BaseModel], namespace: dict):
        """Merge fields with a parent model if it has the same name."""
        for parent in model.__bases__:
            if parent.__name__ == model.__name__ and issubclass(parent, BaseModel):
                parent.__pydantic_fields__.update(model.__pydantic_fields__)
                parent.model_rebuild(force=True, _types_namespace=namespace)

                missing = {
                    name: field
                    for name, field in parent.__pydantic_fields__.items()
                    if name not in model.__pydantic_fields__
                }
                if missing:
                    model.__pydantic_fields__.update(missing)


    def rebuild_model(self, model: type[BaseModel]):
        """Rebuild a Pydantic model using the proper namespace and merge with parents."""
        if model in self._rebuilt:
            return model

        namespace = self._build_namespace_for_model(model)
        model.model_rebuild(force=True, _types_namespace=namespace)
        self._merge_with_parent_model(model, namespace)

        self._rebuilt.add(model)
        return model


    def load(self, name: str):
        """Lazily load modules and rebuild models when accessing attributes."""
        for module_name in self._module_names:
            if module_name not in self._loaded:
                module = importlib.import_module(f"{self.base_package}.{module_name}")
                self._loaded[module_name] = module

            module = self._loaded[module_name]

            if hasattr(module, name):
                value = getattr(module, name)

                if (
                    isinstance(value, type)
                    and issubclass(value, BaseModel)
                    and value is not BaseModel
                ):
                    self.rebuild_model(value)

                return value

        raise AttributeError(f"module {self.base_package} has no attribute {name}")
    