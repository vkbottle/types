from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import GroupsGroupFull, StoriesFeedItem, StoriesStory, StoriesStoryStats, StoriesViewersItem, UsersUser, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class StoriesGetBannedExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class StoriesGetBannedExtendedResponse(BaseResponse):
    response: "StoriesGetBannedExtendedResponseModel" = Field()


class StoriesGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class StoriesGetBannedResponse(BaseResponse):
    response: "StoriesGetBannedResponseModel" = Field()


class StoriesGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["StoriesStory"] = Field()
    profiles: list["UsersUserFull"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class StoriesGetByIdExtendedResponse(BaseResponse):
    response: "StoriesGetByIdExtendedResponseModel" = Field()


class StoriesGetPhotoUploadServerResponseModel(BaseModel):
    upload_url: str = Field()
    user_ids: list[int] = Field()


class StoriesGetPhotoUploadServerResponse(BaseResponse):
    response: "StoriesGetPhotoUploadServerResponseModel" = Field()


class StoriesGetStatsResponse(BaseResponse):
    response: "StoriesStoryStats" = Field()


class StoriesGetVideoUploadServerResponseModel(BaseModel):
    upload_url: str = Field()
    user_ids: list[int] = Field()


class StoriesGetVideoUploadServerResponse(BaseResponse):
    response: "StoriesGetVideoUploadServerResponseModel" = Field()


class StoriesGetViewersExtendedV5115ResponseModel(BaseModel):
    count: int = Field()
    items: list["StoriesViewersItem"] = Field()
    hidden_reason: str | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )


class StoriesGetViewersExtendedV5115Response(BaseResponse):
    response: "StoriesGetViewersExtendedV5115ResponseModel" = Field()


class StoriesGetV5113ResponseModel(BaseModel):
    count: int = Field()
    items: list["StoriesFeedItem"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    need_upload_screen: bool | None = Field(
        default=None,
    )
    track_code: str | None = Field(
        default=None,
    )
    next_from: str | None = Field(
        default=None,
    )


class StoriesGetV5113Response(BaseResponse):
    response: "StoriesGetV5113ResponseModel" = Field()


class StoriesSaveResponseModel(BaseModel):
    count: int = Field()
    items: list["StoriesStory"] = Field()
    profiles: list["UsersUser"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class StoriesSaveResponse(BaseResponse):
    response: "StoriesSaveResponseModel" = Field()


class StoriesUploadResponseModel(BaseModel):
    upload_result: str | None = Field(
        default=None,
    )


class StoriesUploadResponse(BaseResponse):
    response: "StoriesUploadResponseModel" = Field()
