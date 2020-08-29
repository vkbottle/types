import typing
from typing import Optional

from vkbottle_types.objects import apps, users
from .base_response import BaseResponse


class GetCatalogResponse(BaseResponse):
    response: Optional["GetCatalogResponseModel"] = None


class GetFriendsListResponse(BaseResponse):
    response: Optional["GetFriendsListResponseModel"] = None


class GetLeaderboardExtendedResponse(BaseResponse):
    response: Optional["GetLeaderboardExtendedResponseModel"] = None


class GetLeaderboardResponse(BaseResponse):
    response: Optional["GetLeaderboardResponseModel"] = None


class GetScopesResponse(BaseResponse):
    response: Optional["GetScopesResponseModel"] = None


class GetScoreResponse(BaseResponse):
    response: Optional[int] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SendRequestResponse(BaseResponse):
    response: Optional[int] = None


class GetCatalogResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["apps.App"]] = None


class GetFriendsListResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None


class GetLeaderboardExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["apps.Leaderboard"]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None


class GetLeaderboardResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["apps.Leaderboard"]] = None


class GetScopesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["apps.Scope"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["apps.App"]] = None
