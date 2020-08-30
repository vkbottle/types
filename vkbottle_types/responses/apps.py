from typing import Optional, List

from vkbottle_types.objects import (
    AppsLeaderboard,
    UsersUserMin,
    AppsScope,
    UsersUserFull,
    AppsApp,
)
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
    response: Optional["GetScoreResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class SendRequestResponse(BaseResponse):
    response: Optional["SendRequestResponseModel"] = None


class GetCatalogResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["AppsApp"]] = None


class GetFriendsListResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetLeaderboardExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["AppsLeaderboard"]] = None
    profiles: Optional[List["UsersUserMin"]] = None


class GetLeaderboardResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["AppsLeaderboard"]] = None


class GetScopesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["AppsScope"]] = None


GetScoreResponseModel = int


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["AppsApp"]] = None


SendRequestResponseModel = int

GetCatalogResponse.update_forward_refs()
GetFriendsListResponse.update_forward_refs()
GetLeaderboardExtendedResponse.update_forward_refs()
GetLeaderboardResponse.update_forward_refs()
GetScopesResponse.update_forward_refs()
GetScoreResponse.update_forward_refs()
GetResponse.update_forward_refs()
SendRequestResponse.update_forward_refs()
