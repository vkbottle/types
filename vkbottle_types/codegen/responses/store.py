import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    BaseStickersList,
    BaseImage,
    BaseBoolInt,
    StoreProductIcon,
    StoreStickersKeywordSticker,
    StoreStickersKeywordStickers,
)


class StoreProductResponseModel(BaseModel):
    id: int = Field(
        description="Id of the product",
    )

    type: typing.Literal["stickers"] = Field(
        description="Product type",
    )

    is_new: typing.Optional[bool] = Field(
        default=None,
        description="Information whether sticker product wasn't used after being purchased",
    )

    copyright: typing.Optional[str] = Field(
        default=None,
        description="Product copyright information",
    )

    base_id: typing.Optional[int] = Field(
        default=None,
        description="Id of the base pack (for sticker pack styles)",
    )

    style_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Array of style ids available for the sticker pack",
    )

    purchased: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is purchased (1 - yes, 0 - no)",
    )

    active: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is active (1 - yes, 0 - no)",
    )

    promoted: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is promoted (1 - yes, 0 - no)",
    )

    purchase_date: typing.Optional[int] = Field(
        default=None,
        description="Date (Unix time) when the product was purchased",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Title of the product",
    )

    stickers: typing.Optional["BaseStickersList"] = Field(
        default=None,
    )

    style_sticker_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Array of style sticker ids (for sticker pack styles)",
    )

    icon: typing.Optional["StoreProductIcon"] = Field(
        default=None,
        description="Array of icon images or icon set object of the product (for stickers product type)",
    )

    previews: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
        description="Array of preview images of the product (for stickers product type)",
    )

    has_animation: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the product is an animated sticker pack (for stickers product type)",
    )

    subtitle: typing.Optional[str] = Field(
        default=None,
        description="Subtitle of the product",
    )

    payment_region: typing.Optional[str] = Field(
        default=None,
    )

    is_vmoji: typing.Optional[bool] = Field(
        default=None,
        description="Information whether sticker pack is a vmoji pack",
    )

    title_lang_key: typing.Optional[str] = Field(
        default=None,
    )

    description_lang_key: typing.Optional[str] = Field(
        default=None,
    )

    url: typing.Optional[str] = Field(
        default=None,
    )


class StoreProductResponse(BaseResponse):
    response: "StoreProductResponseModel"


class StoreProductIconResponseModel(BaseModel):
    pass


class StoreProductIconResponse(BaseResponse):
    response: "StoreProductIconResponseModel"


class StoreStickersKeywordResponseModel(BaseModel):
    words: typing.List[str] = Field()

    user_stickers: typing.Optional["StoreStickersKeywordStickers"] = Field(
        default=None,
    )

    promoted_stickers: typing.Optional["StoreStickersKeywordStickers"] = Field(
        default=None,
    )

    stickers: typing.Optional[typing.List[StoreStickersKeywordSticker]] = Field(
        default=None,
    )


class StoreStickersKeywordResponse(BaseResponse):
    response: "StoreStickersKeywordResponseModel"


class StoreStickersKeywordStickerResponseModel(BaseModel):
    pack_id: int = Field(
        description="Pack id",
    )

    sticker_id: int = Field(
        description="Sticker id",
    )


class StoreStickersKeywordStickerResponse(BaseResponse):
    response: "StoreStickersKeywordStickerResponseModel"


class StoreStickersKeywordStickersResponseModel(BaseModel):
    pass


class StoreStickersKeywordStickersResponse(BaseResponse):
    response: "StoreStickersKeywordStickersResponseModel"
