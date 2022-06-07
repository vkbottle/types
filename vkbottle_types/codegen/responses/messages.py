import typing

from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsGroupFull,
    MessagesChat,
    MessagesChatFull,
    MessagesChatPreview,
    MessagesConversation,
    MessagesConversationWithMessage,
    MessagesGetConversationById,
    MessagesGetConversationByIdExtended,
    MessagesGetConversationMembers,
    MessagesHistoryAttachment,
    MessagesLastActivity,
    MessagesLongpollMessages,
    MessagesLongpollParams,
    MessagesMessage,
    MessagesMessagesArray,
    MessagesPinnedMessage,
    MessagesSendUserIdsResponseItem,
    UsersUser,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class CreateChatResponse(BaseResponse):
    response: int


class DeleteChatPhotoResponse(BaseResponse):
    response: "DeleteChatPhotoResponseModel"


class DeleteConversationResponse(BaseResponse):
    response: "DeleteConversationResponseModel"


class DeleteResponse(BaseResponse):
    response: typing.Dict[str, int]


class EditResponse(BaseResponse):
    response: BaseBoolInt


class GetByConversationMessageIdExtendedResponse(BaseResponse):
    response: "GetByConversationMessageIdExtendedResponseModel"


class GetByConversationMessageIdResponse(BaseResponse):
    response: "GetByConversationMessageIdResponseModel"


class GetByIdExtendedResponse(BaseResponse):
    response: "GetByIdExtendedResponseModel"


class GetByIdResponse(BaseResponse):
    response: "GetByIdResponseModel"


class GetChatPreviewResponse(BaseResponse):
    response: "GetChatPreviewResponseModel"


class GetChatChatIdsFieldsResponse(BaseResponse):
    response: typing.List["MessagesChatFull"]


class GetChatChatIdsResponse(BaseResponse):
    response: typing.List["MessagesChat"]


class GetChatFieldsResponse(BaseResponse):
    response: MessagesChatFull


class GetChatResponse(BaseResponse):
    response: MessagesChat


class GetConversationMembersResponse(BaseResponse):
    response: MessagesGetConversationMembers


class GetConversationsByIdExtendedResponse(BaseResponse):
    response: MessagesGetConversationByIdExtended


class GetConversationsByIdResponse(BaseResponse):
    response: MessagesGetConversationById


class GetConversationsResponse(BaseResponse):
    response: "GetConversationsResponseModel"


class GetHistoryAttachmentsResponse(BaseResponse):
    response: "GetHistoryAttachmentsResponseModel"


class GetHistoryExtendedResponse(BaseResponse):
    response: "GetHistoryExtendedResponseModel"


class GetHistoryResponse(BaseResponse):
    response: "GetHistoryResponseModel"


class GetImportantMessagesExtendedResponse(BaseResponse):
    response: "GetImportantMessagesExtendedResponseModel"


class GetImportantMessagesResponse(BaseResponse):
    response: "GetImportantMessagesResponseModel"


class GetIntentUsersResponse(BaseResponse):
    response: "GetIntentUsersResponseModel"


class GetInviteLinkResponse(BaseResponse):
    response: "GetInviteLinkResponseModel"


class GetLastActivityResponse(BaseResponse):
    response: MessagesLastActivity


class GetLongPollHistoryResponse(BaseResponse):
    response: "GetLongPollHistoryResponseModel"


class GetLongPollServerResponse(BaseResponse):
    response: MessagesLongpollParams


class IsMessagesFromGroupAllowedResponse(BaseResponse):
    response: "IsMessagesFromGroupAllowedResponseModel"


class JoinChatByInviteLinkResponse(BaseResponse):
    response: "JoinChatByInviteLinkResponseModel"


class MarkAsImportantResponse(BaseResponse):
    response: typing.List[int]


class PinResponse(BaseResponse):
    response: MessagesPinnedMessage


class SearchConversationsExtendedResponse(BaseResponse):
    response: "SearchConversationsExtendedResponseModel"


class SearchConversationsResponse(BaseResponse):
    response: "SearchConversationsResponseModel"


class SearchExtendedResponse(BaseResponse):
    response: "SearchExtendedResponseModel"


class SearchResponse(BaseResponse):
    response: "SearchResponseModel"


class SendResponse(BaseResponse):
    response: int


class SendUserIdsResponse(BaseResponse):
    response: typing.List["MessagesSendUserIdsResponseItem"]


class SetChatPhotoResponse(BaseResponse):
    response: "SetChatPhotoResponseModel"


