import typing

from vkbottle_types.objects import PrettyCardsPrettyCard, PrettyCardsPrettyCardOrError
from vkbottle_types.responses.base_response import BaseResponse


class CreateResponse(BaseResponse):
    response: "CreateResponseModel"


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel"


class EditResponse(BaseResponse):
    response: "EditResponseModel"


class GetByIdResponse(BaseResponse):
    response: typing.List["PrettyCardsPrettyCardOrError"]


class GetUploadURLResponse(BaseResponse):
    response: str


class GetResponse(BaseResponse):
    response: "GetResponseModel"


class CreateResponseModel(BaseResponse):
    owner_id: typing.Optional[int] = None
    card_id: typing.Optional[str] = None


class DeleteResponseModel(BaseResponse):
    owner_id: typing.Optional[int] = None
    card_id: typing.Optional[str] = None
    error: typing.Optional[str] = None


class EditResponseModel(BaseResponse):
    owner_id: typing.Optional[int] = None
    card_id: typing.Optional[str] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PrettyCardsPrettyCard"]] = None


__all__ = (
    "CreateResponse",
    "CreateResponseModel",
    "DeleteResponse",
    "DeleteResponseModel",
    "EditResponse",
    "EditResponseModel",
    "GetByIdResponse",
    "GetResponse",
    "GetResponseModel",
    "GetUploadURLResponse",
    "PrettyCardsPrettyCard",
    "PrettyCardsPrettyCardOrError",
)
