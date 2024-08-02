import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.responses.base_response import BaseResponse


class TranslationsTranslateResponseModel(BaseModel):
    texts: typing.Optional[typing.List[str]] = Field(
        default=None,
    )
    source_lang: typing.Optional[str] = Field(
        default=None,
    )


class TranslationsTranslateResponse(BaseResponse):
    response: "TranslationsTranslateResponseModel" = Field()
