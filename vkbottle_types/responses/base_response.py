from typing import Any

import pydantic

from vkbottle_types.base_model import BaseModel, Field

PYDICT_APAPTER_TO_RAW_JSON = pydantic.TypeAdapter(dict[str, Any])


class BaseResponse(BaseModel):
    response: Any
    raw_json: str | None = Field(default=None)

    @property
    def raw(self) -> str:
        if not self.raw_json:
            raise AttributeError("You cannot get raw_json from here. Get a full raw_json from unnested response.")
        return self.raw_json


class DictResponse(BaseResponse):
    response: dict[str, Any]

    def __init__(self, **data: Any) -> None:
        super().__init__(response=data)

    @property
    def raw(self) -> str:  # type: ignore
        return PYDICT_APAPTER_TO_RAW_JSON.dump_json(self.response).decode()


__all__ = ("BaseResponse", "DictResponse")
