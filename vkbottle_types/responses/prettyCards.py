import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import PrettyCardsPrettyCard


class CreateResponse(BaseResponse):
    response: typing.Optional["CreateResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: typing.Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
    response: typing.Optional["EditResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetUploadURLResponse(BaseResponse):
    response: typing.Optional["GetUploadURLResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


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


GetByIdResponseModel = typing.List[PrettyCardsPrettyCard]


GetUploadURLResponseModel = str


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["PrettyCardsPrettyCard"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
