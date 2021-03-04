from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["GiftsGift"]] = None

GetResponse.update_forward_refs()