import inspect
import typing

from vkbottle_types.objects import (
    AppsApp,
    AppsLeaderboard,
    AppsScope,
    UsersUserFull,
    UsersUserMin,
)

from .base_response import BaseResponse


class GetCatalogResponse(BaseResponse):
    response: typing.Optional["GetCatalogResponseModel"] = None


class GetFriendsListResponse(BaseResponse):
    response: typing.Optional["GetFriendsListResponseModel"] = None


class GetLeaderboardExtendedResponse(BaseResponse):
    response: typing.Optional["GetLeaderboardExtendedResponseModel"] = None


class GetLeaderboardResponse(BaseResponse):
    response: typing.Optional["GetLeaderboardResponseModel"] = None


class GetMiniAppPoliciesResponse(BaseResponse):
    response: typing.Optional["GetMiniAppPoliciesResponseModel"] = None


class GetScopesResponse(BaseResponse):
    response: typing.Optional["GetScopesResponseModel"] = None


class GetScoreResponse(BaseResponse):
    response: typing.Optional["GetScoreResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class ImageUploadResponse(BaseResponse):
    response: typing.Optional["ImageUploadResponseModel"] = None


class SendRequestResponse(BaseResponse):
    response: typing.Optional["SendRequestResponseModel"] = None


class GetCatalogResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsApp"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None


class GetFriendsListResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetLeaderboardExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsLeaderboard"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None


class GetLeaderboardResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsLeaderboard"]] = None


class GetMiniAppPoliciesResponseModel(BaseResponse):
    privacy_policy: typing.Optional[str] = None
    terms: typing.Optional[str] = None


class GetScopesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsScope"]] = None


GetScoreResponseModel = int


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsApp"]] = None


class ImageUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    image: typing.Optional[str] = None


SendRequestResponseModel = int


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
