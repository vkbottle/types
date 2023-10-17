import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    FaveBookmarkType,
    BaseLink,
    FaveTag,
    VideoVideoFull,
    MarketMarketItem,
    GroupsGroupFull,
    WallWallpostFull,
    UsersUserFull,
    FavePageType,
)


class FaveBookmarkResponseModel(BaseModel):
    added_date: int = Field(
        description="Timestamp, when this item was bookmarked",
    )

    seen: bool = Field(
        description="Has user seen this item",
    )

    tags: typing.List[FaveTag] = Field()

    type: "FaveBookmarkType" = Field(
        description="Item type",
    )

    link: typing.Optional["BaseLink"] = Field(
        default=None,
    )

    post: typing.Optional["WallWallpostFull"] = Field(
        default=None,
    )

    product: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    video: typing.Optional["VideoVideoFull"] = Field(
        default=None,
    )


class FaveBookmarkResponse(BaseResponse):
    response: "FaveBookmarkResponseModel"


class FaveBookmarkTypeResponseModel(enum.Enum):
    POST = "post"

    VIDEO = "video"

    PRODUCT = "product"

    ARTICLE = "article"

    LINK = "link"

    CLIP = "clip"


class FaveBookmarkTypeResponse(BaseResponse):
    response: "FaveBookmarkTypeResponseModel"


class FavePageResponseModel(BaseModel):
    description: str = Field(
        description="Some info about user or group",
    )

    tags: typing.List[FaveTag] = Field()

    type: "FavePageType" = Field(
        description="Item type",
    )

    group: typing.Optional["GroupsGroupFull"] = Field(
        default=None,
    )

    updated_date: typing.Optional[int] = Field(
        default=None,
        description="Timestamp, when this page was bookmarked",
    )

    user: typing.Optional["UsersUserFull"] = Field(
        default=None,
    )


class FavePageResponse(BaseResponse):
    response: "FavePageResponseModel"


class FavePageTypeResponseModel(enum.Enum):
    USER = "user"

    GROUP = "group"

    HINTS = "hints"


class FavePageTypeResponse(BaseResponse):
    response: "FavePageTypeResponseModel"


class FaveTagResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Tag id",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Tag name",
    )


class FaveTagResponse(BaseResponse):
    response: "FaveTagResponseModel"
