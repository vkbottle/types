from typing import List, Optional

from vkbottle_types.objects import StorageValue

from .base_response import BaseResponse


class GetKeysResponse(BaseResponse):
    response: Optional["GetKeysResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetV5110Response(BaseResponse):
    response: Optional["GetV5110ResponseModel"] = None


class GetWithKeysResponse(BaseResponse):
    response: Optional["GetWithKeysResponseModel"] = None


GetKeysResponseModel = List[str]

GetResponseModel = str

GetV5110ResponseModel = List[StorageValue]

GetWithKeysResponseModel = List[StorageValue]

GetKeysResponse.update_forward_refs()
GetResponse.update_forward_refs()
GetV5110Response.update_forward_refs()
GetWithKeysResponse.update_forward_refs()
