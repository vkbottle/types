import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class WallCreateCommentResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallEditResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetByIdExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetByIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetCommentExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetCommentResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetCommentsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetRepostsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallParseAttachedLinkResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallPostAdsStealthResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallPostResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallRepostResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallSearchExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class WallSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
