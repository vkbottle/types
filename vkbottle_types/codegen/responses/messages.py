import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    MessagesChat,
    MessagesChatFull,
    MessagesDeleteFullResponseItem,
    MessagesGetConversationById,
    MessagesGetConversationByIdExtended,
    MessagesGetConversationMembers,
    MessagesLastActivity,
    MessagesLongpollParams,
    MessagesPinnedMessage,
    MessagesSendUserIdsResponseItem,
)
from vkbottle_types.responses.base_response import BaseResponse


class MessagesAddChatUsersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesCreateChatWithPeerIdsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesDeleteChatPhotoResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesDeleteConversationResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesDeleteFullResponse(BaseResponse):
    response: typing.List[MessagesDeleteFullResponseItem] = Field()


class MessagesGetByConversationMessageIdExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetByConversationMessageIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetByIdExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetByIdResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetChatPreviewResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetChatChatIdsFieldsResponse(BaseResponse):
    response: typing.List[MessagesChatFull] = Field()


class MessagesGetChatChatIdsResponse(BaseResponse):
    response: typing.List[MessagesChat] = Field()


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


class MessagesGetConversationsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetHistoryAttachmentsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetHistoryExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetHistoryResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetImportantMessagesExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetImportantMessagesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetIntentUsersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetInviteLinkByOwnerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetInviteLinkResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetLastActivityResponse(BaseResponse):
    response: "MessagesLastActivity" = Field()


class MessagesGetLongPollHistoryResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetLongPollServerResponse(BaseResponse):
    response: "MessagesLongpollParams" = Field()


class MessagesGetMessagesReactionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetReactedPeersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesGetReactionsAssetsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesIsMessagesFromGroupAllowedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesJoinChatByInviteLinkResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesMarkAsImportantDeprecatedResponse(BaseResponse):
    response: typing.List[int] = Field()


class MessagesPinResponse(BaseResponse):
    response: "MessagesPinnedMessage" = Field()


class MessagesSearchConversationsExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesSearchConversationsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesSearchExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class MessagesSendDeprecatedResponse(BaseResponse):
    response: int = Field()


class MessagesSendUserIdsResponse(BaseResponse):
    response: typing.List[MessagesSendUserIdsResponseItem] = Field()


class MessagesSetChatPhotoResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
