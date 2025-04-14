import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    GroupsGroupFull,
    MessagesChat,
    MessagesChatFull,
    MessagesChatPreview,
    MessagesConversation,
    MessagesConversationWithMessage,
    MessagesDeleteFullResponseItem,
    MessagesGetConversationById,
    MessagesGetConversationByIdExtended,
    MessagesGetConversationMembers,
    MessagesGetInviteLinkByOwnerResponseItem,
    MessagesHistoryAttachment,
    MessagesLastActivity,
    MessagesLongpollMessages,
    MessagesLongpollParams,
    MessagesMessage,
    MessagesMessagesArray,
    MessagesPinnedMessage,
    MessagesReactionAssetItem,
    MessagesReactionCounterResponseItem,
    MessagesReactionCountersResponseItem,
    MessagesReactionResponseItem,
    MessagesSendUserIdsResponseItem,
    UsersUser,
    UsersUserFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class MessagesAddChatUsersResponseModel(BaseModel):
    failed_peer_ids: typing.List[int] = Field()
    failed_phone_numbers: typing.List[str] = Field()
    invitees: typing.List[int] = Field()


class MessagesAddChatUsersResponse(BaseResponse):
    response: "MessagesAddChatUsersResponseModel" = Field()


class MessagesCreateChatWithPeerIdsResponseModel(BaseModel):
    chat_id: typing.Optional[int] = Field(
        default=None,
    )
    peer_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class MessagesCreateChatWithPeerIdsResponse(BaseResponse):
    response: "MessagesCreateChatWithPeerIdsResponseModel" = Field()


class MessagesDeleteChatPhotoResponseModel(BaseModel):
    message_id: typing.Optional[int] = Field(
        default=None,
    )
    chat: typing.Optional["MessagesChat"] = Field(
        default=None,
    )


class MessagesDeleteChatPhotoResponse(BaseResponse):
    response: "MessagesDeleteChatPhotoResponseModel" = Field()


class MessagesDeleteConversationResponseModel(BaseModel):
    last_deleted_id: int = Field()


class MessagesDeleteConversationResponse(BaseResponse):
    response: "MessagesDeleteConversationResponseModel" = Field()


class MessagesDeleteFullResponse(BaseResponse):
    response: typing.List["MessagesDeleteFullResponseItem"] = Field()


class MessagesGetByConversationMessageIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetByConversationMessageIdExtendedResponse(BaseResponse):
    response: "MessagesGetByConversationMessageIdExtendedResponseModel" = Field()


class MessagesGetByConversationMessageIdResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()


class MessagesGetByConversationMessageIdResponse(BaseResponse):
    response: "MessagesGetByConversationMessageIdResponseModel" = Field()


class MessagesGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetByIdExtendedResponse(BaseResponse):
    response: "MessagesGetByIdExtendedResponseModel" = Field()


class MessagesGetByIdResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()


class MessagesGetByIdResponse(BaseResponse):
    response: "MessagesGetByIdResponseModel" = Field()


class MessagesGetChatPreviewResponseModel(BaseModel):
    preview: "MessagesChatPreview" = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetChatPreviewResponse(BaseResponse):
    response: "MessagesGetChatPreviewResponseModel" = Field()


class MessagesGetChatChatIdsFieldsResponse(BaseResponse):
    response: typing.List["MessagesChatFull"] = Field()


class MessagesGetChatChatIdsResponse(BaseResponse):
    response: typing.List["MessagesChat"] = Field()


class MessagesGetChatFieldsResponse(BaseResponse):
    response: "MessagesChatFull" = Field()


class MessagesGetChatResponse(BaseResponse):
    response: "MessagesChat" = Field()


class MessagesGetConversationMembersResponse(BaseResponse):
    response: "MessagesGetConversationMembers" = Field()


class MessagesGetConversationsByIdExtendedResponse(BaseResponse):
    response: "MessagesGetConversationByIdExtended" = Field()


class MessagesGetConversationsByIdResponse(BaseResponse):
    response: "MessagesGetConversationById" = Field()


class MessagesGetConversationsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesConversationWithMessage"] = Field()
    unread_count: typing.Optional[int] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetConversationsResponse(BaseResponse):
    response: "MessagesGetConversationsResponseModel" = Field()


class MessagesGetHistoryAttachmentsResponseModel(BaseModel):
    items: typing.List["MessagesHistoryAttachment"] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetHistoryAttachmentsResponse(BaseResponse):
    response: "MessagesGetHistoryAttachmentsResponseModel" = Field()


class MessagesGetHistoryExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    conversations: typing.Optional[typing.List["MessagesConversation"]] = Field(
        default=None,
    )


class MessagesGetHistoryExtendedResponse(BaseResponse):
    response: "MessagesGetHistoryExtendedResponseModel" = Field()


class MessagesGetHistoryResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()


class MessagesGetHistoryResponse(BaseResponse):
    response: "MessagesGetHistoryResponseModel" = Field()


class MessagesGetImportantMessagesExtendedResponseModel(BaseModel):
    messages: "MessagesMessagesArray" = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    conversations: typing.Optional[typing.List["MessagesConversation"]] = Field(
        default=None,
    )


class MessagesGetImportantMessagesExtendedResponse(BaseResponse):
    response: "MessagesGetImportantMessagesExtendedResponseModel" = Field()


