from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetBannedExtendedResponse(BaseResponse):
	response: Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(BaseResponse):
	response: Optional["GetBannedResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
	response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetPhotoUploadServerResponse(BaseResponse):
	response: Optional["GetPhotoUploadServerResponseModel"] = None


class GetStatsResponse(BaseResponse):
	response: Optional["GetStatsResponseModel"] = None


class GetVideoUploadServerResponse(BaseResponse):
	response: Optional["GetVideoUploadServerResponseModel"] = None


class GetViewersExtendedV5115Response(BaseResponse):
	response: Optional["GetViewersExtendedV5115ResponseModel"] = None


class GetViewersExtendedResponse(BaseResponse):
	response: Optional["GetViewersExtendedResponseModel"] = None


class GetV5113Response(BaseResponse):
	response: Optional["GetV5113ResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class SaveResponse(BaseResponse):
	response: Optional["SaveResponseModel"] = None


class UploadResponse(BaseResponse):
	response: Optional["UploadResponseModel"] = None


class GetBannedExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List[int]] = None
	profiles: Optional[List["UsersUserFull"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class GetBannedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List[int]] = None


class GetByIdExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["StoriesStory"]] = None
	profiles: Optional[List["UsersUserFull"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["StoriesStory"]] = None


class GetPhotoUploadServerResponseModel(BaseResponse):
	upload_url: Optional[str] = None
	user_ids: Optional[List[int]] = None


GetStatsResponseModel = Optional[StoriesStoryStats]


class GetVideoUploadServerResponseModel(BaseResponse):
	upload_url: Optional[str] = None
	user_ids: Optional[List[int]] = None


class GetViewersExtendedV5115ResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["StoriesViewersItem"]] = None
	hidden_reason: Optional[str] = None


class GetViewersExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["UsersUserFull"]] = None


class GetV5113ResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["StoriesFeedItem"]] = None
	profiles: Optional[List["UsersUser"]] = None
	groups: Optional[List["GroupsGroup"]] = None
	need_upload_screen: Optional[bool] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["list"]] = None
	promo_data: Optional["StoriesPromoBlock"] = None
	profiles: Optional[List["UsersUser"]] = None
	groups: Optional[List["GroupsGroup"]] = None
	need_upload_screen: Optional[bool] = None


class SaveResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["StoriesStory"]] = None


class UploadResponseModel(BaseResponse):
	upload_result: Optional[str] = None

GetBannedExtendedResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetPhotoUploadServerResponse.update_forward_refs()
GetStatsResponse.update_forward_refs()
GetVideoUploadServerResponse.update_forward_refs()
GetViewersExtendedV5115Response.update_forward_refs()
GetViewersExtendedResponse.update_forward_refs()
GetV5113Response.update_forward_refs()
GetResponse.update_forward_refs()
SaveResponse.update_forward_refs()
UploadResponse.update_forward_refs()