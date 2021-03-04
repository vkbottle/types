from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetPostReachResponse(BaseResponse):
	response: Optional["GetPostReachResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


GetPostReachResponseModel = List[StatsWallpostStat]


GetResponseModel = List[StatsPeriod]

GetPostReachResponse.update_forward_refs()
GetResponse.update_forward_refs()