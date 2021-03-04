from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class SearchPodcastResponse(BaseResponse):
	response: Optional["SearchPodcastResponseModel"] = None


class SearchPodcastResponseModel(BaseResponse):
	podcasts: Optional[List["PodcastExternalData"]] = None
	results_total: Optional[int] = None

SearchPodcastResponse.update_forward_refs()