import typing
from typing import Optional

from vkbottle_types.objects import message, messages, groups, base, users
from .base_response import BaseResponse


class CreateChatResponse(BaseResponse):
    response: Optional[int] = None


class DeleteChatPhotoResponse(BaseResponse):
    response: Optional["DeleteChatPhotoResponseModel"] = None


class DeleteConversationResponse(BaseResponse):
    response: Optional["DeleteConversationResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
    response: Optional[typing.List["base.BoolInt"]] = None


class GetByConversationMessageIdResponse(BaseResponse):
    response: Optional["GetByConversationMessageIdResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetChatPreviewResponse(BaseResponse):
    response: Optional["GetChatPreviewResponseModel"] = None


class GetChatChatIdsFieldsResponse(BaseResponse):
    response: Optional[typing.List["messages.ChatFull"]] = None


class GetChatChatIdsResponse(BaseResponse):
    response: Optional[typing.List["messages.Chat"]] = None


class GetChatFieldsResponse(BaseResponse):
    response: Optional[typing.List["messages.ChatFull"]] = None


class GetChatResponse(BaseResponse):
    response: Optional[typing.List["messages.Chat"]] = None


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
    response: Optional[typing.List["messages.LastActivity"]] = None


class GetLongPollHistoryResponse(BaseResponse):
    response: Optional["GetLongPollHistoryResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
    response: Optional[typing.List["messages.LongpollParams"]] = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
    response: Optional["IsMessagesFromGroupAllowedResponseModel"] = None


class JoinChatByInviteLinkResponse(BaseResponse):
    response: Optional["JoinChatByInviteLinkResponseModel"] = None


class MarkAsImportantResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class PinResponse(BaseResponse):
    response: Optional[typing.List["messages.PinnedMessage"]] = None


class SearchConversationsResponse(BaseResponse):
    response: Optional["SearchConversationsResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class SendResponse(BaseResponse):
    response: Optional[int] = None


class SendUserIdsItem(BaseResponse):
    peer_id: Optional[int] = None
    message_id: Optional[int] = None
    error: Optional[base.MessageError] = None


class SendUserIdsResponse(BaseResponse):
    response: Optional[typing.List[SendUserIdsItem]] = None


class SetChatPhotoResponse(BaseResponse):
    response: Optional["SetChatPhotoResponseModel"] = None


class DeleteChatPhotoResponseModel(BaseResponse):
    message_id: Optional[int] = None
    chat: Optional[typing.List["messages.Chat"]] = None


class DeleteConversationResponseModel(BaseResponse):
    last_deleted_id: Optional[int] = None


class GetByConversationMessageIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Message"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Message"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Message"]] = None


class GetChatPreviewResponseModel(BaseResponse):
    preview: Optional[typing.List["message.ChatPreview"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None


class GetConversationMembersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.ConversationMember"]] = None
    chat_restrictions: Optional[typing.List["messages.ChatRestrictions"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetConversationsByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Conversation"]] = None
    profiles: Optional[typing.List["users.User"]] = None


class GetConversationsByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Conversation"]] = None


class GetConversationsResponseModel(BaseResponse):
    count: Optional[int] = None
    unread_count: Optional[int] = None
    items: Optional[typing.List["messages.ConversationWithMessage"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetHistoryAttachmentsResponseModel(BaseResponse):
    items: Optional[typing.List["messages.HistoryAttachment"]] = None
    next_from: Optional[str] = None


class GetHistoryResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Message"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetInviteLinkResponseModel(BaseResponse):
    link: Optional[str] = None


class GetLongPollHistoryResponseModel(BaseResponse):
    groups: Optional[typing.List["groups.Group"]] = None
    messages: Optional[typing.List["messages.LongpollMessages"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    chats: Optional[typing.List["messages.Chat"]] = None
    new_pts: Optional[int] = None
    more: Optional[bool] = None
    conversations: Optional[typing.List["messages.Conversation"]] = None
    history: Optional[typing.List[typing.List[int]]] = None


class IsMessagesFromGroupAllowedResponseModel(BaseResponse):
    is_allowed: Optional[typing.List["base.BoolInt"]] = None


class JoinChatByInviteLinkResponseModel(BaseResponse):
    chat_id: Optional[int] = None


class SearchConversationsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Conversation"]] = None
    profiles: Optional[typing.List["users.UserFull"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["messages.Message"]] = None


class SetChatPhotoResponseModel(BaseResponse):
    message_id: Optional[int] = None
    chat: Optional[typing.List["messages.Chat"]] = None