class DeleteChatPhotoResponseModel(BaseResponse):
    message_id: typing.Optional[int] = None
    chat: typing.Optional["MessagesChat"] = None


class DeleteConversationResponseModel(BaseResponse):
    last_deleted_id: typing.Optional[int] = None


class GetByConversationMessageIdExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesMessage"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


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
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetConversationsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    unread_count: typing.Optional[int] = None
    items: typing.Optional[typing.List["MessagesConversationWithMessage"]] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetHistoryAttachmentsResponseModel(BaseResponse):
    items: typing.Optional[typing.List["MessagesHistoryAttachment"]] = None
    next_from: typing.Optional[str] = None
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


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
    profiles: typing.Optional[typing.List["UsersUserFull"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    conversations: typing.Optional[typing.List["MessagesConversation"]] = None


class GetImportantMessagesResponseModel(BaseResponse):
    messages: typing.Optional["MessagesMessagesArray"] = None
    profiles: typing.Optional[typing.List["UsersUser"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
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
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
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


class SetChatPhotoResponseModel(BaseResponse):
    message_id: typing.Optional[int] = None
    chat: typing.Optional["MessagesChat"] = None


__all__ = (
    "BaseBoolInt",
    "CreateChatResponse",
    "DeleteChatPhotoResponse",
    "DeleteChatPhotoResponseModel",
    "DeleteConversationResponse",
    "DeleteConversationResponseModel",
    "DeleteResponse",
    "EditResponse",
    "GetByConversationMessageIdExtendedResponse",
    "GetByConversationMessageIdExtendedResponseModel",
    "GetByConversationMessageIdResponse",
    "GetByConversationMessageIdResponseModel",
    "GetByIdExtendedResponse",
    "GetByIdExtendedResponseModel",
    "GetByIdResponse",
    "GetByIdResponseModel",
    "GetChatChatIdsFieldsResponse",
    "GetChatChatIdsResponse",
    "GetChatFieldsResponse",
    "GetChatPreviewResponse",
    "GetChatPreviewResponseModel",
    "GetChatResponse",
    "GetConversationMembersResponse",
    "GetConversationsByIdExtendedResponse",
    "GetConversationsByIdResponse",
    "GetConversationsResponse",
    "GetConversationsResponseModel",
    "GetHistoryAttachmentsResponse",
    "GetHistoryAttachmentsResponseModel",
    "GetHistoryExtendedResponse",
    "GetHistoryExtendedResponseModel",
    "GetHistoryResponse",
    "GetHistoryResponseModel",
    "GetImportantMessagesExtendedResponse",
    "GetImportantMessagesExtendedResponseModel",
    "GetImportantMessagesResponse",
    "GetImportantMessagesResponseModel",
    "GetIntentUsersResponse",
    "GetIntentUsersResponseModel",
    "GetInviteLinkResponse",
    "GetInviteLinkResponseModel",
    "GetLastActivityResponse",
    "GetLongPollHistoryResponse",
    "GetLongPollHistoryResponseModel",
    "GetLongPollServerResponse",
    "GroupsGroupFull",
    "IsMessagesFromGroupAllowedResponse",
    "IsMessagesFromGroupAllowedResponseModel",
    "JoinChatByInviteLinkResponse",
    "JoinChatByInviteLinkResponseModel",
    "MarkAsImportantResponse",
    "MessagesChat",
    "MessagesChatFull",
    "MessagesChatPreview",
    "MessagesConversation",
    "MessagesConversationWithMessage",
    "MessagesGetConversationById",
    "MessagesGetConversationByIdExtended",
    "MessagesGetConversationMembers",
    "MessagesHistoryAttachment",
    "MessagesLastActivity",
    "MessagesLongpollMessages",
    "MessagesLongpollParams",
    "MessagesMessage",
    "MessagesMessagesArray",
    "MessagesPinnedMessage",
    "MessagesSendUserIdsResponseItem",
    "PinResponse",
    "SearchConversationsExtendedResponse",
    "SearchConversationsExtendedResponseModel",
    "SearchConversationsResponse",
    "SearchConversationsResponseModel",
    "SearchExtendedResponse",
    "SearchExtendedResponseModel",
    "SearchResponse",
    "SearchResponseModel",
    "SendResponse",
    "SendUserIdsResponse",
    "SetChatPhotoResponse",
    "SetChatPhotoResponseModel",
    "UsersUser",
    "UsersUserFull",
)
