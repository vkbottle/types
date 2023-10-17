import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field


class StorageValueResponseModel(BaseModel):
    key: str = Field()

    value: str = Field()


class StorageValueResponse(BaseResponse):
    response: "StorageValueResponseModel"
