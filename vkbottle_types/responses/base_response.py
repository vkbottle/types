import json
from typing import Any, Dict, Optional

from vkbottle_types.base_model import BaseModel, Field


class BaseResponse(BaseModel):
    response: Any
    raw_json: Optional[str] = Field(default=None)

    @property
    def raw(self) -> str:
        if not self.raw_json:
            raise AttributeError("You cannot get raw_json from here. Get a full raw_json from unnested response.")
        return self.raw_json


class DictResponse(BaseResponse):
    response: Dict[str, Any]

    def __init__(self, **data: Any) -> None:
        super().__init__(response=data)

    @property
    def raw(self) -> Optional[str]:  # type: ignore
        if not self.response:
            return None
        return json.dumps(self.response)


__all__ = ("BaseResponse", "DictResponse")
