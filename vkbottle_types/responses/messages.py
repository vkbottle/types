from .base_response import BaseResponse
from vkbottle_types.objects import users, groups, message, messages, base
from typing import Optional, Any, List, Union
import typing


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


class SendUserIdsResponse(BaseResponse):
    response: Optional["SendUserIdsResponseModel"] = None


class SetChatPhotoResponse(BaseResponse):
    response: Optional["SetChatPhotoResponseModel"] = None


CreateChatResponseModel = int


class DeleteChatPhotoResponseModel(BaseResponse):
    message_id: Optional[int] = None
    chat: Optional["messages.Chat"] = None


class DeleteConversationResponseModel(BaseResponse):
    last_deleted_id: Optional[int] = None


DeleteResponseModel = typing.Dict[str, int]


EditResponseModel = Optional["base.BoolInt"]


class GetByConversationMessageIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Message"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Message"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Message"]] = None


class GetChatPreviewResponseModel(BaseResponse):
    preview: Optional["message.ChatPreview"] = None
    profiles: Optional[List["users.UserFull"]] = None


GetChatChatIdsFieldsResponseModel = List["messages.ChatFull"]


GetChatChatIdsResponseModel = List["messages.Chat"]


GetChatFieldsResponseModel = Optional["messages.ChatFull"]


GetChatResponseModel = Optional["messages.Chat"]


class GetConversationMembersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.ConversationMember"]] = None
    chat_restrictions: Optional["messages.ChatRestrictions"] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetConversationsByIdExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Conversation"]] = None
    profiles: Optional[List["users.User"]] = None


class GetConversationsByIdResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Conversation"]] = None


class GetConversationsResponseModel(BaseResponse):
    count: Optional[int] = None
    unread_count: Optional[int] = None
    items: Optional[List["messages.ConversationWithMessage"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetHistoryAttachmentsResponseModel(BaseResponse):
    items: Optional[List["messages.HistoryAttachment"]] = None
    next_from: Optional[str] = None


class GetHistoryResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Message"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetInviteLinkResponseModel(BaseResponse):
    link: Optional[str] = None


GetLastActivityResponseModel = Optional["messages.LastActivity"]


class GetLongPollHistoryResponseModel(BaseResponse):
    history: Optional[List[List[int]]] = None
    groups: Optional[List["groups.Group"]] = None
    messages: Optional["messages.LongpollMessages"] = None
    profiles: Optional[List["users.UserFull"]] = None
    chats: Optional[List["messages.Chat"]] = None
    new_pts: Optional[int] = None
    more: Optional[bool] = None
    conversations: Optional[List["messages.Conversation"]] = None


GetLongPollServerResponseModel = Optional["messages.LongpollParams"]


class IsMessagesFromGroupAllowedResponseModel(BaseResponse):
    is_allowed: Optional["base.BoolInt"] = None


class JoinChatByInviteLinkResponseModel(BaseResponse):
    chat_id: Optional[int] = None


MarkAsImportantResponseModel = List[int]


PinResponseModel = Optional["messages.PinnedMessage"]


class SearchConversationsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Conversation"]] = None
    profiles: Optional[List["users.UserFull"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["messages.Message"]] = None


SendResponseModel = int


class SendUserIdsResponseModel(BaseResponse):
    peer_id: Optional[int] = None
    message_id: Optional[int] = None
    error: Optional["base.MessageError"] = None


class SetChatPhotoResponseModel(BaseResponse):
    message_id: Optional[int] = None
    chat: Optional["messages.Chat"] = None
