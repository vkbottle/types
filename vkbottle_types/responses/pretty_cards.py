import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import PrettyCardsPrettyCard


class CreateResponse(BaseResponse):
    response: "CreateResponseModel" = None


class DeleteResponse(BaseResponse):
    response: "DeleteResponseModel" = None


class EditResponse(BaseResponse):
    response: "EditResponseModel" = None


class GetByIdResponse(BaseResponse):
    response: typing.List["PrettyCardsPrettyCard"] = None


class GetUploadURLResponse(BaseResponse):
    response: str = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
