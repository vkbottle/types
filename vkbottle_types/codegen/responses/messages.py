import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    BaseMessageError,
    MessagesForeignMessage,
    MessagesChatRestrictions,
    MessagesConversation,
    MessagesMessageAttachmentType,
    MessagesHistoryMessageAttachmentType,
    GroupsGroupFull,
    MarketMarketItem,
    BaseSticker,
    MessagesMessageActionStatus,
    MessagesActionOneOf,
    BaseGeo,
    MessagesConversationPeerType,
    MessagesKeyboardButtonPropertyAction,
    PhotosPhoto,
    GiftsLayout,
    MessagesReactionAssetItemLinks,
    AudioAudio,
    BaseBoolInt,
    MessagesConversationPeer,
    MessagesChatSettingsPhoto,
    MessagesFwdMessages,
    MessagesChatSettingsAcl,
    CallsCall,
    MessagesUserTypeForXtrInvitedBy,
    MessagesPinnedMessage,
    DocsDoc,
    MessagesChatSettingsState,
    MessagesUserXtrInvitedBy,
    BaseLinkButton,
    MessagesGraffiti,
    MessagesOutReadBy,
    MessagesMessage,
    MarketMarketAlbum,
    MessagesPushSettings,
    MessagesConversationSortId,
    MessagesKeyboard,
    MessagesMessageRequestData,
    MessagesReactionCounterResponseItem,
    MessagesChatPushSettings,
    PollsPoll,
    MessagesMessageActionPhoto,
    MessagesKeyboardButton,
    WallWallComment,
    MessagesAudioMessage,
    MessagesChatSettings,
    MessagesHistoryMessageAttachment,
    MessagesConversationCanWrite,
    UsersUserFull,
    MessagesChatSettingsPermissions,
    StoriesStory,
    MessagesMessageAttachment,
    MessagesConversationMember,
)


class MessagesActionOneOfResponseModel(BaseModel):
    pass


class MessagesActionOneOfResponse(BaseResponse):
    response: "MessagesActionOneOfResponseModel"


class MessagesAudioMessageResponseModel(BaseModel):
    duration: int = Field(
        description="Audio message duration in seconds",
    )

    id: int = Field(
        description="Audio message ID",
    )

    link_mp3: str = Field(
        description="MP3 file URL",
    )

    link_ogg: str = Field(
        description="OGG file URL",
    )

    owner_id: int = Field(
        description="Audio message owner ID",
    )

    waveform: typing.List[int] = Field()

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for audio message",
    )

    transcript_error: typing.Optional[int] = Field(
        default=None,
    )


class MessagesAudioMessageResponse(BaseResponse):
    response: "MessagesAudioMessageResponseModel"


class MessagesChatResponseModel(BaseModel):
    admin_id: int = Field(
        description="Chat creator ID",
    )

    id: int = Field(
        description="Chat ID",
    )

    type: str = Field(
        description="Chat type",
    )

    users: typing.List[int] = Field()

    members_count: int = Field(
        description="Count members in a chat",
    )

    kicked: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been kicked from the chat",
    )

    left: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been left the chat",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 100 px in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200 px in width",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 50 px in width",
    )

    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Chat title",
    )

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default",
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
        description="If chat is group channel",
    )


class MessagesChatResponse(BaseResponse):
    response: "MessagesChatResponseModel"


class MessagesChatFullResponseModel(BaseModel):
    admin_id: int = Field(
        description="Chat creator ID",
    )

    id: int = Field(
        description="Chat ID",
    )

    type: str = Field(
        description="Chat type",
    )

    users: typing.List[MessagesUserXtrInvitedBy] = Field()

    members_count: int = Field(
        description="Count members in a chat",
    )

    kicked: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been kicked from the chat",
    )

    left: typing.Optional[bool] = Field(
        default=None,
        description="Shows that user has been left the chat",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 100 px in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200 px in width",
    )

    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 50 px in width",
    )

    push_settings: typing.Optional["MessagesChatPushSettings"] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Chat title",
    )

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default",
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
        description="If chat is group channel",
    )


class MessagesChatFullResponse(BaseResponse):
    response: "MessagesChatFullResponseModel"


class MessagesChatPreviewResponseModel(BaseModel):
    admin_id: typing.Optional[int] = Field(
        default=None,
    )

    joined: typing.Optional[bool] = Field(
        default=None,
    )

    local_id: typing.Optional[int] = Field(
        default=None,
    )

    members: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    members_count: typing.Optional[int] = Field(
        default=None,
    )

    title: typing.Optional[str] = Field(
        default=None,
    )

    is_member: typing.Optional[bool] = Field(
        default=None,
    )

    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        default=None,
    )

    is_don: typing.Optional[bool] = Field(
        default=None,
    )

    is_nft: typing.Optional[bool] = Field(
        default=None,
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )

    button: typing.Optional["BaseLinkButton"] = Field(
        default=None,
    )


