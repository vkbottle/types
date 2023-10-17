import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import GiftsGiftPrivacy, GiftsLayout


class GiftsGiftResponseModel(BaseModel):
    date: typing.Optional[int] = Field(
        default=None,
        description="Date when gist has been sent in Unixtime",
    )

    from_id: typing.Optional[int] = Field(
        default=None,
        description="Gift sender ID",
    )

    gift: typing.Optional["GiftsLayout"] = Field(
        default=None,
    )

    gift_hash: typing.Optional[str] = Field(
        default=None,
        description="Hash",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Gift ID",
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Comment text",
    )

    privacy: typing.Optional["GiftsGiftPrivacy"] = Field(
        default=None,
    )


class GiftsGiftResponse(BaseResponse):
    response: "GiftsGiftResponseModel"


class GiftsGiftPrivacyResponseModel(enum.IntEnum):
    NAME_AND_MESSAGE_FOR_ALL = 0

    NAME_FOR_ALL = 1

    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsGiftPrivacyResponse(BaseResponse):
    response: "GiftsGiftPrivacyResponseModel"


class GiftsLayoutResponseModel(BaseModel):
    id: typing.Optional[int] = Field(
        default=None,
        description="Gift ID",
    )

    thumb_512: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 512 px in width",
    )

    thumb_256: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 256 px in width",
    )

    thumb_48: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 48 px in width",
    )

    thumb_96: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 96 px in width",
    )

    stickers_product_id: typing.Optional[int] = Field(
        default=None,
        description="ID of the sticker pack, if the gift is representing one",
    )

    is_stickers_style: typing.Optional[bool] = Field(
        default=None,
        description="Information whether gift represents a stickers style",
    )

    build_id: typing.Optional[str] = Field(
        default=None,
        description="ID of the build of constructor gift",
    )

    keywords: typing.Optional[str] = Field(
        default=None,
        description="Keywords used for search",
    )


class GiftsLayoutResponse(BaseResponse):
    response: "GiftsLayoutResponseModel"
