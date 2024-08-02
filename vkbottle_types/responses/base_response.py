import json
from typing import Any, Dict, Optional

from vkbottle_types.base_model import BaseModel, Field


class BaseResponse(BaseModel):
    response: Any
    _raw_json: Optional[str] = Field(default=None)

    @property
    def raw_json(self) -> str:
        if not self._raw_json:
            raise AttributeError(
                "You cannot get raw_json from here. " "Get a full raw_json from unnested response."
            )
        return self._raw_json


class DictResponse(BaseResponse):
    response: Dict[str, Any]

    def __init__(self, **data: Any) -> None:
        super().__init__(response=data)

    @property
    def _raw_json(self) -> Optional[str]:  # type: ignore
        if not self.response:
            return None
        return json.dumps(self.response)


__all__ = ("BaseResponse", "DictResponse")
