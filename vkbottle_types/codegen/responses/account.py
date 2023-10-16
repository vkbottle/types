import typing
from vkbottle_types.responses.base_response import BaseResponse, BaseModel
from vkbottle_types.base_model import Field

from vkbottle_types.objects import (
    AccountPushParamsSettings,
    AccountUserSettingsInterest,
    AccountPushParamsOnoff,
    BaseBoolInt,
    AccountPushParamsMode,
    AccountPushParams,
    AccountNameRequestStatus,
    AccountPushConversationsItem,
    AccountPushConversations,
)


class AccountAccountCountersResponseModel(BaseModel):
    app_requests: typing.Optional[int] = Field(
        default=None,
        description="New app requests number",
    )

    events: typing.Optional[int] = Field(
        default=None,
        description="New events number",
    )

    faves: typing.Optional[int] = Field(
        default=None,
        description="New faves number",
    )

    friends: typing.Optional[int] = Field(
        default=None,
        description="New friends requests number",
    )

    friends_recommendations: typing.Optional[int] = Field(
        default=None,
        description="New friends recommendations number",
    )

    gifts: typing.Optional[int] = Field(
        default=None,
        description="New gifts number",
    )

    groups: typing.Optional[int] = Field(
        default=None,
        description="New groups number",
    )

    messages: typing.Optional[int] = Field(
        default=None,
        description="New messages number",
    )

    memories: typing.Optional[int] = Field(
        default=None,
        description="New memories number",
    )

    notes: typing.Optional[int] = Field(
        default=None,
        description="New notes number",
    )

    notifications: typing.Optional[int] = Field(
        default=None,
        description="New notifications number",
    )

    photos: typing.Optional[int] = Field(
        default=None,
        description="New photo tags number",
    )


class AccountAccountCountersResponse(BaseResponse):
    response: "AccountAccountCountersResponseModel"


class AccountCountersFilterResponseModel(enum.Enum):
    APP_REQUESTS = "app_requests"

    EVENTS = "events"

    FRIENDS = "friends"

    FRIENDS_RECOMMENDATIONS = "friends_recommendations"

    GIFTS = "gifts"

    GROUPS = "groups"

    MESSAGES = "messages"

    NOTES = "notes"

    NOTIFICATIONS = "notifications"

    PHOTOS = "photos"

    FAVES = "faves"

    MEMORIES = "memories"


class AccountCountersFilterResponse(BaseResponse):
    response: "AccountCountersFilterResponseModel"


class AccountInfoResponseModel(BaseModel):
    _2fa_required: typing.Optional[bool] = Field(
        default=None,
        description="Two factor authentication is enabled",
        alias="2fa_required",
    )

    country: typing.Optional[str] = Field(
        default=None,
        description="Country code",
    )

    https_required: typing.Optional[bool] = Field(
        default=None,
        description="Information whether HTTPS-only is enabled",
    )

    intro: typing.Optional[bool] = Field(
        default=None,
        description="Information whether user has been processed intro",
    )

    lang: typing.Optional[int] = Field(
        default=None,
        description="Language ID",
    )

    no_wall_replies: typing.Optional[bool] = Field(
        default=None,
        description="Information whether wall comments should be hidden",
    )

    own_posts_default: typing.Optional[bool] = Field(
        default=None,
        description="Information whether only owners posts should be shown",
    )


class AccountInfoResponse(BaseResponse):
    response: "AccountInfoResponseModel"


class AccountNameRequestResponseModel(BaseModel):
    first_name: typing.Optional[str] = Field(
        default=None,
        description="First name in request",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Request ID needed to cancel the request",
    )

    last_name: typing.Optional[str] = Field(
        default=None,
        description="Last name in request",
    )

    status: typing.Optional["AccountNameRequestStatus"] = Field(
        default=None,
    )

    lang: typing.Optional[str] = Field(
        default=None,
        description="Text to display to user",
    )

    link_href: typing.Optional[str] = Field(
        default=None,
        description="href for link in lang field",
    )

    link_label: typing.Optional[str] = Field(
        default=None,
        description="label to display for link in lang field",
    )


class AccountNameRequestResponse(BaseResponse):
    response: "AccountNameRequestResponseModel"


class AccountNameRequestStatusResponseModel(enum.Enum):
    SUCCESS = "success"

    PROCESSING = "processing"

    DECLINED = "declined"

    WAS_ACCEPTED = "was_accepted"

    WAS_DECLINED = "was_declined"

    DECLINED_WITH_LINK = "declined_with_link"

    RESPONSE = "response"

    RESPONSE_WITH_LINK = "response_with_link"


class AccountNameRequestStatusResponse(BaseResponse):
    response: "AccountNameRequestStatusResponseModel"