class MessagesChatPreviewResponse(BaseResponse):
    response: "MessagesChatPreviewResponseModel"


class MessagesChatPushSettingsResponseModel(BaseModel):
    disabled_until: typing.Optional[int] = Field(
        default=None,
        description="Time until that notifications are disabled",
    )

    sound: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the sound is on",
    )


class MessagesChatPushSettingsResponse(BaseResponse):
    response: "MessagesChatPushSettingsResponseModel"


class MessagesChatRestrictionsResponseModel(BaseModel):
    admins_promote_users: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can promote users to admins",
    )

    only_admins_edit_info: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can change chat info",
    )

    only_admins_edit_pin: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can edit pinned message",
    )

    only_admins_invite: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can invite users to this chat",
    )

    only_admins_kick: typing.Optional[bool] = Field(
        default=None,
        description="Only admins can kick users from this chat",
    )


class MessagesChatRestrictionsResponse(BaseResponse):
    response: "MessagesChatRestrictionsResponseModel"


class MessagesChatSettingsResponseModel(BaseModel):
    owner_id: int = Field()

    title: str = Field(
        description="Chat title",
    )

    state: "MessagesChatSettingsState" = Field()

    acl: "MessagesChatSettingsAcl" = Field()

    members_count: typing.Optional[int] = Field(
        default=None,
    )

    friends_count: typing.Optional[int] = Field(
        default=None,
    )

    pinned_message: typing.Optional["MessagesPinnedMessage"] = Field(
        default=None,
    )

    photo: typing.Optional["MessagesChatSettingsPhoto"] = Field(
        default=None,
    )

    admin_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Ids of chat admins",
    )

    active_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    is_group_channel: typing.Optional[bool] = Field(
        default=None,
    )

    permissions: typing.Optional["MessagesChatSettingsPermissions"] = Field(
        default=None,
    )

    is_disappearing: typing.Optional[bool] = Field(
        default=None,
    )

    theme: typing.Optional[str] = Field(
        default=None,
    )

    disappearing_chat_link: typing.Optional[str] = Field(
        default=None,
    )

    is_service: typing.Optional[bool] = Field(
        default=None,
    )


class MessagesChatSettingsResponse(BaseResponse):
    response: "MessagesChatSettingsResponseModel"


class MessagesChatSettingsAclResponseModel(BaseModel):
    can_change_info: bool = Field(
        description="Can you change photo, description and name",
    )

    can_change_invite_link: bool = Field(
        description="Can you change invite link for this chat",
    )

    can_change_pin: bool = Field(
        description="Can you pin/unpin message for this chat",
    )

    can_invite: bool = Field(
        description="Can you invite other peers in chat",
    )

    can_promote_users: bool = Field(
        description="Can you promote simple users to chat admins",
    )

    can_see_invite_link: bool = Field(
        description="Can you see invite link for this chat",
    )

    can_moderate: bool = Field(
        description="Can you moderate (delete) other users' messages",
    )

    can_copy_chat: bool = Field(
        description="Can you copy chat",
    )

    can_call: bool = Field(
        description="Can you init group call in the chat",
    )

    can_use_mass_mentions: bool = Field(
        description="Can you use mass mentions",
    )

    can_change_service_type: typing.Optional[bool] = Field(
        default=None,
        description="Can you change chat service type",
    )


class MessagesChatSettingsAclResponse(BaseResponse):
    response: "MessagesChatSettingsAclResponseModel"


class MessagesChatSettingsPermissionsResponseModel(BaseModel):
    invite: typing.Optional[typing.Literal["owner", "owner_and_admins", "all"]] = Field(
        default=None,
        description="Who can invite users to chat",
    )

    change_info: typing.Optional[
        typing.Literal["owner", "owner_and_admins", "all"]
    ] = Field(
        default=None,
        description="Who can change chat info",
    )

    change_pin: typing.Optional[
        typing.Literal["owner", "owner_and_admins", "all"]
    ] = Field(
        default=None,
        description="Who can change pinned message",
    )

    use_mass_mentions: typing.Optional[
        typing.Literal["owner", "owner_and_admins", "all"]
    ] = Field(
        default=None,
        description="Who can use mass mentions",
    )

    see_invite_link: typing.Optional[
        typing.Literal["owner", "owner_and_admins", "all"]
    ] = Field(
        default=None,
        description="Who can see invite link",
    )

    call: typing.Optional[typing.Literal["owner", "owner_and_admins", "all"]] = Field(
        default=None,
        description="Who can make calls",
    )

    change_admins: typing.Optional[typing.Literal["owner", "owner_and_admins"]] = Field(
        default=None,
        description="Who can change admins",
    )


