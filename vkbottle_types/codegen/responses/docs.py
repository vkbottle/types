import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import BaseUploadServer, DocsDoc
from vkbottle_types.responses.base_response import BaseResponse


class DocsAddResponse(BaseResponse):
    response: int = Field()


class DocsDocUploadResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DocsGetByIdResponse(BaseResponse):
    response: typing.List[DocsDoc] = Field()


class DocsGetTypesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DocsGetUploadServerResponse(BaseResponse):
    response: "BaseUploadServer" = Field()


class DocsGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DocsSaveResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class DocsSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
