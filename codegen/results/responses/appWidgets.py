from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetAppImageUploadServerResponse(BaseResponse):
	response: Optional["GetAppImageUploadServerResponseModel"] = None


class GetAppImagesResponse(BaseResponse):
	response: Optional["GetAppImagesResponseModel"] = None


class GetGroupImageUploadServerResponse(BaseResponse):
	response: Optional["GetGroupImageUploadServerResponseModel"] = None


class GetGroupImagesResponse(BaseResponse):
	response: Optional["GetGroupImagesResponseModel"] = None


class GetImagesByIdResponse(BaseResponse):
	response: Optional["GetImagesByIdResponseModel"] = None


class SaveAppImageResponse(BaseResponse):
	response: Optional["SaveAppImageResponseModel"] = None


class SaveGroupImageResponse(BaseResponse):
	response: Optional["SaveGroupImageResponseModel"] = None


class GetAppImageUploadServerResponseModel(BaseResponse):
	upload_url: Optional[str] = None


GetAppImagesResponseModel = Optional[AppWidgetsPhotos]


class GetGroupImageUploadServerResponseModel(BaseResponse):
	upload_url: Optional[str] = None


GetGroupImagesResponseModel = Optional[AppWidgetsPhotos]


GetImagesByIdResponseModel = List[AppWidgetsPhoto]


SaveAppImageResponseModel = Optional[AppWidgetsPhoto]


SaveGroupImageResponseModel = Optional[AppWidgetsPhoto]

GetAppImageUploadServerResponse.update_forward_refs()
GetAppImagesResponse.update_forward_refs()
GetGroupImageUploadServerResponse.update_forward_refs()
GetGroupImagesResponse.update_forward_refs()
GetImagesByIdResponse.update_forward_refs()
SaveAppImageResponse.update_forward_refs()
SaveGroupImageResponse.update_forward_refs()