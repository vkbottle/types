import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import AppsCatalogList, AppsTestingGroup
from vkbottle_types.responses.base_response import BaseResponse


class AppsAddSnippetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsCreatedGroupResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetCatalogResponse(BaseResponse):
    response: "AppsCatalogList" = Field()


class AppsGetFriendsListExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetFriendsListResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetLeaderboardExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetLeaderboardResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetMiniAppPoliciesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetScopesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetScoreResponse(BaseResponse):
    response: int = Field()


class AppsGetSnippetsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsGetTestingGroupsResponse(BaseResponse):
    response: typing.List[AppsTestingGroup] = Field()


class AppsGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsImageUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsIsNotificationsAllowedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class AppsSendRequestResponse(BaseResponse):
    response: int = Field()
