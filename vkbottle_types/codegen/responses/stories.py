import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import GroupsGroupFull, StoriesFeedItem, StoriesStory, StoriesStoryStats, StoriesViewersItem, UsersUser, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class StoriesGetBannedExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class StoriesGetBannedExtendedResponse(BaseResponse):
    response: "StoriesGetBannedExtendedResponseModel" = Field()


class StoriesGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class StoriesGetBannedResponse(BaseResponse):
    response: "StoriesGetBannedResponseModel" = Field()


class StoriesGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["StoriesStory"] = Field()
    profiles: typing.List["UsersUserFull"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class StoriesGetByIdExtendedResponse(BaseResponse):
    response: "StoriesGetByIdExtendedResponseModel" = Field()


class StoriesGetPhotoUploadServerResponseModel(BaseModel):
    upload_url: str = Field()
    user_ids: typing.List[int] = Field()


class StoriesGetPhotoUploadServerResponse(BaseResponse):
    response: "StoriesGetPhotoUploadServerResponseModel" = Field()


class StoriesGetStatsResponse(BaseResponse):
    response: "StoriesStoryStats" = Field()


class StoriesGetVideoUploadServerResponseModel(BaseModel):
    upload_url: str = Field()
    user_ids: typing.List[int] = Field()


class StoriesGetVideoUploadServerResponse(BaseResponse):
    response: "StoriesGetVideoUploadServerResponseModel" = Field()


class StoriesGetViewersExtendedV5115ResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["StoriesViewersItem"] = Field()
    hidden_reason: typing.Optional[str] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class StoriesGetViewersExtendedV5115Response(BaseResponse):
    response: "StoriesGetViewersExtendedV5115ResponseModel" = Field()


class StoriesGetV5113ResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["StoriesFeedItem"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    need_upload_screen: typing.Optional[bool] = Field(
        default=None,
    )
    track_code: typing.Optional[str] = Field(
        default=None,
    )
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class StoriesGetV5113Response(BaseResponse):
    response: "StoriesGetV5113ResponseModel" = Field()


class StoriesSaveResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["StoriesStory"] = Field()
    profiles: typing.Optional[typing.List["UsersUser"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class StoriesSaveResponse(BaseResponse):
    response: "StoriesSaveResponseModel" = Field()


class StoriesUploadResponseModel(BaseModel):
    upload_result: typing.Optional[str] = Field(
        default=None,
    )


class StoriesUploadResponse(BaseResponse):
    response: "StoriesUploadResponseModel" = Field()