class AccountOfferResponseModel(BaseModel):
    description: typing.Optional[str] = Field(
        default=None,
        description="Offer description",
    )

    id: typing.Optional[int] = Field(
        default=None,
        description="Offer ID",
    )

    img: typing.Optional[str] = Field(
        default=None,
        description="URL of the preview image",
    )

    instruction: typing.Optional[str] = Field(
        default=None,
        description="Instruction how to process the offer",
    )

    instruction_html: typing.Optional[str] = Field(
        default=None,
        description="Instruction how to process the offer (HTML format)",
    )

    price: typing.Optional[int] = Field(
        default=None,
        description="Offer price",
    )

    short_description: typing.Optional[str] = Field(
        default=None,
        description="Offer short description",
    )

    tag: typing.Optional[str] = Field(
        default=None,
        description="Offer tag",
    )

    title: typing.Optional[str] = Field(
        default=None,
        description="Offer title",
    )

    currency_amount: typing.Optional[float] = Field(
        default=None,
        description="Currency amount",
    )

    link_id: typing.Optional[int] = Field(
        default=None,
        description="Link id",
    )

    link_type: typing.Optional[typing.Literal["profile", "group", "app"]] = Field(
        default=None,
        description="Link type",
    )


class AccountOfferResponse(BaseResponse):
    response: "AccountOfferResponseModel"


class AccountPushConversationsResponseModel(BaseModel):
    count: typing.Optional[int] = Field(
        default=None,
        description="Items count",
    )

    items: typing.Optional[typing.List[AccountPushConversationsItem]] = Field(
        default=None,
    )


class AccountPushConversationsResponse(BaseResponse):
    response: "AccountPushConversationsResponseModel"


class AccountPushConversationsItemResponseModel(BaseModel):
    disabled_until: int = Field(
        description="Time until that notifications are disabled in seconds",
    )

    peer_id: int = Field(
        description="Peer ID",
    )

    sound: bool = Field(
        description="Information whether the sound are enabled",
    )

    disabled_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mentions are disabled",
    )

    disabled_mass_mentions: typing.Optional[bool] = Field(
        default=None,
        description="Information whether the mass mentions (like '@all', '@online') are disabled. Can be affected by 'disabled_mentions'",
    )


class AccountPushConversationsItemResponse(BaseResponse):
    response: "AccountPushConversationsItemResponseModel"


class AccountPushParamsResponseModel(BaseModel):
    msg: typing.Optional[typing.List[AccountPushParamsMode]] = Field(
        default=None,
    )

    chat: typing.Optional[typing.List[AccountPushParamsMode]] = Field(
        default=None,
    )

    like: typing.Optional[typing.List[AccountPushParamsSettings]] = Field(
        default=None,
    )

    repost: typing.Optional[typing.List[AccountPushParamsSettings]] = Field(
        default=None,
    )

    comment: typing.Optional[typing.List[AccountPushParamsSettings]] = Field(
        default=None,
    )

    mention: typing.Optional[typing.List[AccountPushParamsSettings]] = Field(
        default=None,
    )

    reply: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    new_post: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    wall_post: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    wall_publish: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    friend: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    friend_found: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    friend_accepted: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    group_invite: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    group_accepted: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    birthday: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    event_soon: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    app_request: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )

    sdk_open: typing.Optional[typing.List[AccountPushParamsOnoff]] = Field(
        default=None,
    )


class AccountPushParamsResponse(BaseResponse):
    response: "AccountPushParamsResponseModel"


class AccountPushParamsModeResponseModel(enum.Enum):
    ON = "on"

    OFF = "off"

    NO_SOUND = "no_sound"

    NO_TEXT = "no_text"


class AccountPushParamsModeResponse(BaseResponse):
    response: "AccountPushParamsModeResponseModel"


class AccountPushParamsOnoffResponseModel(enum.Enum):
    ON = "on"

    OFF = "off"


class AccountPushParamsOnoffResponse(BaseResponse):
    response: "AccountPushParamsOnoffResponseModel"


class AccountPushParamsSettingsResponseModel(enum.Enum):
    ON = "on"

    OFF = "off"

    FR_OF_FR = "fr_of_fr"


class AccountPushParamsSettingsResponse(BaseResponse):
    response: "AccountPushParamsSettingsResponseModel"


class AccountPushSettingsResponseModel(BaseModel):
    disabled: typing.Optional[bool] = Field(
        default=None,
        description="Information whether notifications are disabled",
    )

    disabled_until: typing.Optional[int] = Field(
        default=None,
        description="Time until that notifications are disabled in Unixtime",
    )

    settings: typing.Optional["AccountPushParams"] = Field(
        default=None,
    )

    conversations: typing.Optional["AccountPushConversations"] = Field(
        default=None,
    )


class AccountPushSettingsResponse(BaseResponse):
    response: "AccountPushSettingsResponseModel"


class AccountUserSettingsResponseModel(UsersUserMin, UsersUserSettingsXtr):
    photo_200: typing.Optional[str] = Field(
        default=None,
        description="URL of square photo of the user with 200 pixels in width",
    )

    is_service_account: typing.Optional[bool] = Field(
        default=None,
        description="flag about service account",
    )


class AccountUserSettingsResponse(BaseResponse):
    response: "AccountUserSettingsResponseModel"


class AccountUserSettingsInterestResponseModel(BaseModel):
    title: str = Field()

    value: str = Field()


class AccountUserSettingsInterestResponse(BaseResponse):
    response: "AccountUserSettingsInterestResponseModel"


class AccountUserSettingsInterestsResponseModel(BaseModel):
    activities: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    interests: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    music: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    tv: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    movies: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    books: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    games: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    quotes: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )

    about: typing.Optional["AccountUserSettingsInterest"] = Field(
        default=None,
    )


class AccountUserSettingsInterestsResponse(BaseResponse):
    response: "AccountUserSettingsInterestsResponseModel"
