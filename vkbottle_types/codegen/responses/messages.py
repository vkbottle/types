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
    failed_peer_ids: list[int] = Field()
    failed_phone_numbers: list[str] = Field()
    invitees: list[int] = Field()


class MessagesAddChatUsersResponse(BaseResponse):
    response: "MessagesAddChatUsersResponseModel" = Field()


class MessagesCreateChatWithPeerIdsResponseModel(BaseModel):
    chat_id: int | None = Field(
        default=None,
    )
    peer_ids: list[int] | None = Field(
        default=None,
    )


class MessagesCreateChatWithPeerIdsResponse(BaseResponse):
    response: "MessagesCreateChatWithPeerIdsResponseModel" = Field()


class MessagesDeleteChatPhotoResponseModel(BaseModel):
    message_id: int | None = Field(
        default=None,
    )
    chat: "MessagesChat | None" = Field(
        default=None,
    )


class MessagesDeleteChatPhotoResponse(BaseResponse):
    response: "MessagesDeleteChatPhotoResponseModel" = Field()


class MessagesDeleteConversationResponseModel(BaseModel):
    last_deleted_id: int = Field()


class MessagesDeleteConversationResponse(BaseResponse):
    response: "MessagesDeleteConversationResponseModel" = Field()


class MessagesDeleteFullResponse(BaseResponse):
    response: list["MessagesDeleteFullResponseItem"] = Field()


class MessagesGetByConversationMessageIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetByConversationMessageIdExtendedResponse(BaseResponse):
    response: "MessagesGetByConversationMessageIdExtendedResponseModel" = Field()


class MessagesGetByConversationMessageIdResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()


class MessagesGetByConversationMessageIdResponse(BaseResponse):
    response: "MessagesGetByConversationMessageIdResponseModel" = Field()


class MessagesGetByIdExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetByIdExtendedResponse(BaseResponse):
    response: "MessagesGetByIdExtendedResponseModel" = Field()


class MessagesGetByIdResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()


class MessagesGetByIdResponse(BaseResponse):
    response: "MessagesGetByIdResponseModel" = Field()


class MessagesGetChatPreviewResponseModel(BaseModel):
    preview: "MessagesChatPreview" = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetChatPreviewResponse(BaseResponse):
    response: "MessagesGetChatPreviewResponseModel" = Field()


class MessagesGetChatChatIdsFieldsResponse(BaseResponse):
    response: list["MessagesChatFull"] = Field()


class MessagesGetChatChatIdsResponse(BaseResponse):
    response: list["MessagesChat"] = Field()


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
    items: list["MessagesConversationWithMessage"] = Field()
    unread_count: int | None = Field(
        default=None,
    )
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetConversationsResponse(BaseResponse):
    response: "MessagesGetConversationsResponseModel" = Field()


class MessagesGetHistoryAttachmentsResponseModel(BaseModel):
    items: list["MessagesHistoryAttachment"] = Field()
    next_from: str | None = Field(
        default=None,
    )
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetHistoryAttachmentsResponse(BaseResponse):
    response: "MessagesGetHistoryAttachmentsResponseModel" = Field()


class MessagesGetHistoryExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    conversations: list["MessagesConversation"] | None = Field(
        default=None,
    )


class MessagesGetHistoryExtendedResponse(BaseResponse):
    response: "MessagesGetHistoryExtendedResponseModel" = Field()


class MessagesGetHistoryResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()


class MessagesGetHistoryResponse(BaseResponse):
    response: "MessagesGetHistoryResponseModel" = Field()


class MessagesGetImportantMessagesExtendedResponseModel(BaseModel):
    messages: "MessagesMessagesArray" = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    conversations: list["MessagesConversation"] | None = Field(
        default=None,
    )


class MessagesGetImportantMessagesExtendedResponse(BaseResponse):
    response: "MessagesGetImportantMessagesExtendedResponseModel" = Field()


class MessagesGetImportantMessagesResponseModel(BaseModel):
    messages: "MessagesMessagesArray" = Field()
    profiles: list["UsersUser"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    conversations: list["MessagesConversation"] | None = Field(
        default=None,
    )


class MessagesGetImportantMessagesResponse(BaseResponse):
    response: "MessagesGetImportantMessagesResponseModel" = Field()


class MessagesGetIntentUsersResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )


