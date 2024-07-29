import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class NewsfeedGenericResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetBannedExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetBannedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetCommentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetListsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetListsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetMentionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedGetSuggestedSourcesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedIgnoreItemResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedSaveListResponse(BaseResponse):
    response: int = Field()


class NewsfeedSearchExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedSearchExtendedStrictResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class NewsfeedSearchStrictResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
