from typing import Any, Optional

from vkbottle_types.base_model import BaseModel


class BaseResponse(BaseModel):
    _raw_json: Optional[str]
    response: Any

    @property
    def raw_json(self) -> str:
        if not self._raw_json:
            raise AttributeError(
                "You cannot get raw_json from here. Get a full raw_json from unnested response"
            )
        return self._raw_json
