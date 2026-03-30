from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import PrettyCardsPrettyCard, PrettyCardsPrettyCardOrError
from vkbottle_types.responses.base_response import BaseResponse


class PrettyCardsCreateResponseModel(BaseModel):
    owner_id: int = Field()
    card_id: str = Field()


class PrettyCardsCreateResponse(BaseResponse):
    response: "PrettyCardsCreateResponseModel" = Field()


class PrettyCardsDeleteResponseModel(BaseModel):
    owner_id: int = Field()
    card_id: str = Field()
    error: str | None = Field(
        default=None,
    )


class PrettyCardsDeleteResponse(BaseResponse):
    response: "PrettyCardsDeleteResponseModel" = Field()


class PrettyCardsEditResponseModel(BaseModel):
    owner_id: int = Field()
    card_id: str = Field()


class PrettyCardsEditResponse(BaseResponse):
    response: "PrettyCardsEditResponseModel" = Field()


class PrettyCardsGetByIdResponse(BaseResponse):
    response: list["PrettyCardsPrettyCardOrError"] = Field()


class PrettyCardsGetUploadURLResponse(BaseResponse):
    response: str = Field()


class PrettyCardsGetResponseModel(BaseModel):
    count: int = Field()
    items: list["PrettyCardsPrettyCard"] = Field()


class PrettyCardsGetResponse(BaseResponse):
    response: "PrettyCardsGetResponseModel" = Field()
