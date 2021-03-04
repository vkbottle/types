from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetKeysResponse(BaseResponse):
	response: Optional["GetKeysResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


GetKeysResponseModel = List[: Optional[List[str]]]


GetResponseModel = List[StorageValue]

GetKeysResponse.update_forward_refs()
GetResponse.update_forward_refs()