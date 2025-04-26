import enum

import pydantic
import typing_extensions as typing
from pydantic_core import CoreSchema, core_schema

if typing.TYPE_CHECKING:

    @typing.dataclass_transform(
        kw_only_default=True,
        field_specifiers=(pydantic.Field, pydantic.PrivateAttr),
    )
    class BaseModel(pydantic.BaseModel):
        @classmethod
        def from_raw(cls, data: bytes, /, *, strict: bool = False) -> typing.Self: ...

        @classmethod
        def from_dict(cls, data: typing.Dict[str, typing.Any], /) -> typing.Self: ...

        def to_dict(self) -> typing.Dict[str, typing.Any]: ...

else:

    class BaseModel(pydantic.BaseModel):
        model_config = pydantic.ConfigDict(frozen=True)

        @classmethod
        def from_raw(cls, data, /, *, strict=False):
            return cls.model_validate_json(data, strict=strict)

        @classmethod
        def from_dict(cls, data, /):
            return cls(**data)

        def to_dict(self):
            return cls.model_dump()


class BaseEnumMeta(enum.EnumMeta, type):
    @staticmethod
    def __get_pydantic_core_schema__(
        _cls: typing.Any,
        _source_type: typing.Any,
        _handler: pydantic.GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            lambda x: _cls(x),  # type: ignore
            core_schema.str_schema(),
        )

    if typing.TYPE_CHECKING:

        class BaseEnumMeta(enum.Enum):  # noqa
            NOT_SUPPORTED_MEMBER = enum.auto()

        NOT_SUPPORTED_MEMBER: typing.Literal[BaseEnumMeta.NOT_SUPPORTED_MEMBER]

    else:

        def __new__(
            metacls,
            cls,
            bases,
            classdict,
            *,
            boundary=None,
            _simple=False,
            **kwds,
        ):
            classdict["NOT_SUPPORTED_MEMBER"] = "NOT_SUPPORTED" if any(x in bases for x in (str, enum.StrEnum)) else -1234567890
            classdict["_missing_"] = classmethod(lambda cls, _: cls._member_map_["NOT_SUPPORTED_MEMBER"])
            classdict["__get_pydantic_core_schema__"] = classmethod(BaseEnumMeta.__get_pydantic_core_schema__)
            return super().__new__(metacls, cls, bases, classdict, boundary=boundary, _simple=_simple, **kwds)


Field = pydantic.Field


__all__ = ("BaseModel", "BaseEnumMeta", "Field")