class MessagesChatSettingsPermissionsResponse(BaseResponse):
    response: "MessagesChatSettingsPermissionsResponseModel"


class MessagesChatSettingsPhotoResponseModel(BaseModel):
    photo_50: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 50px in width",
    )

    photo_100: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 100px in width",
    )

    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image with 200px in width",
    )

    is_default_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default",
    )

    is_default_call_photo: typing.Optional[bool] = Field(
        default=None,
        description="If provided photo is default call photo",
    )


class MessagesChatSettingsPhotoResponse(BaseResponse):
    response: "MessagesChatSettingsPhotoResponseModel"


class MessagesChatSettingsStateResponseModel(enum.Enum):
    IN = "in"

    KICKED = "kicked"

    LEFT = "left"

    OUT = "out"


class MessagesChatSettingsStateResponse(BaseResponse):
    response: "MessagesChatSettingsStateResponseModel"


class MessagesConversationResponseModel(BaseModel):
    peer: "MessagesConversationPeer" = Field()

    last_message_id: int = Field(
        description="ID of the last message in conversation",
    )

    in_read: int = Field(
        description="Last message user have read",
    )

    out_read: int = Field(
        description="Last outcoming message have been read by the opponent",
    )

    sort_id: typing.Optional["MessagesConversationSortId"] = Field(
        default=None,
    )

    last_conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Conversation message ID of the last message in conversation",
    )

    unread_count: typing.Optional[int] = Field(
        default=None,
        description="Unread messages number",
    )

    is_marked_unread: typing.Optional[bool] = Field(
        default=None,
        description="Is this conversation uread",
    )

    out_read_by: typing.Optional["MessagesOutReadBy"] = Field(
        default=None,
    )

    important: typing.Optional[bool] = Field(
        default=None,
    )

    unanswered: typing.Optional[bool] = Field(
        default=None,
    )

    special_service_type: typing.Optional[typing.Literal["business_notify"]] = Field(
        default=None,
    )

    message_request_data: typing.Optional["MessagesMessageRequestData"] = Field(
        default=None,
    )

    mentions: typing.Optional[typing.List[int]] = Field(
        default=None,
        description="Ids of messages with mentions",
    )

    current_keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )

    push_settings: typing.Optional["MessagesPushSettings"] = Field(
        default=None,
    )

    can_write: typing.Optional["MessagesConversationCanWrite"] = Field(
        default=None,
    )

    chat_settings: typing.Optional["MessagesChatSettings"] = Field(
        default=None,
    )


class MessagesConversationResponse(BaseResponse):
    response: "MessagesConversationResponseModel"


class MessagesConversationCanWriteResponseModel(BaseModel):
    allowed: bool = Field()

    reason: typing.Optional[int] = Field(
        default=None,
    )


class MessagesConversationCanWriteResponse(BaseResponse):
    response: "MessagesConversationCanWriteResponseModel"


class MessagesConversationMemberResponseModel(BaseModel):
    member_id: int = Field()

    can_kick: typing.Optional[bool] = Field(
        default=None,
        description="Is it possible for user to kick this member",
    )

    invited_by: typing.Optional[int] = Field(
        default=None,
    )

    is_admin: typing.Optional[bool] = Field(
        default=None,
    )

    is_owner: typing.Optional[bool] = Field(
        default=None,
    )

    is_message_request: typing.Optional[bool] = Field(
        default=None,
    )

    join_date: typing.Optional[int] = Field(
        default=None,
    )

    request_date: typing.Optional[int] = Field(
        default=None,
        description="Message request date",
    )


class MessagesConversationMemberResponse(BaseResponse):
    response: "MessagesConversationMemberResponseModel"


class MessagesConversationPeerResponseModel(BaseModel):
    id: int = Field()

    type: "MessagesConversationPeerType" = Field()

    local_id: typing.Optional[int] = Field(
        default=None,
    )


class MessagesConversationPeerResponse(BaseResponse):
    response: "MessagesConversationPeerResponseModel"


class MessagesConversationPeerTypeResponseModel(enum.Enum):
    CHAT = "chat"

    EMAIL = "email"

    USER = "user"

    GROUP = "group"


class MessagesConversationPeerTypeResponse(BaseResponse):
    response: "MessagesConversationPeerTypeResponseModel"


class MessagesConversationSortIdResponseModel(BaseModel):
    major_id: int = Field(
        description="Major id for sorting conversations",
    )

    minor_id: int = Field(
        description="Minor id for sorting conversations",
    )


class MessagesConversationSortIdResponse(BaseResponse):
    response: "MessagesConversationSortIdResponseModel"


