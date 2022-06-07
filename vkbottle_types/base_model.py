import pydantic


class ModelMetaclass(pydantic.main.ModelMetaclass):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, __resolve_forward_refs__=False, **kwargs)


class BaseModel(pydantic.BaseModel, metaclass=ModelMetaclass):
    class Config:
        frozen = True


__all__ = ("BaseModel",)
