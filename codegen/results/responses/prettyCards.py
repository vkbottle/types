from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class CreateResponse(BaseResponse):
	response: Optional["CreateResponseModel"] = None


class DeleteResponse(BaseResponse):
	response: Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
	response: Optional["EditResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetUploadURLResponse(BaseResponse):
	response: Optional["GetUploadURLResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class CreateResponseModel(BaseResponse):
	owner_id: Optional[int] = None
	card_id: Optional[str] = None


class DeleteResponseModel(BaseResponse):
	owner_id: Optional[int] = None
	card_id: Optional[str] = None
	error: Optional[str] = None


class EditResponseModel(BaseResponse):
	owner_id: Optional[int] = None
	card_id: Optional[str] = None


GetByIdResponseModel = List[PrettyCardsPrettycard]


GetUploadURLResponseModel = string


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["PrettyCardsPrettycard"]] = None

CreateResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetUploadURLResponse.update_forward_refs()
GetResponse.update_forward_refs()