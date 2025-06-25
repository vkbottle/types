import enum
import math
import sys

import pydantic
import typing_extensions as typing
from pydantic_core import CoreSchema, core_schema

_NOT_SUPPORTED: typing.Final = "NOT_SUPPORTED"
_ENUM_FRIENDS: typing.Final = (str, int, float)


if typing.TYPE_CHECKING:

    @typing.dataclass_transform(
        kw_only_default=True,
        field_specifiers=(pydantic.Field, pydantic.PrivateAttr),
    )
    class BaseModel(pydantic.BaseModel):
        @classmethod
        def from_raw(cls, data: str | bytes, /, *, strict: bool = False) -> typing.Self: ...

        @classmethod
        def from_dict(cls, data: typing.Dict[str, typing.Any], /) -> typing.Self: ...

        def to_dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]: ...

        def to_raw(self, **kwargs: typing.Any) -> str: ...

else:

    class BaseModel(pydantic.BaseModel):
        model_config = pydantic.ConfigDict(frozen=True)

        @classmethod
        def from_raw(cls, data, /, *, strict=False):
            return cls.model_validate_json(data, strict=strict)

        @classmethod
        def from_dict(cls, data, /):
            return cls(**data)

        def to_dict(self, **kwargs):
            return self.model_dump(**kwargs)

        def to_raw(self, **kwargs):
            return self.model_dump_json(**kwargs)


class BaseEnumMeta(enum.EnumMeta, type):
    @staticmethod
    def __get_pydantic_core_schema__(_cls: typing.Any, _source_type: typing.Any, _handler: pydantic.GetCoreSchemaHandler) -> CoreSchema:
        return core_schema.no_info_after_validator_function(
            function=lambda x: _cls(x),  # type: ignore
            schema=getattr(core_schema, f"{_cls.__bases__[0].__name__}_schema", core_schema.any_schema)(),
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
            if any(friend in bases for friend in _ENUM_FRIENDS):
                classdict["NOT_SUPPORTED_MEMBER"] = _NOT_SUPPORTED if str in bases else math.inf if float in bases else sys.maxsize

            classdict["_missing_"] = classmethod(lambda cls, _: cls._member_map_["NOT_SUPPORTED_MEMBER"])
            classdict["__get_pydantic_core_schema__"] = classmethod(BaseEnumMeta.__get_pydantic_core_schema__)
            kwargs = dict(
                metacls=metacls,
                cls=cls,
                bases=bases,
                classdict=classdict,
            )

            if sys.version_info >= (3, 11):
                kwargs.update(
                    dict(
                        boundary=boundary,
                        _simple=_simple,
                    ),
                )

            return super().__new__(**kwargs, **kwds)


Field = pydantic.Field


__all__ = ("BaseEnumMeta", "BaseModel", "Field")
