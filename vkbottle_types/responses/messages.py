import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
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
    response: typing.Optional["CreateChatResponseModel"] = None


class DeleteChatPhotoResponse(BaseResponse):
    response: typing.Optional["DeleteChatPhotoResponseModel"] = None


class DeleteConversationResponse(BaseResponse):
    response: typing.Optional["DeleteConversationResponseModel"] = None


class DeleteResponse(BaseResponse):
    response: typing.Optional["DeleteResponseModel"] = None


class EditResponse(BaseResponse):
    response: typing.Optional["EditResponseModel"] = None


class GetByConversationMessageIdResponse(BaseResponse):
    response: typing.Optional["GetByConversationMessageIdResponseModel"] = None


class GetByIdExtendedResponse(BaseResponse):
    response: typing.Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetChatPreviewResponse(BaseResponse):
    response: typing.Optional["GetChatPreviewResponseModel"] = None


class GetChatChatIdsFieldsResponse(BaseResponse):
    response: typing.Optional["GetChatChatIdsFieldsResponseModel"] = None


class GetChatChatIdsResponse(BaseResponse):
    response: typing.Optional["GetChatChatIdsResponseModel"] = None


class GetChatFieldsResponse(BaseResponse):
    response: typing.Optional["GetChatFieldsResponseModel"] = None


class GetChatResponse(BaseResponse):
    response: typing.Optional["GetChatResponseModel"] = None


class GetConversationMembersResponse(BaseResponse):
    response: typing.Optional["GetConversationMembersResponseModel"] = None


class GetConversationsByIdExtendedResponse(BaseResponse):
    response: typing.Optional["GetConversationsByIdExtendedResponseModel"] = None


class GetConversationsByIdResponse(BaseResponse):
    response: typing.Optional["GetConversationsByIdResponseModel"] = None


class GetConversationsResponse(BaseResponse):
    response: typing.Optional["GetConversationsResponseModel"] = None


class GetHistoryAttachmentsResponse(BaseResponse):
    response: typing.Optional["GetHistoryAttachmentsResponseModel"] = None


class GetHistoryExtendedResponse(BaseResponse):
    response: typing.Optional["GetHistoryExtendedResponseModel"] = None


class GetHistoryResponse(BaseResponse):
    response: typing.Optional["GetHistoryResponseModel"] = None


class GetImportantMessagesExtendedResponse(BaseResponse):
    response: typing.Optional["GetImportantMessagesExtendedResponseModel"] = None


class GetImportantMessagesResponse(BaseResponse):
    response: typing.Optional["GetImportantMessagesResponseModel"] = None


class GetIntentUsersResponse(BaseResponse):
    response: typing.Optional["GetIntentUsersResponseModel"] = None


class GetInviteLinkResponse(BaseResponse):
    response: typing.Optional["GetInviteLinkResponseModel"] = None


class GetLastActivityResponse(BaseResponse):
    response: typing.Optional["GetLastActivityResponseModel"] = None


class GetLongPollHistoryResponse(BaseResponse):
    response: typing.Optional["GetLongPollHistoryResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
    response: typing.Optional["GetLongPollServerResponseModel"] = None


class IsMessagesFromGroupAllowedResponse(BaseResponse):
    response: typing.Optional["IsMessagesFromGroupAllowedResponseModel"] = None


class JoinChatByInviteLinkResponse(BaseResponse):
    response: typing.Optional["JoinChatByInviteLinkResponseModel"] = None


class MarkAsImportantResponse(BaseResponse):
    response: typing.Optional["MarkAsImportantResponseModel"] = None


class PinResponse(BaseResponse):
    response: typing.Optional["PinResponseModel"] = None


class SearchConversationsExtendedResponse(BaseResponse):
    response: typing.Optional["SearchConversationsExtendedResponseModel"] = None


class SearchConversationsResponse(BaseResponse):
    response: typing.Optional["SearchConversationsResponseModel"] = None


class SearchExtendedResponse(BaseResponse):
    response: typing.Optional["SearchExtendedResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


class SendResponse(BaseResponse):
    response: typing.Optional["SendResponseModel"] = None


class SendUserIdsResponse(BaseResponse):
    response: typing.Optional["SendUserIdsResponseModel"] = None


class SetChatPhotoResponse(BaseResponse):
    response: typing.Optional["SetChatPhotoResponseModel"] = None


CreateChatResponseModel = int


class DeleteChatPhotoResponseModel(BaseResponse):
    message_id: typing.Optional[int] = None
    chat: typing.Optional["MessagesChat"] = None


class DeleteConversationResponseModel(BaseResponse):
    last_deleted_id: typing.Optional[int] = None


DeleteResponseModel = typing.Dict[str, int]


EditResponseModel = BaseBoolInt


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


GetChatChatIdsFieldsResponseModel = typing.List[MessagesChatFull]


GetChatChatIdsResponseModel = typing.List[MessagesChat]


GetChatFieldsResponseModel = MessagesChatFull


GetChatResponseModel = MessagesChat


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


GetLastActivityResponseModel = MessagesLastActivity


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


GetLongPollServerResponseModel = MessagesLongpollParams


class IsMessagesFromGroupAllowedResponseModel(BaseResponse):
    is_allowed: typing.Optional["BaseBoolInt"] = None


class JoinChatByInviteLinkResponseModel(BaseResponse):
    chat_id: typing.Optional[int] = None


MarkAsImportantResponseModel = typing.List[int]


PinResponseModel = MessagesPinnedMessage


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


SendResponseModel = int


SendUserIdsResponseModel = typing.List["typing.Any"]


class SetChatPhotoResponseModel(BaseResponse):
    message_id: typing.Optional[int] = None
    chat: typing.Optional["MessagesChat"] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
