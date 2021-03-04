from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class GetFavoriteStickersResponse(BaseResponse):
	response: Optional["GetFavoriteStickersResponseModel"] = None


class GetProductsResponse(BaseResponse):
	response: Optional["GetProductsResponseModel"] = None


class GetStickersKeywordsResponse(BaseResponse):
	response: Optional["GetStickersKeywordsResponseModel"] = None


GetFavoriteStickersResponseModel = List[BaseSticker]


GetProductsResponseModel = List[StoreProduct]


class GetStickersKeywordsResponseModel(BaseResponse):
	count: Optional[int] = None
	dictionary: Optional[List["StoreStickersKeyword"]] = None
	chunks_count: Optional[int] = None
	chunks_hash: Optional[str] = None

GetFavoriteStickersResponse.update_forward_refs()
GetProductsResponse.update_forward_refs()
GetStickersKeywordsResponse.update_forward_refs()