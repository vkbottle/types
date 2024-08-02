import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    AppsApp,
    AppsCatalogList,
    AppsCustomSnippet,
    AppsLeaderboard,
    AppsScope,
    AppsTestingGroup,
    GroupsGroupFull,
    UsersUser,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class AppsAddSnippetResponseModel(BaseModel):
    snippet_id: int = Field()


class AppsAddSnippetResponse(BaseResponse):
    response: "AppsAddSnippetResponseModel" = Field()


class AppsCreatedGroupResponseModel(BaseModel):
    group_id: int = Field()


class AppsCreatedGroupResponse(BaseResponse):
    response: "AppsCreatedGroupResponseModel" = Field()


class AppsGetCatalogResponse(BaseResponse):
    response: "AppsCatalogList" = Field()


class AppsGetFriendsListExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()


class AppsGetFriendsListExtendedResponse(BaseResponse):
    response: "AppsGetFriendsListExtendedResponseModel" = Field()


class AppsGetFriendsListResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class AppsGetFriendsListResponse(BaseResponse):
    response: "AppsGetFriendsListResponseModel" = Field()


class AppsGetLeaderboardExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["AppsLeaderboard"] = Field()
    profiles: typing.Optional[typing.List["UsersUser"]] = Field(
        default=None,
    )


class AppsGetLeaderboardExtendedResponse(BaseResponse):
    response: "AppsGetLeaderboardExtendedResponseModel" = Field()


class AppsGetLeaderboardResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["AppsLeaderboard"] = Field()


class AppsGetLeaderboardResponse(BaseResponse):
    response: "AppsGetLeaderboardResponseModel" = Field()


class AppsGetMiniAppPoliciesResponseModel(BaseModel):
    privacy_policy: typing.Optional[str] = Field(
        default=None,
    )
    terms: typing.Optional[str] = Field(
        default=None,
    )


class AppsGetMiniAppPoliciesResponse(BaseResponse):
    response: "AppsGetMiniAppPoliciesResponseModel" = Field()


class AppsGetScopesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["AppsScope"] = Field()


class AppsGetScopesResponse(BaseResponse):
    response: "AppsGetScopesResponseModel" = Field()


class AppsGetScoreResponse(BaseResponse):
    response: int = Field()


class AppsGetSnippetsResponseModel(BaseModel):
    items: typing.Optional[typing.List["AppsCustomSnippet"]] = Field(
        default=None,
    )


class AppsGetSnippetsResponse(BaseResponse):
    response: "AppsGetSnippetsResponseModel" = Field()


class AppsGetTestingGroupsResponse(BaseResponse):
    response: typing.List["AppsTestingGroup"] = Field()


class AppsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["AppsApp"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class AppsGetResponse(BaseResponse):
    response: "AppsGetResponseModel" = Field()


class AppsImageUploadResponseModel(BaseModel):
    hash: typing.Optional[str] = Field(
        default=None,
    )
    image: typing.Optional[str] = Field(
        default=None,
    )


class AppsImageUploadResponse(BaseResponse):
    response: "AppsImageUploadResponseModel" = Field()


class AppsIsNotificationsAllowedResponseModel(BaseModel):
    is_allowed: bool = Field()


class AppsIsNotificationsAllowedResponse(BaseResponse):
    response: "AppsIsNotificationsAllowedResponseModel" = Field()


class AppsSendRequestResponse(BaseResponse):
    response: int = Field()