class MessagesGetIntentUsersResponse(BaseResponse):
    response: "MessagesGetIntentUsersResponseModel" = Field()


class MessagesGetInviteLinkByOwnerResponseModel(BaseModel):
    items: list["MessagesGetInviteLinkByOwnerResponseItem"] = Field()


class MessagesGetInviteLinkByOwnerResponse(BaseResponse):
    response: "MessagesGetInviteLinkByOwnerResponseModel" = Field()


class MessagesGetInviteLinkResponseModel(BaseModel):
    link: str | None = Field(
        default=None,
    )


class MessagesGetInviteLinkResponse(BaseResponse):
    response: "MessagesGetInviteLinkResponseModel" = Field()


class MessagesGetLastActivityResponse(BaseResponse):
    response: "MessagesLastActivity" = Field()


class MessagesGetLongPollHistoryResponseModel(BaseModel):
    history: list[list[str | int]] | None = Field(
        default=None,
    )
    messages: "MessagesLongpollMessages | None" = Field(
        default=None,
    )
    credentials: "MessagesLongpollParams | None" = Field(
        default=None,
    )
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    chats: list["MessagesChat"] | None = Field(
        default=None,
    )
    new_pts: int | None = Field(
        default=None,
    )
    from_pts: int | None = Field(
        default=None,
    )
    more: bool | None = Field(
        default=None,
    )
    conversations: list["MessagesConversation"] | None = Field(
        default=None,
    )


class MessagesGetLongPollHistoryResponse(BaseResponse):
    response: "MessagesGetLongPollHistoryResponseModel" = Field()


class MessagesGetLongPollServerResponse(BaseResponse):
    response: "MessagesLongpollParams" = Field()


