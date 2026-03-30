from vkbottle_types.base_model import Field
from vkbottle_types.objects import StatsPeriod, StatsWallpostStat
from vkbottle_types.responses.base_response import BaseResponse


class StatsGetPostReachResponse(BaseResponse):
    response: list["StatsWallpostStat"] = Field()


class StatsGetResponse(BaseResponse):
    response: list["StatsPeriod"] = Field()
