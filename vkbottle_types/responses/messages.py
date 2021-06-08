import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    BaseMessageError,
    GroupsGroup,
    GroupsGroupFull,
    MessagesChat,
    MessagesChatFull,
    MessagesChatPreview,
    MessagesChatRestrictions,
    MessagesConversation,
    MessagesConversationMember,
    MessagesConversationWithMessage,
    MessagesHistoryAttachment,
    MessagesLastActivity,
    MessagesLongpollMessages,
    MessagesLongpollParams,
    MessagesMessage,
    MessagesMessagesArray,
    MessagesPinnedMessage,
    UsersUser,
    UsersUserFull
)


class CreateChatResponse(BaseResponse):
    response: int = None


class DeleteChatPhotoResponse(BaseResponse):
    response: "DeleteChatPhotoResponseModel" = None


class DeleteConversationResponse(BaseResponse):
    response: "DeleteConversationResponseModel" = None


class DeleteResponse(BaseResponse):
    response: typing.Dict[str, int] = None


class EditResponse(BaseResponse):
    response: BaseBoolInt = None


class GetByConversationMessageIdResponse(BaseResponse):
    response: "GetByConversationMessageIdResponseModel" = None


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel" = None


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel" = None


class GetChatPreviewResponse(BaseResponse):
    response: "GetChatPreviewResponseModel" = None


class GetChatChatIdsFieldsResponse(BaseResponse):
    response: typing.List["MessagesChatFull"] = None


class GetChatChatIdsResponse(BaseResponse):
    response: typing.List["MessagesChat"] = None


class GetChatFieldsResponse(BaseResponse):
    response: MessagesChatFull = None


class GetChatResponse(BaseResponse):
    response: MessagesChat = None


class GetConversationMembersResponse(BaseResponse):
    response: "GetConversationMembersResponseModel" = None


class GetConversationsByIdExtendedResponse(BaseResponse):
    response: "GetConversationsByIdExtendedResponseModel" = None


class GetConversationsByIdResponse(BaseResponse):
    response: "GetConversationsByIdResponseModel" = None


class GetConversationsResponse(BaseResponse):
    response: "GetConversationsResponseModel" = None


class GetHistoryAttachmentsResponse(BaseResponse):
    response: "GetHistoryAttachmentsResponseModel" = None


class GetHistoryExtendedResponse(BaseResponse):
    response: "GetHistoryExtendedResponseModel" = None


class GetHistoryResponse(BaseResponse):
    response: "GetHistoryResponseModel" = None


class GetImportantMessagesExtendedResponse(BaseResponse):
    response: "GetImportantMessagesExtendedResponseModel" = None


class GetImportantMessagesResponse(BaseResponse):
    response: "GetImportantMessagesResponseModel" = None


class GetIntentUsersResponse(BaseResponse):
    response: "GetIntentUsersResponseModel" = None


class GetInviteLinkResponse(BaseResponse):
    response: "GetInviteLinkResponseModel" = None


class GetLastActivityResponse(BaseResponse):
    response: MessagesLastActivity = None


class GetLongPollHistoryResponse(BaseResponse):
    response: "GetLongPollHistoryResponseModel" = None


class GetLongPollServerResponse(BaseResponse):
    response: MessagesLongpollParams = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
    response: "IsMessagesFromGroupAllowedResponseModel" = None


class JoinChatByInviteLinkResponse(BaseResponse):
    response: "JoinChatByInviteLinkResponseModel" = None


class MarkAsImportantResponse(BaseResponse):
    response: typing.List[int] = None


class PinResponse(BaseResponse):
    response: MessagesPinnedMessage = None


class SearchConversationsExtendedResponse(BaseResponse):
    response: "SearchConversationsExtendedResponseModel" = None


class SearchConversationsResponse(BaseResponse):
    response: "SearchConversationsResponseModel" = None


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel" = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class SendResponse(BaseResponse):
    response: int = None


class SendUserIdsResponse(BaseResponse):
    response: typing.List["SendUserIdsResponseModel"] = None


class SetChatPhotoResponse(BaseResponse):
    response: "SetChatPhotoResponseModel" = None


class DeleteChatPhotoResponseModel(BaseResponse):
    message_id: typing.Optional[int] = None
    chat: typing.Optional["MessagesChat"] = None


class DeleteConversationResponseModel(BaseResponse):
    last_deleted_id: typing.Optional[int] = None


class GetByConversationMessageIdResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None


class GetByIdExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetByIdResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None


class GetChatPreviewResponseModel(BaseResponse):
    preview: typing.Optional["MessagesChatPreview"] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None


class GetConversationMembersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversationMember"]] = None
    chat_restrictions: typing.Optional["MessagesChatRestrictions"] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetConversationsByIdExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversation"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetConversationsByIdResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversation"]] = None


class GetConversationsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    unread_count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversationWithMessage"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetHistoryAttachmentsResponseModel(BaseResponse):
    items: typing.Optional[typing.List["MessagesHistoryAttachment"]] = None
    next_from: typing.Optional[str] = None


class GetHistoryExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    conversations: typing.Optional[typing.List["MessagesConversation"]] = None


class GetHistoryResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None


class GetImportantMessagesExtendedResponseModel(BaseResponse):
    messages: typing.Optional["MessagesMessagesArray"] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    conversations: typing.Optional[typing.List["MessagesConversation"]] = None


class GetImportantMessagesResponseModel(BaseResponse):
    messages: typing.Optional["MessagesMessagesArray"] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    conversations: typing.Optional[typing.List["MessagesConversation"]] = None


class GetIntentUsersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None


class GetInviteLinkResponseModel(BaseResponse):
    link: typing.Optional[str] = None


class GetLongPollHistoryResponseModel(BaseResponse):
    history: typing.Optional[typing.List["list"]] = None
    messages: typing.Optional["MessagesLongpollMessages"] = None
    credentials: typing.Optional["MessagesLongpollParams"] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroup"]] = None
    chats: typing.Optional[typing.List["MessagesChat"]] = None
    new_pts: typing.Optional[int] = None
    from_pts: typing.Optional[int] = None
    more: typing.Optional[bool] = None
    conversations: typing.Optional[typing.List["MessagesConversation"]] = None


class IsMessagesFromGroupAllowedResponseModel(BaseResponse):
    is_allowed: typing.Optional["BaseBoolInt"] = None


class JoinChatByInviteLinkResponseModel(BaseResponse):
    chat_id: typing.Optional[int] = None


class SearchConversationsExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversation"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class SearchConversationsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversation"]] = None


class SearchExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    conversations: typing.Optional[typing.List["MessagesConversation"]] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None


class SendUserIdsResponseModel(BaseResponse):
    peer_id: typing.Optional[int] = None
    message_id: typing.Optional[int] = None
    conversation_message_id: typing.Optional[int] = None
    error: typing.Optional["BaseMessageError"] = None


class SetChatPhotoResponseModel(BaseResponse):
    message_id: typing.Optional[int] = None
    chat: typing.Optional["MessagesChat"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
