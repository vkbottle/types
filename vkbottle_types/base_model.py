import pydantic
import typing_extensions as typing

if typing.TYPE_CHECKING:

    @typing.dataclass_transform(
        kw_only_default=True,
        field_specifiers=(pydantic.Field, pydantic.PrivateAttr),
    )
    class BaseModel(pydantic.BaseModel):
        @classmethod
        def from_raw(cls, data: bytes, /, *, strict: bool = False) -> typing.Self: ...

        def to_dict(self) -> typing.Dict[str, typing.Any]: ...

else:

    class BaseModel(pydantic.BaseModel):
        model_config = pydantic.ConfigDict(frozen=True)

        @classmethod
        def from_raw(cls, data, /, *, strict=False):
            return cls.model_validate_json(data, strict=strict)

        def to_dict(self):
            return cls.model_dump()


Field = pydantic.Field


__all__ = ("BaseModel", "Field")
