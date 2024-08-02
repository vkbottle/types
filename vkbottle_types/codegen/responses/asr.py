from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import AsrTask
from vkbottle_types.responses.base_response import BaseResponse


class AsrCheckStatusResponse(BaseResponse):
    response: "AsrTask" = Field()


class AsrProcessResponseModel(BaseModel):
    task_id: str = Field()


class AsrProcessResponse(BaseResponse):
    response: "AsrProcessResponseModel" = Field()
