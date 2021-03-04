from typing import Optional, List, Union
from vkbottle_types.objects import GroupsGroupFull, GroupsGroup, MessagesMessage, MessagesPinnedMessage, MessagesHistoryAttachment, MessagesChatFull, MessageChatPreview, MessagesLongpollParams, MessagesLastActivity, MessagesConversation, BaseMessageError, MessagesConversationWithMessage, BaseBoolInt, MessagesChatRestrictions, MessagesChat, UsersUser, UsersUserFull, MessagesLongpollMessages, MessagesConversationMember
from .base_response import BaseResponse


class AddAlbumResponse(BaseResponse):
	response: Optional["AddAlbumResponseModel"] = None


class CreateCommentResponse(BaseResponse):
	response: Optional["CreateCommentResponseModel"] = None


class GetAlbumByIdResponse(BaseResponse):
	response: Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsByVideoExtendedResponse(BaseResponse):
	response: Optional["GetAlbumsByVideoExtendedResponseModel"] = None


class GetAlbumsByVideoResponse(BaseResponse):
	response: Optional["GetAlbumsByVideoResponseModel"] = None


class GetAlbumsExtendedResponse(BaseResponse):
	response: Optional["GetAlbumsExtendedResponseModel"] = None


class GetAlbumsResponse(BaseResponse):
	response: Optional["GetAlbumsResponseModel"] = None


class GetCommentsExtendedResponse(BaseResponse):
	response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(BaseResponse):
	response: Optional["GetCommentsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
	response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
	response: Optional["GetResponseModel"] = None


class RestoreCommentResponse(BaseResponse):
	response: Optional["RestoreCommentResponseModel"] = None


class SaveResponse(BaseResponse):
	response: Optional["SaveResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
	response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
	response: Optional["SearchResponseModel"] = None


class UploadResponse(BaseResponse):
	response: Optional["UploadResponseModel"] = None


class AddAlbumResponseModel(BaseResponse):
	album_id: Optional[int] = None


CreateCommentResponseModel = int


GetAlbumByIdResponseModel = Optional[VideoVideoAlbumFull]


class GetAlbumsByVideoExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideoAlbumFull"]] = None


GetAlbumsByVideoResponseModel = List[: Optional[List[int]]]


class GetAlbumsExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideoAlbumFull"]] = None


class GetAlbumsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideoAlbumFull"]] = None


class GetCommentsExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallComment"]] = None
	profiles: Optional[List["UsersUserMin"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["WallWallComment"]] = None


class GetExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideoFull"]] = None
	profiles: Optional[List["UsersUserMin"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class GetResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideoFull"]] = None


RestoreCommentResponseModel = Optional[BaseBoolInt]


SaveResponseModel = Optional[VideoSaveResult]


class SearchExtendedResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideoFull"]] = None
	profiles: Optional[List["UsersUserMin"]] = None
	groups: Optional[List["GroupsGroupFull"]] = None


class SearchResponseModel(BaseResponse):
	count: Optional[int] = None
	items: Optional[List["VideoVideo"]] = None


class UploadResponseModel(BaseResponse):
	size: Optional[int] = None
	video_id: Optional[int] = None

AddAlbumResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetAlbumByIdResponse.update_forward_refs()
GetAlbumsByVideoExtendedResponse.update_forward_refs()
GetAlbumsByVideoResponse.update_forward_refs()
GetAlbumsExtendedResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()
UploadResponse.update_forward_refs()