import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import AppsApp, AppsLeaderboard, AppsScope, UsersUserFull, UsersUserMin


class GetCatalogResponse(BaseResponse):
    response: "GetCatalogResponseModel" = None


class GetFriendsListResponse(BaseResponse):
    response: "GetFriendsListResponseModel" = None


class GetLeaderboardExtendedResponse(BaseResponse):
    response: "GetLeaderboardExtendedResponseModel" = None


class GetLeaderboardResponse(BaseResponse):
    response: "GetLeaderboardResponseModel" = None


class GetMiniAppPoliciesResponse(BaseResponse):
    response: "GetMiniAppPoliciesResponseModel" = None


class GetScopesResponse(BaseResponse):
    response: "GetScopesResponseModel" = None


class GetScoreResponse(BaseResponse):
    response: int = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class ImageUploadResponse(BaseResponse):
    response: "ImageUploadResponseModel" = None


class SendRequestResponse(BaseResponse):
    response: int = None


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


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AppsApp"]] = None


class ImageUploadResponseModel(BaseResponse):
    hash: typing.Optional[str] = None
    image: typing.Optional[str] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
