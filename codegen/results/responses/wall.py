from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class EditResponse(BaseResponse):
	response: Optional["EditResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
	response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdLegacyResponse(BaseResponse):
	response: Optional["GetByIdLegacyResponseModel"] = None


class GetByIdResponse(BaseResponse):
	response: Optional["GetByIdResponseModel"] = None


class GetCommentExtendedResponse(BaseResponse):
	response: Optional["GetCommentExtendedResponseModel"] = None


class GetCommentResponse(BaseResponse):
	response: Optional["GetCommentResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
	response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetRepostsResponse(BaseResponse):
	response: Optional["GetRepostsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class PostAdsStealthResponse(BaseResponse):
	response: Optional["PostAdsStealthResponseModel"] = None


class PostResponse(BaseResponse):
	response: Optional["PostResponseModel"] = None


class RepostResponse(BaseResponse):
	response: Optional["RepostResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
	response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class CreateCommentResponseModel(BaseResponse):
	comment_id: Optional[int] = None


class EditResponseModel(BaseResponse):
	post_id: Optional[int] = None


class GetByIdExtendedResponseModel(BaseResponse):
	items: Optional[List["WallWallpostFull"]] = None
	profiles: Optional[List["UsersUserFull"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


GetByIdLegacyResponseModel = List[WallWallpostFull]


class GetByIdResponseModel(BaseResponse):
	items: Optional[List["WallWallpostFull"]] = None


class GetCommentExtendedResponseModel(BaseResponse):
	items: Optional[List["WallWallComment"]] = None
	profiles: Optional[List["UsersUser"]] = None
	groups: Optional[List["GroupsGroup"]] = None


class GetCommentResponseModel(BaseResponse):
	items: Optional[List["WallWallComment"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallComment"]] = None
	show_reply_button: Optional[bool] = None
	can_post: Optional[bool] = None
	groups_can_post: Optional[bool] = None
	current_level_count: Optional[int] = None
	profiles: Optional[List["UsersUser"]] = None
	groups: Optional[List["GroupsGroup"]] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallComment"]] = None
	can_post: Optional[bool] = None
	groups_can_post: Optional[bool] = None
	current_level_count: Optional[int] = None


class GetRepostsResponseModel(BaseResponse):
	items: Optional[List["WallWallpostFull"]] = None
	profiles: Optional[List["UsersUser"]] = None
	groups: Optional[List["GroupsGroup"]] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallpostFull"]] = None
	profiles: Optional[List["UsersUserFull"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallpostFull"]] = None


class PostAdsStealthResponseModel(BaseResponse):
	post_id: Optional[int] = None


class PostResponseModel(BaseResponse):
	post_id: Optional[int] = None


class RepostResponseModel(BaseResponse):
	success: Optional[int] = None
	post_id: Optional[int] = None
	reposts_count: Optional[int] = None
	wall_repost_count: Optional[int] = None
	mail_repost_count: Optional[int] = None
	likes_count: Optional[int] = None


class SearchExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallpostFull"]] = None
	profiles: Optional[List["UsersUserFull"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallpostFull"]] = None

CreateCommentResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdLegacyResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentExtendedResponse.update_forward_refs()
GetCommentResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetRepostsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
PostAdsStealthResponse.update_forward_refs()
PostResponse.update_forward_refs()
RepostResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()