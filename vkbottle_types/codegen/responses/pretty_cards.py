import typing
import enum
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import BaseImage, PrettyCardsButtonOneOf


class PrettyCardsButtonOneOfResponseModel(BaseModel):
    pass


class PrettyCardsButtonOneOfResponse(BaseResponse):
    response: "PrettyCardsButtonOneOfResponseModel"


class PrettyCardsPrettyCardResponseModel(BaseModel):
    card_id: str = Field(
        description="Card ID (long int returned as string)",
    )

    link_url: str = Field(
        description="Link URL",
    )

    photo: str = Field(
        description='Photo ID (format "<owner_id>_<media_id>")',
    )

    title: str = Field(
        description="Title",
    )

    button: typing.Optional["PrettyCardsButtonOneOf"] = Field(
        default=None,
        description="Button key",
    )

    button_text: typing.Optional[str] = Field(
        default=None,
        description="Button text in current language",
    )

    images: typing.Optional[typing.List[BaseImage]] = Field(
        default=None,
    )

    price: typing.Optional[str] = Field(
        default=None,
        description="Price if set (decimal number returned as string)",
    )

    price_old: typing.Optional[str] = Field(
        default=None,
        description="Old price if set (decimal number returned as string)",
    )


class PrettyCardsPrettyCardResponse(BaseResponse):
    response: "PrettyCardsPrettyCardResponseModel"


class PrettyCardsPrettyCardOrErrorResponseModel(BaseModel):
    pass


class PrettyCardsPrettyCardOrErrorResponse(BaseResponse):
    response: "PrettyCardsPrettyCardOrErrorResponseModel"