class MessagesConversationWithMessageResponseModel(BaseModel):
    conversation: "MessagesConversation" = Field()

    last_message: typing.Optional["MessagesMessage"] = Field(
        default=None,
    )


class MessagesConversationWithMessageResponse(BaseResponse):
    response: "MessagesConversationWithMessageResponseModel"


class MessagesDeleteFullResponseItemResponseModel(BaseModel):
    peer_id: typing.Optional[int] = Field(
        default=None,
    )

    message_id: typing.Optional[int] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )

    response: typing.Optional[bool] = Field(
        default=None,
    )

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )


class MessagesDeleteFullResponseItemResponse(BaseResponse):
    response: "MessagesDeleteFullResponseItemResponseModel"


class MessagesForeignMessageResponseModel(BaseModel):
    date: int = Field(
        description="Date when the message was created",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    text: str = Field(
        description="Message text",
    )

    attachments: typing.Optional[typing.List[MessagesMessageAttachment]] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Conversation message ID",
    )

    fwd_messages: typing.Optional[typing.List[MessagesForeignMessage]] = Field(
        default=None,
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Message ID",
    )

    peer_id: typing.Optional[int] = Field(
        default=None,
        description="Peer ID",
    )

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )

    update_time: typing.Optional[int] = Field(
        default=None,
        description="Date when the message has been updated in Unixtime",
    )

    was_listened: typing.Optional[bool] = Field(
        default=None,
        description="Was the audio message inside already listened by you",
    )

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesForeignMessageResponse(BaseResponse):
    response: "MessagesForeignMessageResponseModel"


class MessagesForwardResponseModel(BaseModel):
    owner_id: typing.Optional[int] = Field(
        default=None,
        description="Messages owner_id",
    )

    peer_id: typing.Optional[int] = Field(
        default=None,
        description="Messages peer_id",
    )

    conversation_message_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    message_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )

    is_reply: typing.Optional[bool] = Field(
        default=None,
        description="If you need to reply to a message",
    )


class MessagesForwardResponse(BaseResponse):
    response: "MessagesForwardResponseModel"


MessagesFwdMessagesResponseModel = typing.List["MessagesForeignMessage"]


class MessagesFwdMessagesResponse(BaseResponse):
    response: "MessagesFwdMessagesResponseModel"


class MessagesGetConversationByIdResponseModel(BaseModel):
    count: int = Field(
        description="Total number",
    )

    items: typing.List[MessagesConversation] = Field()


class MessagesGetConversationByIdResponse(BaseResponse):
    response: "MessagesGetConversationByIdResponseModel"


class MessagesGetConversationByIdExtendedResponseModel(MessagesGetConversationById):
    profiles: typing.Optional[typing.List[UsersUserFull]] = Field(
        default=None,
    )

    groups: typing.Optional[typing.List[GroupsGroupFull]] = Field(
        default=None,
    )


class MessagesGetConversationByIdExtendedResponse(BaseResponse):
    response: "MessagesGetConversationByIdExtendedResponseModel"


class MessagesGetConversationMembersResponseModel(BaseModel):
    items: typing.List[MessagesConversationMember] = Field()

    count: int = Field(
        description="Chat members count",
    )

    chat_restrictions: typing.Optional["MessagesChatRestrictions"] = Field(
        default=None,
    )

    profiles: typing.Optional[typing.List[UsersUserFull]] = Field(
        default=None,
    )

    groups: typing.Optional[typing.List[GroupsGroupFull]] = Field(
        default=None,
    )


class MessagesGetConversationMembersResponse(BaseResponse):
    response: "MessagesGetConversationMembersResponseModel"


class MessagesGraffitiResponseModel(BaseModel):
    id: int = Field(
        description="Graffiti ID",
    )

    owner_id: int = Field(
        description="Graffiti owner ID",
    )

    url: str = Field(
        description="Graffiti URL",
    )

    width: int = Field(
        description="Graffiti width",
    )

    height: int = Field(
        description="Graffiti height",
    )

    access_key: typing.Optional[str] = Field(
        default=None,
        description="Access key for graffiti",
    )


class MessagesGraffitiResponse(BaseResponse):
    response: "MessagesGraffitiResponseModel"


