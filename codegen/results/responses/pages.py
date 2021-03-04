from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetHistoryResponse(BaseResponse):
	response: Optional["GetHistoryResponseModel"] = None


class GetTitlesResponse(BaseResponse):
	response: Optional["GetTitlesResponseModel"] = None


class GetVersionResponse(BaseResponse):
	response: Optional["GetVersionResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class ParseWikiResponse(BaseResponse):
	response: Optional["ParseWikiResponseModel"] = None


class SaveAccessResponse(BaseResponse):
	response: Optional["SaveAccessResponseModel"] = None


class SaveResponse(BaseResponse):
	response: Optional["SaveResponseModel"] = None


GetHistoryResponseModel = List[PagesWikipageHistory]


GetTitlesResponseModel = List[PagesWikipage]


GetVersionResponseModel = Optional[PagesWikipageFull]


GetResponseModel = Optional[PagesWikipageFull]


ParseWikiResponseModel = string


SaveAccessResponseModel = int


SaveResponseModel = int

GetHistoryResponse.update_forward_refs()
GetTitlesResponse.update_forward_refs()
GetVersionResponse.update_forward_refs()
GetResponse.update_forward_refs()
ParseWikiResponse.update_forward_refs()
SaveAccessResponse.update_forward_refs()
SaveResponse.update_forward_refs()