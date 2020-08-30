from .base_response import BaseResponse
from vkbottle_types.objects import users, apps
from typing import Optional, Any, List, Union
import typing


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
    response: Optional["GetScoreResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SendRequestResponse(BaseResponse):
    response: Optional["SendRequestResponseModel"] = None


class GetCatalogResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["apps.App"]] = None


class GetFriendsListResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["users.UserFull"]] = None


class GetLeaderboardExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["apps.Leaderboard"]] = None
    profiles: Optional[List["users.UserMin"]] = None


class GetLeaderboardResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["apps.Leaderboard"]] = None


class GetScopesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["apps.Scope"]] = None


GetScoreResponseModel = int


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["apps.App"]] = None


SendRequestResponseModel = int
