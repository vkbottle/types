from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetServerUrlResponse(BaseResponse):
	response: Optional["GetServerUrlResponseModel"] = None


class GetServerUrlResponseModel(BaseResponse):
	endpoint: Optional[str] = None
	key: Optional[str] = None

GetServerUrlResponse.update_forward_refs()