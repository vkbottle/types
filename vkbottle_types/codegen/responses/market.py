import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class MarketAddAlbumResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketAddPropertyVariantResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketAddPropertyResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketAddResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketCreateCommentResponse(BaseResponse):
    response: int = Field()


class MarketGetAlbumByIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetAlbumsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetByIdExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetByIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetCategoriesNewResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetGroupOrdersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetOrderByIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetOrderItemsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetOrdersExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetOrdersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetPropertiesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketGroupItemsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketPhotoIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketSearchBasicResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketSearchExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MarketSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
