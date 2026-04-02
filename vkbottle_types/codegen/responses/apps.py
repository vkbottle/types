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
    items: list["UsersUserFull"] = Field()


class AppsGetFriendsListExtendedResponse(BaseResponse):
    response: "AppsGetFriendsListExtendedResponseModel" = Field()


class AppsGetFriendsListResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class AppsGetFriendsListResponse(BaseResponse):
    response: "AppsGetFriendsListResponseModel" = Field()


class AppsGetLeaderboardExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["AppsLeaderboard"] = Field()
    profiles: list["UsersUser"] | None = Field(
        default=None,
    )


class AppsGetLeaderboardExtendedResponse(BaseResponse):
    response: "AppsGetLeaderboardExtendedResponseModel" = Field()


class AppsGetLeaderboardResponseModel(BaseModel):
    count: int = Field()
    items: list["AppsLeaderboard"] = Field()


class AppsGetLeaderboardResponse(BaseResponse):
    response: "AppsGetLeaderboardResponseModel" = Field()


class AppsGetMiniAppPoliciesResponseModel(BaseModel):
    privacy_policy: str | None = Field(
        default=None,
    )
    terms: str | None = Field(
        default=None,
    )


class AppsGetMiniAppPoliciesResponse(BaseResponse):
    response: "AppsGetMiniAppPoliciesResponseModel" = Field()


class AppsGetScopesResponseModel(BaseModel):
    count: int = Field()
    items: list["AppsScope"] = Field()


class AppsGetScopesResponse(BaseResponse):
    response: "AppsGetScopesResponseModel" = Field()


class AppsGetScoreResponse(BaseResponse):
    response: int = Field()


class AppsGetSnippetsResponseModel(BaseModel):
    items: list["AppsCustomSnippet"] | None = Field(
        default=None,
    )


class AppsGetSnippetsResponse(BaseResponse):
    response: "AppsGetSnippetsResponseModel" = Field()


class AppsGetTestingGroupsResponse(BaseResponse):
    response: list["AppsTestingGroup"] = Field()


class AppsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["AppsApp"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class AppsGetResponse(BaseResponse):
    response: "AppsGetResponseModel" = Field()


class AppsImageUploadResponseModel(BaseModel):
    hash: str | None = Field(
        default=None,
    )
    image: str | None = Field(
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


__all__ = (
    "AppsAddSnippetResponse",
    "AppsAddSnippetResponseModel",
    "AppsCreatedGroupResponse",
    "AppsCreatedGroupResponseModel",
    "AppsGetCatalogResponse",
    "AppsGetFriendsListExtendedResponse",
    "AppsGetFriendsListExtendedResponseModel",
    "AppsGetFriendsListResponse",
    "AppsGetFriendsListResponseModel",
    "AppsGetLeaderboardExtendedResponse",
    "AppsGetLeaderboardExtendedResponseModel",
    "AppsGetLeaderboardResponse",
    "AppsGetLeaderboardResponseModel",
    "AppsGetMiniAppPoliciesResponse",
    "AppsGetMiniAppPoliciesResponseModel",
    "AppsGetResponse",
    "AppsGetResponseModel",
    "AppsGetScopesResponse",
    "AppsGetScopesResponseModel",
    "AppsGetScoreResponse",
    "AppsGetSnippetsResponse",
    "AppsGetSnippetsResponseModel",
    "AppsGetTestingGroupsResponse",
    "AppsImageUploadResponse",
    "AppsImageUploadResponseModel",
    "AppsIsNotificationsAllowedResponse",
    "AppsIsNotificationsAllowedResponseModel",
    "AppsSendRequestResponse",
)
