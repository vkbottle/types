import typing

from vkbottle_types.objects import (
    AppsApp,
    AppsCatalogList,
    AppsLeaderboard,
    AppsScope,
    UsersUser,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class GetCatalogResponse(BaseResponse):
    response: AppsCatalogList


class GetFriendsListExtendedResponse(BaseResponse):
    response: "GetFriendsListExtendedResponseModel"


class GetFriendsListResponse(BaseResponse):
    response: "GetFriendsListResponseModel"


class GetLeaderboardExtendedResponse(BaseResponse):
    response: "GetLeaderboardExtendedResponseModel"


class GetLeaderboardResponse(BaseResponse):
    response: "GetLeaderboardResponseModel"


class GetMiniAppPoliciesResponse(BaseResponse):
    response: "GetMiniAppPoliciesResponseModel"


class GetScopesResponse(BaseResponse):
    response: "GetScopesResponseModel"


class GetScoreResponse(BaseResponse):
    response: int


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class ImageUploadResponse(BaseResponse):
    response: "ImageUploadResponseModel"


class SendRequestResponse(BaseResponse):
    response: int


class GetFriendsListExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetFriendsListResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class GetLeaderboardExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsLeaderboard"]] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None


class GetLeaderboardResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsLeaderboard"]] = None


class GetMiniAppPoliciesResponseModel(BaseResponse):
    privacy_policy: typing.Optional[str] = None
    terms: typing.Optional[str] = None


class GetScopesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsScope"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsApp"]] = None


class ImageUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    image: typing.Optional[str] = None


__all__ = (
    "AppsApp",
    "AppsCatalogList",
    "AppsLeaderboard",
    "AppsScope",
    "GetCatalogResponse",
    "GetFriendsListExtendedResponse",
    "GetFriendsListExtendedResponseModel",
    "GetFriendsListResponse",
    "GetFriendsListResponseModel",
    "GetLeaderboardExtendedResponse",
    "GetLeaderboardExtendedResponseModel",
    "GetLeaderboardResponse",
    "GetLeaderboardResponseModel",
    "GetMiniAppPoliciesResponse",
    "GetMiniAppPoliciesResponseModel",
    "GetResponse",
    "GetResponseModel",
    "GetScopesResponse",
    "GetScopesResponseModel",
    "GetScoreResponse",
    "ImageUploadResponse",
    "ImageUploadResponseModel",
    "SendRequestResponse",
    "UsersUser",
    "UsersUserFull",
)
