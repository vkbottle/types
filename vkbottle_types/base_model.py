import enum
import math
import sys

import pydantic
import typing_extensions as typing
from pydantic_core import CoreSchema, core_schema

NOT_SUPPORTED: typing.Final = "NOT_SUPPORTED"

Field = pydantic.Field


def _is_friend(bases: tuple[type[typing.Any], ...], /) -> bool:
    return any(friend in bases for friend in ENUM_FRIENDS)


if typing.TYPE_CHECKING:

    @typing.dataclass_transform(
        kw_only_default=True,
        field_specifiers=(pydantic.Field, pydantic.PrivateAttr),
    )
    class BaseModel(pydantic.BaseModel):
        @classmethod
        def from_raw(cls, data: str | bytes, /, *, strict: bool = False) -> typing.Self: ...

        @classmethod
        def from_dict(cls, data: dict[str, typing.Any], /) -> typing.Self: ...

        @classmethod
        def object_build(cls, localns: typing.Mapping[str, typing.Any], /) -> None: ...

        @classmethod
        def set_original_module_namespace(cls, namespace: typing.Mapping[str, typing.Any], /) -> None: ...

        def to_dict(self, **kwargs: typing.Any) -> dict[str, typing.Any]: ...

        def to_raw(self, **kwargs: typing.Any) -> str: ...

else:
    ORIG_MODULE_NAMESPACE_ATTR = "__orig_module_namespace__"

    class BaseModel(pydantic.BaseModel):
        model_config = pydantic.ConfigDict(frozen=True)

        @classmethod
        def object_build(cls, localns, /):
            localns = dict(localns) if not isinstance(localns, dict) else localns
            cls.model_rebuild(_types_namespace=getattr(cls, ORIG_MODULE_NAMESPACE_ATTR, {}) | localns)

        @classmethod
        def set_original_module_namespace(cls, namespace, /) -> None:
            setattr(cls, ORIG_MODULE_NAMESPACE_ATTR, namespace)

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


class StrEnum(str, enum.Enum):
    def __str__(self) -> str:
        return self.value


class IntEnum(int, enum.Enum):
    def __int__(self) -> int:
        return self.value

    def __float__(self) -> float:
        return float(self.value)

    def __index__(self) -> int:
        return self.value


class FloatEnum(float, enum.Enum):
    def __int__(self) -> int:
        return int(self.value)

    def __float__(self) -> float:
        return self.value


class BaseEnumMeta(enum.EnumMeta, type):
    if typing.TYPE_CHECKING:

        class _BaseEnumMeta(enum.Enum):  # noqa
            NOT_SUPPORTED_MEMBER = enum.auto()

        NOT_SUPPORTED_MEMBER: typing.Literal[_BaseEnumMeta.NOT_SUPPORTED_MEMBER]

    else:

        @staticmethod
        def __get_pydantic_core_schema__(_cls: typing.Any, _source_type: typing.Any, _handler: pydantic.GetCoreSchemaHandler) -> CoreSchema:
            return core_schema.no_info_after_validator_function(
                function=lambda x: _cls(x),  # type: ignore
                schema=getattr(core_schema, f"{_cls.__base__.__name__}_schema", core_schema.any_schema)(),
            )

        @staticmethod
        def _member_missing(cls, value):
            return cls._member_map_["NOT_SUPPORTED_MEMBER"]

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
            if _is_friend(bases):
                classdict["NOT_SUPPORTED_MEMBER"] = next(
                    (value for base, value in NOT_SUPPORTED_VALUES.items() if base in bases),
                    NOT_SUPPORTED,
                )

            classdict["_missing_"] = classmethod(BaseEnumMeta._member_missing)
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


ENUM_FRIENDS: typing.Final = (str, int, float, StrEnum, IntEnum, FloatEnum)
NOT_SUPPORTED_VALUES: typing.Final[dict[typing.Any, typing.Any]] = {
    str: NOT_SUPPORTED,
    int: sys.maxsize,
    float: math.inf,
    StrEnum: NOT_SUPPORTED,
    FloatEnum: math.inf,
    IntEnum: sys.maxsize,
    enum.IntEnum: sys.maxsize,
    enum.IntFlag: sys.maxsize,
}


if sys.version_info >= (3, 11):
    NOT_SUPPORTED_VALUES.update({enum.StrEnum: NOT_SUPPORTED})


__all__ = ("BaseEnumMeta", "BaseModel", "Field", "FloatEnum", "IntEnum", "StrEnum")
