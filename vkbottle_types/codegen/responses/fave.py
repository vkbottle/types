import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import FaveBookmark, FavePage, FaveTag, GroupsGroup, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class FaveAddTagResponse(BaseResponse):
    response: "FaveTag" = Field()


class FaveGetPagesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FavePage"] = Field()


class FaveGetPagesResponse(BaseResponse):
    response: "FaveGetPagesResponseModel" = Field()


class FaveGetTagsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FaveTag"] = Field()


class FaveGetTagsResponse(BaseResponse):
    response: "FaveGetTagsResponseModel" = Field()


class FaveGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FaveBookmark"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroup"]] = Field(
        default=None,
    )


class FaveGetExtendedResponse(BaseResponse):
    response: "FaveGetExtendedResponseModel" = Field()


class FaveGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["FaveBookmark"] = Field()


class FaveGetResponse(BaseResponse):
    response: "FaveGetResponseModel" = Field()
