import typing
from typing import Optional, List, Union

from vkbottle_types.objects import (
    GroupsGroupFull,
    GroupsGroup,
    MessagesMessage,
    MessagesPinnedMessage,
    MessagesHistoryAttachment,
    MessagesChatFull,
    MessageChatPreview,
    MessagesLongpollParams,
    MessagesLastActivity,
    MessagesConversation,
    BaseMessageError,
    MessagesConversationWithMessage,
    BaseBoolInt,
    MessagesChatRestrictions,
    MessagesChat,
    UsersUser,
    UsersUserFull,
    MessagesLongpollMessages,
    MessagesConversationMember,
)
from .base_response import BaseResponse


class CreateChatResponse(BaseResponse):
    response: Optional["CreateChatResponseModel"] = None


class DeleteChatPhotoResponse(BaseResponse):
    response: Optional["DeleteChatPhotoResponseModel"] = None


class DeleteConversationResponse(BaseResponse):
    response: Optional["DeleteConversationResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
    response: Optional["EditResponseModel"] = None


class GetByConversationMessageIdResponse(BaseResponse):
    response: Optional["GetByConversationMessageIdResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetChatPreviewResponse(BaseResponse):
    response: Optional["GetChatPreviewResponseModel"] = None


class GetChatChatIdsFieldsResponse(BaseResponse):
    response: Optional["GetChatChatIdsFieldsResponseModel"] = None


class GetChatChatIdsResponse(BaseResponse):
    response: Optional["GetChatChatIdsResponseModel"] = None


class GetChatFieldsResponse(BaseResponse):
    response: Optional["GetChatFieldsResponseModel"] = None


class GetChatResponse(BaseResponse):
    response: Optional["GetChatResponseModel"] = None


class GetConversationMembersResponse(BaseResponse):
    response: Optional["GetConversationMembersResponseModel"] = None


class GetConversationsByIdExtendedResponse(BaseResponse):
    response: Optional["GetConversationsByIdExtendedResponseModel"] = None


class GetConversationsByIdResponse(BaseResponse):
    response: Optional["GetConversationsByIdResponseModel"] = None


class GetConversationsResponse(BaseResponse):
    response: Optional["GetConversationsResponseModel"] = None


class GetHistoryAttachmentsResponse(BaseResponse):
    response: Optional["GetHistoryAttachmentsResponseModel"] = None


class GetHistoryResponse(BaseResponse):
    response: Optional["GetHistoryResponseModel"] = None


class GetInviteLinkResponse(BaseResponse):
    response: Optional["GetInviteLinkResponseModel"] = None


class GetLastActivityResponse(BaseResponse):
    response: Optional["GetLastActivityResponseModel"] = None


class GetLongPollHistoryResponse(BaseResponse):
    response: Optional["GetLongPollHistoryResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
    response: Optional["GetLongPollServerResponseModel"] = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
    response: Optional["IsMessagesFromGroupAllowedResponseModel"] = None


class JoinChatByInviteLinkResponse(BaseResponse):
    response: Optional["JoinChatByInviteLinkResponseModel"] = None


class MarkAsImportantResponse(BaseResponse):
    response: Optional["MarkAsImportantResponseModel"] = None


class PinResponse(BaseResponse):
    response: Optional["PinResponseModel"] = None


class SearchConversationsResponse(BaseResponse):
    response: Optional["SearchConversationsResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class SendResponse(BaseResponse):
    response: Optional["SendResponseModel"] = None


class SendPeerIdsResponse(BaseResponse):
    response: Optional[List["SendResponsePeerIdsModel"]] = None


class SendUserIdsResponse(BaseResponse):
    response: Optional["SendUserIdsResponseModel"] = None


class SetChatPhotoResponse(BaseResponse):
    response: Optional["SetChatPhotoResponseModel"] = None


CreateChatResponseModel = int


class DeleteChatPhotoResponseModel(BaseResponse):
    message_id: Optional[int] = None
    chat: Optional["MessagesChat"] = None


class DeleteConversationResponseModel(BaseResponse):
    last_deleted_id: Optional[int] = None


DeleteResponseModel = typing.Dict[str, int]

EditResponseModel = Optional[BaseBoolInt]


class GetByConversationMessageIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class GetChatPreviewResponseModel(BaseResponse):
    preview: Optional["MessageChatPreview"] = None
    profiles: Optional[List["UsersUserFull"]] = None


GetChatChatIdsFieldsResponseModel = List[MessagesChatFull]

GetChatChatIdsResponseModel = List[MessagesChat]

GetChatFieldsResponseModel = Optional[MessagesChatFull]

GetChatResponseModel = Optional[MessagesChat]


class GetConversationMembersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesConversationMember"]] = None
    chat_restrictions: Optional["MessagesChatRestrictions"] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetConversationsByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesConversation"]] = None
    profiles: Optional[List["UsersUser"]] = None


class GetConversationsByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesConversation"]] = None


class GetConversationsResponseModel(BaseResponse):
    count: Optional[int] = None
    unread_count: Optional[int] = None
    items: Optional[List["MessagesConversationWithMessage"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetHistoryAttachmentsResponseModel(BaseResponse):
    items: Optional[List["MessagesHistoryAttachment"]] = None
    next_from: Optional[str] = None


class GetHistoryResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetInviteLinkResponseModel(BaseResponse):
    link: Optional[str] = None


GetLastActivityResponseModel = Optional[MessagesLastActivity]


class GetLongPollHistoryResponseModel(BaseResponse):
    history: Optional[List[List[int]]] = None
    groups: Optional[List["GroupsGroup"]] = None
    messages: Optional["MessagesLongpollMessages"] = None
    profiles: Optional[List["UsersUserFull"]] = None
    chats: Optional[List["MessagesChat"]] = None
    new_pts: Optional[int] = None
    more: Optional[bool] = None
    conversations: Optional[List["MessagesConversation"]] = None


GetLongPollServerResponseModel = Optional[MessagesLongpollParams]


class IsMessagesFromGroupAllowedResponseModel(BaseResponse):
    is_allowed: Optional["BaseBoolInt"] = None


class JoinChatByInviteLinkResponseModel(BaseResponse):
    chat_id: Optional[int] = None


MarkAsImportantResponseModel = List[int]

PinResponseModel = Optional[MessagesPinnedMessage]


class SearchConversationsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesConversation"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


SendResponseModel = Union[int, SendUserIdsResponse]


class SendResponsePeerIdsModel(BaseResponse):
    peer_id: Optional[int] = None
    message_id: Optional[int] = None
    conversation_message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None


class SendUserIdsResponseModel(BaseResponse):
    peer_id: Optional[int] = None
    message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None


class SetChatPhotoResponseModel(BaseResponse):
    message_id: Optional[int] = None
    chat: Optional["MessagesChat"] = None


CreateChatResponse.update_forward_refs()
DeleteChatPhotoResponse.update_forward_refs()
DeleteConversationResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByConversationMessageIdResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetChatPreviewResponse.update_forward_refs()
GetChatChatIdsFieldsResponse.update_forward_refs()
GetChatChatIdsResponse.update_forward_refs()
GetChatFieldsResponse.update_forward_refs()
GetChatResponse.update_forward_refs()
GetConversationMembersResponse.update_forward_refs()
GetConversationsByIdExtendedResponse.update_forward_refs()
GetConversationsByIdResponse.update_forward_refs()
GetConversationsResponse.update_forward_refs()
GetHistoryAttachmentsResponse.update_forward_refs()
GetHistoryResponse.update_forward_refs()
GetInviteLinkResponse.update_forward_refs()
GetLastActivityResponse.update_forward_refs()
GetLongPollHistoryResponse.update_forward_refs()
GetLongPollServerResponse.update_forward_refs()
IsMessagesFromGroupAllowedResponse.update_forward_refs()
JoinChatByInviteLinkResponse.update_forward_refs()
MarkAsImportantResponse.update_forward_refs()
PinResponse.update_forward_refs()
SearchConversationsResponse.update_forward_refs()
SearchResponse.update_forward_refs()
SendResponse.update_forward_refs()
SendPeerIdsResponse.update_forward_refs()
SendUserIdsResponse.update_forward_refs()
SetChatPhotoResponse.update_forward_refs()
