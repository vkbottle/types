from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import FaveBookmark, FavePage, FaveTag, GroupsGroup, UsersUserFull
from vkbottle_types.responses.base_response import BaseResponse


class FaveAddTagResponse(BaseResponse):
    response: "FaveTag" = Field()


class FaveGetPagesResponseModel(BaseModel):
    count: int = Field()
    items: list["FavePage"] = Field()


class FaveGetPagesResponse(BaseResponse):
    response: "FaveGetPagesResponseModel" = Field()


class FaveGetTagsResponseModel(BaseModel):
    count: int = Field()
    items: list["FaveTag"] = Field()


class FaveGetTagsResponse(BaseResponse):
    response: "FaveGetTagsResponseModel" = Field()


class FaveGetExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["FaveBookmark"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroup"] | None = Field(
        default=None,
    )


class FaveGetExtendedResponse(BaseResponse):
    response: "FaveGetExtendedResponseModel" = Field()


class FaveGetResponseModel(BaseModel):
    count: int = Field()
    items: list["FaveBookmark"] = Field()


class FaveGetResponse(BaseResponse):
    response: "FaveGetResponseModel" = Field()


__all__ = (
    "FaveAddTagResponse",
    "FaveGetExtendedResponse",
    "FaveGetExtendedResponseModel",
    "FaveGetPagesResponse",
    "FaveGetPagesResponseModel",
    "FaveGetResponse",
    "FaveGetResponseModel",
    "FaveGetTagsResponse",
    "FaveGetTagsResponseModel",
)
