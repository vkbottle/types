import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class StoreGetFavoriteStickersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoreGetProductsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class StoreGetStickersKeywordsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
