import typing_extensions as typing

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore  # noqa: F401


if typing.TYPE_CHECKING:

    @typing.dataclass_transform(
        kw_only_default=True,
        field_specifiers=(pydantic.Field, pydantic.PrivateAttr),
    )
    class BaseModel(pydantic.BaseModel):
        @classmethod
        def from_raw(cls, data: bytes) -> typing.Self: ...

        def to_dict(self) -> typing.Dict[str, typing.Any]: ...

else:

    class ModelMetaclass(pydantic.main.ModelMetaclass):
        def __new__(cls, *args: typing.Any, **kwargs: typing.Any) -> typing.Type[typing.Any]:
            return super().__new__(cls, *args, __resolve_forward_refs__=False, **kwargs)

    class BaseModel(pydantic.BaseModel, metaclass=ModelMetaclass):
        class Config:
            frozen = True

        @classmethod
        def from_raw(cls, data: bytes) -> typing.Self:
            return getattr(cls, "model_validate_json", cls.parse_raw)(data)

        def to_dict(self) -> typing.Dict[str, typing.Any]:
            return getattr(self, "model_dump", self.dict)()


Field = pydantic.Field


__all__ = ("BaseModel",)
