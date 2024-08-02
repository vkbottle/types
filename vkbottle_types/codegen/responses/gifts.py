import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import GiftsGift
from vkbottle_types.responses.base_response import BaseResponse


class GiftsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GiftsGift"] = Field()


class GiftsGetResponse(BaseResponse):
    response: "GiftsGetResponseModel" = Field()