class MessagesHistoryAttachmentResponseModel(BaseModel):
    attachment: "MessagesHistoryMessageAttachment" = Field()

    date: int = Field(
        description="Message sending time",
    )

    message_id: int = Field(
        description="Message ID",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    message_expire_ttl: typing.Optional[int] = Field(
        default=None,
        description="Message Exipire ttl",
    )

    cmid: typing.Optional[int] = Field(
        default=None,
        description="Conversation Message ID",
    )

    forward_level: typing.Optional[int] = Field(
        default=None,
        description="Forward level (optional)",
    )

    was_listened: typing.Optional[bool] = Field(
        default=None,
    )

    position: typing.Optional[int] = Field(
        default=None,
        description="Attachment position in the Message",
    )


class MessagesHistoryAttachmentResponse(BaseResponse):
    response: "MessagesHistoryAttachmentResponseModel"


class MessagesHistoryMessageAttachmentResponseModel(BaseModel):
    type: "MessagesHistoryMessageAttachmentType" = Field()

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )


class MessagesHistoryMessageAttachmentResponse(BaseResponse):
    response: "MessagesHistoryMessageAttachmentResponseModel"


class MessagesHistoryMessageAttachmentTypeResponseModel(enum.Enum):
    PHOTO = "photo"

    VIDEO = "video"

    AUDIO = "audio"

    DOC = "doc"

    LINK = "link"

    MARKET = "market"

    WALL = "wall"

    SHARE = "share"

    APP_ACTION = "app_action"

    GRAFFITI = "graffiti"

    AUDIO_MESSAGE = "audio_message"


class MessagesHistoryMessageAttachmentTypeResponse(BaseResponse):
    response: "MessagesHistoryMessageAttachmentTypeResponseModel"


class MessagesKeyboardResponseModel(BaseModel):
    one_time: bool = Field(
        description="Should this keyboard disappear on first use",
    )

    buttons: typing.List[typing.List[MessagesKeyboardButton]] = Field()

    author_id: typing.Optional[int] = Field(
        default=None,
        description="Community or bot, which set this keyboard",
    )

    inline: typing.Optional[bool] = Field(
        default=None,
    )


class MessagesKeyboardResponse(BaseResponse):
    response: "MessagesKeyboardResponseModel"


class MessagesKeyboardButtonResponseModel(BaseModel):
    action: "MessagesKeyboardButtonPropertyAction" = Field()

    color: typing.Optional[
        typing.Literal["default", "positive", "negative", "primary"]
    ] = Field(
        default=None,
        description="Button color",
    )


class MessagesKeyboardButtonResponse(BaseResponse):
    response: "MessagesKeyboardButtonResponseModel"


class MessagesKeyboardButtonActionCallbackResponseModel(BaseModel):
    label: str = Field(
        description="Label for button",
    )

    type: typing.Literal["callback"] = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionCallbackResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionCallbackResponseModel"


class MessagesKeyboardButtonActionLocationResponseModel(BaseModel):
    type: typing.Literal["location"] = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionLocationResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionLocationResponseModel"


class MessagesKeyboardButtonActionOpenAppResponseModel(BaseModel):
    app_id: int = Field(
        description="Fragment value in app link like vk.com/app{app_id}_-654321#hash",
    )

    label: str = Field(
        description="Label for button",
    )

    owner_id: int = Field(
        description="Fragment value in app link like vk.com/app123456_{owner_id}#hash",
    )

    type: typing.Literal["open_app"] = Field()

    hash: typing.Optional[str] = Field(
        default=None,
        description="Fragment value in app link like vk.com/app123456_-654321#{hash}",
    )

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionOpenAppResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionOpenAppResponseModel"


class MessagesKeyboardButtonActionOpenLinkResponseModel(BaseModel):
    label: str = Field(
        description="Label for button",
    )

    link: str = Field(
        description="link for button",
    )

    type: typing.Literal["open_link"] = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionOpenLinkResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionOpenLinkResponseModel"


class MessagesKeyboardButtonActionOpenPhotoResponseModel(BaseModel):
    type: typing.Literal["open_photo"] = Field()


class MessagesKeyboardButtonActionOpenPhotoResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionOpenPhotoResponseModel"


class MessagesKeyboardButtonActionTextResponseModel(BaseModel):
    label: str = Field(
        description="Label for button",
    )

    type: typing.Literal["text"] = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionTextResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionTextResponseModel"


class MessagesKeyboardButtonActionVkpayResponseModel(BaseModel):
    hash: str = Field(
        description="Fragment value in app link like vk.com/app123456_-654321#{hash}",
    )

    type: typing.Literal["vkpay"] = Field()

    payload: typing.Optional[str] = Field(
        default=None,
        description="Additional data sent along with message for developer convenience",
    )


class MessagesKeyboardButtonActionVkpayResponse(BaseResponse):
    response: "MessagesKeyboardButtonActionVkpayResponseModel"


class MessagesKeyboardButtonPropertyActionResponseModel(BaseModel):
    pass


class MessagesKeyboardButtonPropertyActionResponse(BaseResponse):
    response: "MessagesKeyboardButtonPropertyActionResponseModel"


