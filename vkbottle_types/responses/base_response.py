from typing import Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):
    _raw_json: Optional[str]

    @property
    def raw_json(self) -> str:
        if not self.raw_json:
            raise AttributeError(
                "You cannot get raw_json from here. Get a full raw_json from unnested response"
            )
        return self._raw_json
