import typing

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
    items: typing.List["NewsfeedNewsfeedItem"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    lives_items: typing.Optional[typing.List["NewsfeedNewsfeedItem"]] = Field(
        default=None,
    )


class NewsfeedGenericResponse(BaseResponse):
    response: "NewsfeedGenericResponseModel" = Field()


class NewsfeedGetBannedExtendedResponseModel(BaseModel):
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class NewsfeedGetBannedExtendedResponse(BaseResponse):
    response: "NewsfeedGetBannedExtendedResponseModel" = Field()


class NewsfeedGetBannedResponseModel(BaseModel):
    groups: typing.Optional[typing.List[int]] = Field(
        default=None,
    )
    members: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class NewsfeedGetBannedResponse(BaseResponse):
    response: "NewsfeedGetBannedResponseModel" = Field()


class NewsfeedGetCommentsResponseModel(BaseModel):
    items: typing.List["NewsfeedCommentsItem"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class NewsfeedGetCommentsResponse(BaseResponse):
    response: "NewsfeedGetCommentsResponseModel" = Field()


class NewsfeedGetListsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["NewsfeedListFull"] = Field()


class NewsfeedGetListsExtendedResponse(BaseResponse):
    response: "NewsfeedGetListsExtendedResponseModel" = Field()


class NewsfeedGetListsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["NewsfeedList"] = Field()


class NewsfeedGetListsResponse(BaseResponse):
    response: "NewsfeedGetListsResponseModel" = Field()


class NewsfeedGetMentionsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["WallWallpostFull"] = Field()


class NewsfeedGetMentionsResponse(BaseResponse):
    response: "NewsfeedGetMentionsResponseModel" = Field()


class NewsfeedGetSuggestedSourcesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersSubscriptionsItem"] = Field()


class NewsfeedGetSuggestedSourcesResponse(BaseResponse):
    response: "NewsfeedGetSuggestedSourcesResponseModel" = Field()


class NewsfeedIgnoreItemResponseModel(BaseModel):
    status: bool = Field(default=1)


class NewsfeedIgnoreItemResponse(BaseResponse):
    response: "NewsfeedIgnoreItemResponseModel" = Field()


class NewsfeedSaveListResponse(BaseResponse):
    response: int = Field()


class NewsfeedSearchExtendedResponseModel(BaseModel):
    items: typing.List["WallWallpostFull"] = Field()
    count: int = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    suggested_queries: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )
    total_count: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedSearchExtendedResponse(BaseResponse):
    response: "NewsfeedSearchExtendedResponseModel" = Field()


class NewsfeedSearchExtendedStrictResponseModel(BaseModel):
    items: typing.List["WallWallpostFull"] = Field()
    count: int = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    suggested_queries: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )
    total_count: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedSearchExtendedStrictResponse(BaseResponse):
    response: "NewsfeedSearchExtendedStrictResponseModel" = Field()


class NewsfeedSearchResponseModel(BaseModel):
    items: typing.List["WallWallpostFull"] = Field()
    count: int = Field()
    suggested_queries: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )
    total_count: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedSearchResponse(BaseResponse):
    response: "NewsfeedSearchResponseModel" = Field()


class NewsfeedSearchStrictResponseModel(BaseModel):
    items: typing.List["WallWallpostFull"] = Field()
    count: int = Field()
    suggested_queries: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )
    total_count: typing.Optional[int] = Field(
        default=None,
    )


class NewsfeedSearchStrictResponse(BaseResponse):
    response: "NewsfeedSearchStrictResponseModel" = Field()