class MessagesLastActivityResponseModel(BaseModel):
    online: bool = Field(
        description="Information whether user is online",
    )

    time: int = Field(
        description="Time when user was online in Unixtime",
    )


class MessagesLastActivityResponse(BaseResponse):
    response: "MessagesLastActivityResponseModel"


class MessagesLongpollMessagesResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Total number",
    )

    items: typing.Optional[typing.List[MessagesMessage]] = Field(
        default=None,
    )


class MessagesLongpollMessagesResponse(BaseResponse):
    response: "MessagesLongpollMessagesResponseModel"


class MessagesLongpollParamsResponseModel(BaseModel):
    server: str = Field(
        description="Server URL",
    )

    key: str = Field(
        description="Key",
    )

    ts: int = Field(
        description="Timestamp",
    )

    pts: typing.Optional[int] = Field(
        default=None,
        description="Persistent timestamp",
    )


class MessagesLongpollParamsResponse(BaseResponse):
    response: "MessagesLongpollParamsResponseModel"


class MessagesMessageResponseModel(BaseModel):
    date: int = Field(
        description="Date when the message has been sent in Unixtime",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    id: int = Field(
        description="Message ID",
    )

    out: bool = Field(
        description="Information whether the message is outcoming",
    )

    peer_id: int = Field(
        description="Peer ID",
    )

    text: str = Field(
        description="Message text",
    )

    action: typing.Optional["MessagesActionOneOf"] = Field(
        default=None,
    )

    admin_author_id: typing.Optional[int] = Field(
        default=None,
        description="Only for messages from community. Contains user ID of community admin, who sent this message.",
    )

    attachments: typing.Optional[typing.List[MessagesMessageAttachment]] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Unique auto-incremented number for all messages with this peer",
    )

    deleted: typing.Optional[bool] = Field(
        default=None,
        description="Is it an deleted message",
    )

    fwd_messages: typing.Optional["MessagesFwdMessages"] = Field(
        default=None,
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    important: typing.Optional[bool] = Field(
        default=None,
        description="Is it an important message",
    )

    is_hidden: typing.Optional[bool] = Field(
        default=None,
    )

    is_cropped: typing.Optional[bool] = Field(
        default=None,
        description="this message is cropped for bot",
    )

    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )

    members_count: typing.Optional[int] = Field(
        default=None,
        description="Members number",
    )

    payload: typing.Optional[str] = Field(
        default=None,
    )

    random_id: typing.Optional[int] = Field(
        default=None,
        description="ID used for sending messages. It returned only for outgoing messages",
    )

    ref: typing.Optional[str] = Field(
        default=None,
    )

    ref_source: typing.Optional[str] = Field(
        default=None,
    )

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )

    reaction_id: typing.Optional[int] = Field(
        default=None,
        description="Reaction id set on message",
    )

    reactions: typing.Optional[
        typing.List[MessagesReactionCounterResponseItem]
    ] = Field(
        default=None,
        description="Actual reactions counters on this message",
    )

    last_reaction_id: typing.Optional[int] = Field(
        default=None,
        description="Last reaction id set on this message",
    )

    update_time: typing.Optional[int] = Field(
        default=None,
        description="Date when the message has been updated in Unixtime",
    )

    was_listened: typing.Optional[bool] = Field(
        default=None,
        description="Was the audio message inside already listened by you",
    )

    pinned_at: typing.Optional[int] = Field(
        default=None,
        description="Date when the message has been pinned in Unixtime",
    )

    is_silent: typing.Optional[bool] = Field(
        default=None,
        description="Is silent message, push without sound",
    )


class MessagesMessageResponse(BaseResponse):
    response: "MessagesMessageResponseModel"


class MessagesMessageActionResponseModel(BaseModel):
    type: "MessagesMessageActionStatus" = Field()

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Message ID",
    )

    email: typing.Optional[str] = Field(
        default=None,
        description="Email address for chat_invite_user or chat_kick_user actions",
    )

    member_id: typing.Optional[int] = Field(
        default=None,
        description="User or email peer ID",
    )

    message: typing.Optional[str] = Field(
        default=None,
        description="Message body of related message",
    )

    photo: typing.Optional["MessagesMessageActionPhoto"] = Field(
        default=None,
    )

    text: typing.Optional[str] = Field(
        default=None,
        description="New chat title for chat_create and chat_title_update actions",
    )


class MessagesMessageActionResponse(BaseResponse):
    response: "MessagesMessageActionResponseModel"


class MessagesMessageActionPhotoResponseModel(BaseModel):
    photo_50: str = Field(
        description="URL of the preview image with 50px in width",
    )

    photo_100: str = Field(
        description="URL of the preview image with 100px in width",
    )

    photo_200: str = Field(
        description="URL of the preview image with 200px in width",
    )


