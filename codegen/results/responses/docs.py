from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class AddResponse(BaseResponse):
	response: Optional["AddResponseModel"] = None


class DocUploadResponse(BaseResponse):
	response: Optional["DocUploadResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetTypesResponse(BaseResponse):
	response: Optional["GetTypesResponseModel"] = None


class GetUploadServer(BaseResponse):
	response: Optional["GetUploadServerModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class SaveResponse(BaseResponse):
	response: Optional["SaveResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


AddResponseModel = int


class DocUploadResponseModel(BaseResponse):
	file: Optional[str] = None


GetByIdResponseModel = List[DocsDoc]


class GetTypesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["DocsDocTypes"]] = None


GetUploadServerModel = Optional[BaseUploadServer]


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["DocsDoc"]] = None


class SaveResponseModel(BaseResponse):
	type: Optional["DocsDocAttachmentType"] = None
	audio_message: Optional["MessagesAudioMessage"] = None
	doc: Optional["DocsDoc"] = None
	graffiti: Optional["MessagesGraffiti"] = None


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["DocsDoc"]] = None

AddResponse.update_forward_refs()
DocUploadResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetTypesResponse.update_forward_refs()
GetUploadServer.update_forward_refs()
GetResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchResponse.update_forward_refs()