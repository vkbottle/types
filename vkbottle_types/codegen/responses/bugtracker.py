import typing

from vkbottle_types.base_model import Field
from vkbottle_types.responses.base_response import BaseResponse


class BugtrackerAddCompanyGroupsMembersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BugtrackerAddCompanyMembersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BugtrackerCreateCommentResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BugtrackerGetBugreportByIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BugtrackerGetCompanyGroupMembersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BugtrackerGetCompanyMembersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class BugtrackerGetDownloadVersionUrlResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
