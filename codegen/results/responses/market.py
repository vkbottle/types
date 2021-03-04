from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
	response: Optional["AddAlbumResponseModel"] = None


class AddResponse(BaseResponse):
	response: Optional["AddResponseModel"] = None


class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(BaseResponse):
	response: Optional["DeleteCommentResponseModel"] = None


class GetAlbumByIdResponse(BaseResponse):
	response: Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
	response: Optional["GetAlbumsResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
	response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetCategoriesNewResponse(BaseResponse):
	response: Optional["GetCategoriesNewResponseModel"] = None


class GetCategoriesResponse(BaseResponse):
	response: Optional["GetCategoriesResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetGroupOrdersResponse(BaseResponse):
	response: Optional["GetGroupOrdersResponseModel"] = None


class GetOrderByIdResponse(BaseResponse):
	response: Optional["GetOrderByIdResponseModel"] = None


class GetOrderItemsResponse(BaseResponse):
	response: Optional["GetOrderItemsResponseModel"] = None


class GetOrdersExtendedResponse(BaseResponse):
	response: Optional["GetOrdersExtendedResponseModel"] = None


class GetOrdersResponse(BaseResponse):
	response: Optional["GetOrdersResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
	response: Optional["RestoreCommentResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
	response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
	market_album_id: Optional[int] = None


class AddResponseModel(BaseResponse):
	market_item_id: Optional[int] = None


CreateCommentResponseModel = int


DeleteCommentResponseModel = Optional[BaseBoolInt]


class GetAlbumByIdResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketAlbum"]] = None


class GetAlbumsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketAlbum"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketItemFull"]] = None


class GetByIdResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketItem"]] = None


class GetCategoriesNewResponseModel(BaseResponse):
	items: Optional[List["MarketMarketCategoryTree"]] = None


class GetCategoriesResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketCategory"]] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallComment"]] = None


class GetGroupOrdersResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketOrder"]] = None


class GetOrderByIdResponseModel(BaseResponse):
	order: Optional["MarketOrder"] = None


class GetOrderItemsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketOrderItem"]] = None


class GetOrdersExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketOrder"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class GetOrdersResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketOrder"]] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketItemFull"]] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketItem"]] = None


RestoreCommentResponseModel = Optional[BaseBoolInt]


class SearchExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketItemFull"]] = None


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["MarketMarketItem"]] = None

AddAlbumResponse.update_forward_refs()
AddResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
DeleteCommentResponse.update_forward_refs()
GetAlbumByIdResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCategoriesNewResponse.update_forward_refs()
GetCategoriesResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetGroupOrdersResponse.update_forward_refs()
GetOrderByIdResponse.update_forward_refs()
GetOrderItemsResponse.update_forward_refs()
GetOrdersExtendedResponse.update_forward_refs()
GetOrdersResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()