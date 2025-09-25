import typing

from vkbottle_types.base_model import BaseModel, Field

Response = typing.TypeVar("Response")


class ExecuteResponse(BaseModel, typing.Generic[Response]):
    response: Response = Field()


__all__ = ("ExecuteResponse",)