class MessagesMessageActionPhotoResponse(BaseResponse):
    response: "MessagesMessageActionPhotoResponseModel"


class MessagesMessageActionStatusResponseModel(enum.Enum):
    CHAT_PHOTO_UPDATE = "chat_photo_update"

    CHAT_PHOTO_REMOVE = "chat_photo_remove"

    CHAT_CREATE = "chat_create"

    CHAT_TITLE_UPDATE = "chat_title_update"

    CHAT_INVITE_USER = "chat_invite_user"

    CHAT_KICK_USER = "chat_kick_user"

    CHAT_PIN_MESSAGE = "chat_pin_message"

    CHAT_UNPIN_MESSAGE = "chat_unpin_message"

    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"

    CHAT_INVITE_USER_BY_MESSAGE_REQUEST = "chat_invite_user_by_message_request"

    CHAT_SCREENSHOT = "chat_screenshot"


class MessagesMessageActionStatusResponse(BaseResponse):
    response: "MessagesMessageActionStatusResponseModel"


class MessagesMessageAttachmentResponseModel(BaseModel):
    type: "MessagesMessageAttachmentType" = Field()

    audio: typing.Optional["AudioAudio"] = Field(
        default=None,
    )

    audio_message: typing.Optional["MessagesAudioMessage"] = Field(
        default=None,
    )

    call: typing.Optional["CallsCall"] = Field(
        default=None,
    )

    doc: typing.Optional["DocsDoc"] = Field(
        default=None,
    )

    gift: typing.Optional["GiftsLayout"] = Field(
        default=None,
    )

    graffiti: typing.Optional["MessagesGraffiti"] = Field(
        default=None,
    )

    market: typing.Optional["MarketMarketItem"] = Field(
        default=None,
    )

    market_market_album: typing.Optional["MarketMarketAlbum"] = Field(
        default=None,
    )

    photo: typing.Optional["PhotosPhoto"] = Field(
        default=None,
    )

    sticker: typing.Optional["BaseSticker"] = Field(
        default=None,
    )

    story: typing.Optional["StoriesStory"] = Field(
        default=None,
    )

    wall_reply: typing.Optional["WallWallComment"] = Field(
        default=None,
    )

    poll: typing.Optional["PollsPoll"] = Field(
        default=None,
    )


class MessagesMessageAttachmentResponse(BaseResponse):
    response: "MessagesMessageAttachmentResponseModel"


class MessagesMessageAttachmentTypeResponseModel(enum.Enum):
    PHOTO = "photo"

    AUDIO = "audio"

    VIDEO = "video"

    VIDEO_PLAYLIST = "video_playlist"

    DOC = "doc"

    LINK = "link"

    MARKET = "market"

    MARKET_ALBUM = "market_album"

    GIFT = "gift"

    STICKER = "sticker"

    WALL = "wall"

    WALL_REPLY = "wall_reply"

    ARTICLE = "article"

    POLL = "poll"

    CALL = "call"

    GRAFFITI = "graffiti"

    AUDIO_MESSAGE = "audio_message"


class MessagesMessageAttachmentTypeResponse(BaseResponse):
    response: "MessagesMessageAttachmentTypeResponseModel"


class MessagesMessageRequestDataResponseModel(BaseModel):
    status: typing.Optional[str] = Field(
        default=None,
        description="Status of message request",
    )

    inviter_id: typing.Optional[int] = Field(
        default=None,
        description="Message request sender id",
    )

    request_date: typing.Optional[int] = Field(
        default=None,
        description="Message request date",
    )


class MessagesMessageRequestDataResponse(BaseResponse):
    response: "MessagesMessageRequestDataResponseModel"


class MessagesMessagesArrayResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
    )

    items: typing.Optional[typing.List[MessagesMessage]] = Field(
        default=None,
    )


class MessagesMessagesArrayResponse(BaseResponse):
    response: "MessagesMessagesArrayResponseModel"


class MessagesOutReadByResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
    )

    member_ids: typing.Optional[typing.List[int]] = Field(
        default=None,
    )


class MessagesOutReadByResponse(BaseResponse):
    response: "MessagesOutReadByResponseModel"


class MessagesPinnedMessageResponseModel(BaseModel):
    id: int = Field(
        description="Message ID",
    )

    date: int = Field(
        description="Date when the message has been sent in Unixtime",
    )

    from_id: int = Field(
        description="Message author's ID",
    )

    peer_id: int = Field(
        description="Peer ID",
    )

    text: str = Field(
        description="Message text",
    )

    attachments: typing.Optional[typing.List[MessagesMessageAttachment]] = Field(
        default=None,
    )

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
        description="Unique auto-incremented number for all messages with this peer",
    )

    fwd_messages: typing.Optional[typing.List[MessagesForeignMessage]] = Field(
        default=None,
        description="Forwarded messages",
    )

    geo: typing.Optional["BaseGeo"] = Field(
        default=None,
    )

    reply_message: typing.Optional["MessagesForeignMessage"] = Field(
        default=None,
    )

    keyboard: typing.Optional["MessagesKeyboard"] = Field(
        default=None,
    )


