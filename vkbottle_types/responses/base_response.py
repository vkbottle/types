from typing import Any

from vkbottle_types.base_model import PYDICT_APAPTER_TO_RAW_JSON, PYOBJECT_ADAPTER_TO_RAW_JSON, BaseModel, Field


class BaseResponse(BaseModel):
    response: Any
    raw_json: str | None = Field(default=None, init=False)

    @property
    def raw(self) -> str:
        return PYOBJECT_ADAPTER_TO_RAW_JSON.dump_json(self.response).decode()


class DictResponse(BaseResponse):
    response: dict[str, Any]

    def __init__(self, **data: Any) -> None:
        super().__init__(response=data)

    @property
    def raw(self) -> str:
        return PYDICT_APAPTER_TO_RAW_JSON.dump_json(self.response).decode()


__all__ = ("BaseResponse", "DictResponse")
