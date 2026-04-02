from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.responses.base_response import BaseResponse


class TranslationsTranslateResponseModel(BaseModel):
    texts: list[str] | None = Field(
        default=None,
    )
    source_lang: str | None = Field(
        default=None,
    )


class TranslationsTranslateResponse(BaseResponse):
    response: "TranslationsTranslateResponseModel" = Field()


__all__ = (
    "TranslationsTranslateResponse",
    "TranslationsTranslateResponseModel",
)