class MessagesGetMessagesReactionsResponseModel(BaseModel):
    items: list["MessagesReactionCountersResponseItem"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetMessagesReactionsResponse(BaseResponse):
    response: "MessagesGetMessagesReactionsResponseModel" = Field()


class MessagesGetReactedPeersResponseModel(BaseModel):
    count: int = Field()
    reactions: list["MessagesReactionResponseItem"] = Field()
    counters: list["MessagesReactionCounterResponseItem"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesGetReactedPeersResponse(BaseResponse):
    response: "MessagesGetReactedPeersResponseModel" = Field()


class MessagesGetReactionsAssetsResponseModel(BaseModel):
    version: int = Field()
    assets: list["MessagesReactionAssetItem"] = Field()
    reaction_ids: list[int] = Field()
    override_assets: list["MessagesReactionAssetItem"] | None = Field(
        default=None,
    )


class MessagesGetReactionsAssetsResponse(BaseResponse):
    response: "MessagesGetReactionsAssetsResponseModel" = Field()


class MessagesIsMessagesFromGroupAllowedResponseModel(BaseModel):
    is_allowed: bool | None = Field(
        default=None,
    )


class MessagesIsMessagesFromGroupAllowedResponse(BaseResponse):
    response: "MessagesIsMessagesFromGroupAllowedResponseModel" = Field()


class MessagesJoinChatByInviteLinkResponseModel(BaseModel):
    chat_id: int | None = Field(
        default=None,
    )


class MessagesJoinChatByInviteLinkResponse(BaseResponse):
    response: "MessagesJoinChatByInviteLinkResponseModel" = Field()


class MessagesMarkAsImportantDeprecatedResponse(BaseResponse):
    response: list[int] = Field()


class MessagesPinResponse(BaseResponse):
    response: "MessagesPinnedMessage" = Field()


class MessagesSearchConversationsExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesConversation"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )


class MessagesSearchConversationsExtendedResponse(BaseResponse):
    response: "MessagesSearchConversationsExtendedResponseModel" = Field()


class MessagesSearchConversationsResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesConversation"] = Field()


class MessagesSearchConversationsResponse(BaseResponse):
    response: "MessagesSearchConversationsResponseModel" = Field()


class MessagesSearchExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()
    profiles: list["UsersUserFull"] | None = Field(
        default=None,
    )
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    conversations: list["MessagesConversation"] | None = Field(
        default=None,
    )


class MessagesSearchExtendedResponse(BaseResponse):
    response: "MessagesSearchExtendedResponseModel" = Field()


class MessagesSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["MessagesMessage"] = Field()


class MessagesSearchResponse(BaseResponse):
    response: "MessagesSearchResponseModel" = Field()


class MessagesSendDeprecatedResponse(BaseResponse):
    response: int = Field()


class MessagesSendUserIdsResponse(BaseResponse):
    response: list["MessagesSendUserIdsResponseItem"] = Field()


class MessagesSetChatPhotoResponseModel(BaseModel):
    message_id: int | None = Field(
        default=None,
    )
    chat: "MessagesChat | None" = Field(
        default=None,
    )


class MessagesSetChatPhotoResponse(BaseResponse):
    response: "MessagesSetChatPhotoResponseModel" = Field()


__all__ = (
    "MessagesAddChatUsersResponse",
    "MessagesAddChatUsersResponseModel",
    "MessagesCreateChatWithPeerIdsResponse",
    "MessagesCreateChatWithPeerIdsResponseModel",
    "MessagesDeleteChatPhotoResponse",
    "MessagesDeleteChatPhotoResponseModel",
    "MessagesDeleteConversationResponse",
    "MessagesDeleteConversationResponseModel",
    "MessagesDeleteFullResponse",
    "MessagesGetByConversationMessageIdExtendedResponse",
    "MessagesGetByConversationMessageIdExtendedResponseModel",
    "MessagesGetByConversationMessageIdResponse",
    "MessagesGetByConversationMessageIdResponseModel",
    "MessagesGetByIdExtendedResponse",
    "MessagesGetByIdExtendedResponseModel",
    "MessagesGetByIdResponse",
    "MessagesGetByIdResponseModel",
    "MessagesGetChatChatIdsFieldsResponse",
    "MessagesGetChatChatIdsResponse",
    "MessagesGetChatFieldsResponse",
    "MessagesGetChatPreviewResponse",
    "MessagesGetChatPreviewResponseModel",
    "MessagesGetChatResponse",
    "MessagesGetConversationMembersResponse",
    "MessagesGetConversationsByIdExtendedResponse",
    "MessagesGetConversationsByIdResponse",
    "MessagesGetConversationsResponse",
    "MessagesGetConversationsResponseModel",
    "MessagesGetHistoryAttachmentsResponse",
    "MessagesGetHistoryAttachmentsResponseModel",
    "MessagesGetHistoryExtendedResponse",
    "MessagesGetHistoryExtendedResponseModel",
    "MessagesGetHistoryResponse",
    "MessagesGetHistoryResponseModel",
    "MessagesGetImportantMessagesExtendedResponse",
    "MessagesGetImportantMessagesExtendedResponseModel",
    "MessagesGetImportantMessagesResponse",
    "MessagesGetImportantMessagesResponseModel",
    "MessagesGetIntentUsersResponse",
    "MessagesGetIntentUsersResponseModel",
    "MessagesGetInviteLinkByOwnerResponse",
    "MessagesGetInviteLinkByOwnerResponseModel",
    "MessagesGetInviteLinkResponse",
    "MessagesGetInviteLinkResponseModel",
    "MessagesGetLastActivityResponse",
    "MessagesGetLongPollHistoryResponse",
    "MessagesGetLongPollHistoryResponseModel",
    "MessagesGetLongPollServerResponse",
    "MessagesGetMessagesReactionsResponse",
    "MessagesGetMessagesReactionsResponseModel",
    "MessagesGetReactedPeersResponse",
    "MessagesGetReactedPeersResponseModel",
    "MessagesGetReactionsAssetsResponse",
    "MessagesGetReactionsAssetsResponseModel",
    "MessagesIsMessagesFromGroupAllowedResponse",
    "MessagesIsMessagesFromGroupAllowedResponseModel",
    "MessagesJoinChatByInviteLinkResponse",
    "MessagesJoinChatByInviteLinkResponseModel",
    "MessagesMarkAsImportantDeprecatedResponse",
    "MessagesPinResponse",
    "MessagesSearchConversationsExtendedResponse",
    "MessagesSearchConversationsExtendedResponseModel",
    "MessagesSearchConversationsResponse",
    "MessagesSearchConversationsResponseModel",
    "MessagesSearchExtendedResponse",
    "MessagesSearchExtendedResponseModel",
    "MessagesSearchResponse",
    "MessagesSearchResponseModel",
    "MessagesSendDeprecatedResponse",
    "MessagesSendUserIdsResponse",
    "MessagesSetChatPhotoResponse",
    "MessagesSetChatPhotoResponseModel",
)
