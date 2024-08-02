import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import UsersSubscriptionsItem
from vkbottle_types.responses.base_response import BaseResponse


class LikesAddResponseModel(BaseModel):
    likes: int = Field()


class LikesAddResponse(BaseResponse):
    response: "LikesAddResponseModel" = Field()


class LikesDeleteResponseModel(BaseModel):
    likes: int = Field()


class LikesDeleteResponse(BaseResponse):
    response: "LikesDeleteResponseModel" = Field()


class LikesGetListExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersSubscriptionsItem"] = Field()
    liked_by_author: typing.Optional[dict] = Field(
        default=None,
    )
    liked_by_group: typing.Optional[dict] = Field(
        default=None,
    )


class LikesGetListExtendedResponse(BaseResponse):
    response: "LikesGetListExtendedResponseModel" = Field()


class LikesGetListResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class LikesGetListResponse(BaseResponse):
    response: "LikesGetListResponseModel" = Field()


class LikesIsLikedResponseModel(BaseModel):
    liked: bool = Field()
    copied: bool = Field()


class LikesIsLikedResponse(BaseResponse):
    response: "LikesIsLikedResponseModel" = Field()
