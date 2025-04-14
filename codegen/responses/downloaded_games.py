from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.responses.base_response import BaseResponse


class DownloadedGamesPaidStatusResponseModel(BaseModel):
    is_paid: bool = Field()


class DownloadedGamesPaidStatusResponse(BaseResponse):
    response: "DownloadedGamesPaidStatusResponseModel" = Field()