class MessagesPinnedMessageResponse(BaseResponse):
    response: "MessagesPinnedMessageResponseModel"


class MessagesPushSettingsResponseModel(BaseModel):
    disabled_forever: bool = Field(
        description="Information whether push notifications are disabled forever",
    )

    no_sound: bool = Field(
        description="Information whether the sound is on",
    )

    disabled_until: typing.Optional[int] = Field(
        default=None,
        description="Time until what notifications are disabled",
    )

    disabled_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mentions are disabled",
    )

    disabled_mass_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mass mentions (like '@all', '@online') are disabled",
    )


class MessagesPushSettingsResponse(BaseResponse):
    response: "MessagesPushSettingsResponseModel"


class MessagesReactionAssetItemResponseModel(BaseModel):
    reaction_id: int = Field()

    links: "MessagesReactionAssetItemLinks" = Field(
        description="Liks to reactions assets for each asset type",
    )


class MessagesReactionAssetItemResponse(BaseResponse):
    response: "MessagesReactionAssetItemResponseModel"


class MessagesReactionAssetItemLinksResponseModel(BaseModel):
    big_animation: str = Field(
        description="Big reaction animation json file",
    )

    small_animation: str = Field(
        description="Small reaction animation json file",
    )

    static: str = Field(
        description="Reaction image file",
    )


class MessagesReactionAssetItemLinksResponse(BaseResponse):
    response: "MessagesReactionAssetItemLinksResponseModel"


class MessagesReactionCounterResponseItemResponseModel(BaseModel):
    reaction_id: int = Field()

    count: int = Field()

    user_ids: typing.List[int] = Field()


class MessagesReactionCounterResponseItemResponse(BaseResponse):
    response: "MessagesReactionCounterResponseItemResponseModel"


class MessagesReactionCountersResponseItemResponseModel(BaseModel):
    cmid: int = Field()

    counters: typing.List[MessagesReactionCounterResponseItem] = Field()


class MessagesReactionCountersResponseItemResponse(BaseResponse):
    response: "MessagesReactionCountersResponseItemResponseModel"


class MessagesReactionResponseItemResponseModel(BaseModel):
    user_id: int = Field()

    reaction_id: int = Field()


class MessagesReactionResponseItemResponse(BaseResponse):
    response: "MessagesReactionResponseItemResponseModel"


class MessagesSendUserIdsResponseItemResponseModel(BaseModel):
    peer_id: int = Field()

    message_id: int = Field()

    conversation_message_id: typing.Optional[int] = Field(
        default=None,
    )

    error: typing.Optional["BaseMessageError"] = Field(
        default=None,
    )


class MessagesSendUserIdsResponseItemResponse(BaseResponse):
    response: "MessagesSendUserIdsResponseItemResponseModel"


class MessagesTemplateActionTypeNamesResponseModel(enum.Enum):
    TEXT = "text"

    START = "start"

    LOCATION = "location"

    VKPAY = "vkpay"

    OPEN_APP = "open_app"

    OPEN_PHOTO = "open_photo"

    OPEN_LINK = "open_link"

    CALLBACK = "callback"

    INTENT_SUBSCRIBE = "intent_subscribe"

    INTENT_UNSUBSCRIBE = "intent_unsubscribe"

    OPEN_MODAL_VIEW = "open_modal_view"


class MessagesTemplateActionTypeNamesResponse(BaseResponse):
    response: "MessagesTemplateActionTypeNamesResponseModel"


class MessagesUserTypeForXtrInvitedByResponseModel(enum.Enum):
    PROFILE = "profile"

    GROUP = "group"


class MessagesUserTypeForXtrInvitedByResponse(BaseResponse):
    response: "MessagesUserTypeForXtrInvitedByResponseModel"


class MessagesUserXtrInvitedByResponseModel(UsersUserXtrType):
    invited_by: typing.Optional[int] = Field(
        default=None,
        description="ID of the inviter",
    )

    name: typing.Optional[str] = Field(
        default=None,
        description="Name of group",
    )

    type: typing.Optional["MessagesUserTypeForXtrInvitedBy"] = Field(
        default=None,
    )


class MessagesUserXtrInvitedByResponse(BaseResponse):
    response: "MessagesUserXtrInvitedByResponseModel"