class MessagesGetImportantMessagesResponseModel(BaseModel):
    messages: "MessagesMessagesArray" = Field()
    profiles: typing.Optional[typing.List["UsersUser"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    conversations: typing.Optional[typing.List["MessagesConversation"]] = Field(
        default=None,
    )


class MessagesGetImportantMessagesResponse(BaseResponse):
    response: "MessagesGetImportantMessagesResponseModel" = Field()


class MessagesGetIntentUsersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )


class MessagesGetIntentUsersResponse(BaseResponse):
    response: "MessagesGetIntentUsersResponseModel" = Field()


class MessagesGetInviteLinkByOwnerResponseModel(BaseModel):
    items: typing.List["MessagesGetInviteLinkByOwnerResponseItem"] = Field()


class MessagesGetInviteLinkByOwnerResponse(BaseResponse):
    response: "MessagesGetInviteLinkByOwnerResponseModel" = Field()


class MessagesGetInviteLinkResponseModel(BaseModel):
    link: typing.Optional[str] = Field(
        default=None,
    )


class MessagesGetInviteLinkResponse(BaseResponse):
    response: "MessagesGetInviteLinkResponseModel" = Field()


class MessagesGetLastActivityResponse(BaseResponse):
    response: "MessagesLastActivity" = Field()


class MessagesGetLongPollHistoryResponseModel(BaseModel):
    history: typing.Optional[typing.List[typing.List[typing.Union["str", "int"]]]] = Field(
        default=None,
    )
    messages: typing.Optional["MessagesLongpollMessages"] = Field(
        default=None,
    )
    credentials: typing.Optional["MessagesLongpollParams"] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    chats: typing.Optional[typing.List["MessagesChat"]] = Field(
        default=None,
    )
    new_pts: typing.Optional[int] = Field(
        default=None,
    )
    from_pts: typing.Optional[int] = Field(
        default=None,
    )
    more: typing.Optional[bool] = Field(
        default=None,
    )
    conversations: typing.Optional[typing.List["MessagesConversation"]] = Field(
        default=None,
    )


class MessagesGetLongPollHistoryResponse(BaseResponse):
    response: "MessagesGetLongPollHistoryResponseModel" = Field()


class MessagesGetLongPollServerResponse(BaseResponse):
    response: "MessagesLongpollParams" = Field()


class MessagesGetMessagesReactionsResponseModel(BaseModel):
    items: typing.List["MessagesReactionCountersResponseItem"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetMessagesReactionsResponse(BaseResponse):
    response: "MessagesGetMessagesReactionsResponseModel" = Field()


class MessagesGetReactedPeersResponseModel(BaseModel):
    count: int = Field()
    reactions: typing.List["MessagesReactionResponseItem"] = Field()
    counters: typing.List["MessagesReactionCounterResponseItem"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesGetReactedPeersResponse(BaseResponse):
    response: "MessagesGetReactedPeersResponseModel" = Field()


class MessagesGetReactionsAssetsResponseModel(BaseModel):
    version: int = Field()
    assets: typing.List["MessagesReactionAssetItem"] = Field()
    reaction_ids: typing.List[int] = Field()
    override_assets: typing.Optional[typing.List["MessagesReactionAssetItem"]] = Field(
        default=None,
    )


class MessagesGetReactionsAssetsResponse(BaseResponse):
    response: "MessagesGetReactionsAssetsResponseModel" = Field()


class MessagesIsMessagesFromGroupAllowedResponseModel(BaseModel):
    is_allowed: typing.Optional[bool] = Field(
        default=None,
    )


class MessagesIsMessagesFromGroupAllowedResponse(BaseResponse):
    response: "MessagesIsMessagesFromGroupAllowedResponseModel" = Field()


class MessagesJoinChatByInviteLinkResponseModel(BaseModel):
    chat_id: typing.Optional[int] = Field(
        default=None,
    )


class MessagesJoinChatByInviteLinkResponse(BaseResponse):
    response: "MessagesJoinChatByInviteLinkResponseModel" = Field()


class MessagesMarkAsImportantDeprecatedResponse(BaseResponse):
    response: typing.List[int] = Field()


class MessagesPinResponse(BaseResponse):
    response: "MessagesPinnedMessage" = Field()


class MessagesSearchConversationsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesConversation"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )


class MessagesSearchConversationsExtendedResponse(BaseResponse):
    response: "MessagesSearchConversationsExtendedResponseModel" = Field()


class MessagesSearchConversationsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesConversation"] = Field()


class MessagesSearchConversationsResponse(BaseResponse):
    response: "MessagesSearchConversationsResponseModel" = Field()


class MessagesSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()
    profiles: typing.Optional[typing.List["UsersUserFull"]] = Field(
        default=None,
    )
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    conversations: typing.Optional[typing.List["MessagesConversation"]] = Field(
        default=None,
    )


class MessagesSearchExtendedResponse(BaseResponse):
    response: "MessagesSearchExtendedResponseModel" = Field()


class MessagesSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["MessagesMessage"] = Field()


class MessagesSearchResponse(BaseResponse):
    response: "MessagesSearchResponseModel" = Field()


class MessagesSendDeprecatedResponse(BaseResponse):
    response: int = Field()


class MessagesSendUserIdsResponse(BaseResponse):
    response: typing.List["MessagesSendUserIdsResponseItem"] = Field()


class MessagesSetChatPhotoResponseModel(BaseModel):
    message_id: typing.Optional[int] = Field(
        default=None,
    )
    chat: typing.Optional["MessagesChat"] = Field(
        default=None,
    )


class MessagesSetChatPhotoResponse(BaseResponse):
    response: "MessagesSetChatPhotoResponseModel" = Field()
