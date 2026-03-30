from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    GroupsGroupFull,
    NewsfeedCommentsItem,
    NewsfeedList,
    NewsfeedListFull,
    NewsfeedNewsfeedItem,
    UsersSubscriptionsItem,
    UsersUserFull,
    WallWallpostFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class NewsfeedGenericResponseModel(BaseModel):
    items: list["NewsfeedNewsfeedItem"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()
    lives_items: list["NewsfeedNewsfeedItem"] | None = Field(
        default=None,
    )


class NewsfeedGenericResponse(BaseResponse):
    response: "NewsfeedGenericResponseModel" = Field()


class NewsfeedGetBannedExtendedResponseModel(BaseModel):
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class NewsfeedGetBannedExtendedResponse(BaseResponse):
    response: "NewsfeedGetBannedExtendedResponseModel" = Field()


class NewsfeedGetBannedResponseModel(BaseModel):
    groups: list[int] | None = Field(
        default=None,
    )
    members: list[int] | None = Field(
        default=None,
    )


class NewsfeedGetBannedResponse(BaseResponse):
    response: "NewsfeedGetBannedResponseModel" = Field()


class NewsfeedGetCommentsResponseModel(BaseModel):
    items: list["NewsfeedCommentsItem"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class NewsfeedGetCommentsResponse(BaseResponse):
    response: "NewsfeedGetCommentsResponseModel" = Field()


class NewsfeedGetListsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["NewsfeedListFull"] = Field()


class NewsfeedGetListsExtendedResponse(BaseResponse):
    response: "NewsfeedGetListsExtendedResponseModel" = Field()


class NewsfeedGetListsResponseModel(BaseModel):
    count: int = Field()
    items: list["NewsfeedList"] = Field()


class NewsfeedGetListsResponse(BaseResponse):
    response: "NewsfeedGetListsResponseModel" = Field()


class NewsfeedGetMentionsResponseModel(BaseModel):
    count: int = Field()
    items: list["WallWallpostFull"] = Field()


class NewsfeedGetMentionsResponse(BaseResponse):
    response: "NewsfeedGetMentionsResponseModel" = Field()


class NewsfeedGetSuggestedSourcesResponseModel(BaseModel):
    count: int = Field()
    items: list["UsersSubscriptionsItem"] = Field()


class NewsfeedGetSuggestedSourcesResponse(BaseResponse):
    response: "NewsfeedGetSuggestedSourcesResponseModel" = Field()


class NewsfeedIgnoreItemResponseModel(BaseModel):
    status: bool = Field(default=1)


class NewsfeedIgnoreItemResponse(BaseResponse):
    response: "NewsfeedIgnoreItemResponseModel" = Field()


class NewsfeedSaveListResponse(BaseResponse):
    response: int = Field()


class NewsfeedSearchExtendedResponseModel(BaseModel):
    items: list["WallWallpostFull"] = Field()
    count: int = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )


class NewsfeedSearchExtendedResponse(BaseResponse):
    response: "NewsfeedSearchExtendedResponseModel" = Field()


class NewsfeedSearchExtendedStrictResponseModel(BaseModel):
    items: list["WallWallpostFull"] = Field()
    count: int = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )


class NewsfeedSearchExtendedStrictResponse(BaseResponse):
    response: "NewsfeedSearchExtendedStrictResponseModel" = Field()


class NewsfeedSearchResponseModel(BaseModel):
    items: list["WallWallpostFull"] = Field()
    count: int = Field()
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )


class NewsfeedSearchResponse(BaseResponse):
    response: "NewsfeedSearchResponseModel" = Field()


class NewsfeedSearchStrictResponseModel(BaseModel):
    items: list["WallWallpostFull"] = Field()
    count: int = Field()
    suggested_queries: list[str] | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )
    total_count: int | None = Field(
        default=None,
    )


class NewsfeedSearchStrictResponse(BaseResponse):
    response: "NewsfeedSearchStrictResponseModel" = Field()
