import typing

from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    GroupsAddress,
    GroupsCallbackServer,
    GroupsCallbackSettings,
    GroupsGroupAccess,
    GroupsGroupAgeLimits,
    GroupsGroupAudio,
    GroupsGroupCategory,
    GroupsGroupCategoryFull,
    GroupsGroupDocs,
    GroupsGroupFull,
    GroupsGroupFullSection,
    GroupsGroupPhotos,
    GroupsGroupPublicCategoryList,
    GroupsGroupSuggestedPrivacy,
    GroupsGroupTag,
    GroupsGroupTopics,
    GroupsGroupVideo,
    GroupsGroupWall,
    GroupsGroupWiki,
    GroupsLinksItem,
    GroupsLongPollServer,
    GroupsLongPollSettings,
    GroupsMemberRole,
    GroupsMemberStatus,
    GroupsMemberStatusFull,
    GroupsOnlineStatusType,
    GroupsOwnerXtrBanInfo,
    GroupsProfileItem,
    GroupsSectionsListItem,
    GroupsSettingsTwitter,
    GroupsSubjectItem,
    GroupsTokenPermissionSetting,
    GroupsUserXtrRole,
    UsersUserFull,
    UsersUserMin,
)
from vkbottle_types.responses.base_response import BaseResponse


class GroupsAddAddressResponse(BaseResponse):
    response: "GroupsAddress" = Field()


class GroupsAddCallbackServerResponseModel(BaseModel):
    server_id: int = Field()


class GroupsAddCallbackServerResponse(BaseResponse):
    response: "GroupsAddCallbackServerResponseModel" = Field()


class GroupsAddLinkResponse(BaseResponse):
    response: "GroupsLinksItem" = Field()


class GroupsCreateResponse(BaseResponse):
    response: "GroupsGroupFull" = Field()


class GroupsEditAddressResponse(BaseResponse):
    response: "GroupsAddress" = Field()


class GroupsGetAddressesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsAddress"] = Field()


class GroupsGetAddressesResponse(BaseResponse):
    response: "GroupsGetAddressesResponseModel" = Field()


class GroupsGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsOwnerXtrBanInfo"] = Field()


class GroupsGetBannedResponse(BaseResponse):
    response: "GroupsGetBannedResponseModel" = Field()


class GroupsGetByIdObjectResponseModel(BaseModel):
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = Field(
        default=None,
    )
    profiles: typing.Optional[typing.List["GroupsProfileItem"]] = Field(
        default=None,
    )


class GroupsGetByIdObjectResponse(BaseResponse):
    response: "GroupsGetByIdObjectResponseModel" = Field()


class GroupsGetCallbackConfirmationCodeResponseModel(BaseModel):
    code: str = Field()


class GroupsGetCallbackConfirmationCodeResponse(BaseResponse):
    response: "GroupsGetCallbackConfirmationCodeResponseModel" = Field()


class GroupsGetCallbackServersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsCallbackServer"] = Field()


class GroupsGetCallbackServersResponse(BaseResponse):
    response: "GroupsGetCallbackServersResponseModel" = Field()


class GroupsGetCallbackSettingsResponse(BaseResponse):
    response: "GroupsCallbackSettings" = Field()


class GroupsGetCatalogInfoExtendedResponseModel(BaseModel):
    enabled: bool = Field()
    categories: typing.Optional[typing.List["GroupsGroupCategoryFull"]] = Field(
        default=None,
    )


class GroupsGetCatalogInfoExtendedResponse(BaseResponse):
    response: "GroupsGetCatalogInfoExtendedResponseModel" = Field()


class GroupsGetCatalogInfoResponseModel(BaseModel):
    enabled: bool = Field()
    categories: typing.Optional[typing.List["GroupsGroupCategory"]] = Field(
        default=None,
    )


class GroupsGetCatalogInfoResponse(BaseResponse):
    response: "GroupsGetCatalogInfoResponseModel" = Field()


class GroupsGetInvitedUsersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()


class GroupsGetInvitedUsersResponse(BaseResponse):
    response: "GroupsGetInvitedUsersResponseModel" = Field()


class GroupsGetInvitesExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsGroupFull"] = Field()
    profiles: typing.List["UsersUserMin"] = Field()
    groups: typing.List["GroupsGroupFull"] = Field()


class GroupsGetInvitesExtendedResponse(BaseResponse):
    response: "GroupsGetInvitesExtendedResponseModel" = Field()


class GroupsGetInvitesResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsGroupFull"] = Field()


class GroupsGetInvitesResponse(BaseResponse):
    response: "GroupsGetInvitesResponseModel" = Field()


class GroupsGetLongPollServerResponse(BaseResponse):
    response: "GroupsLongPollServer" = Field()


class GroupsGetLongPollSettingsResponse(BaseResponse):
    response: "GroupsLongPollSettings" = Field()


class GroupsGetMembersFieldsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsUserXtrRole"] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class GroupsGetMembersFieldsResponse(BaseResponse):
    response: "GroupsGetMembersFieldsResponseModel" = Field()


class GroupsGetMembersFilterResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsMemberRole"] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class GroupsGetMembersFilterResponse(BaseResponse):
    response: "GroupsGetMembersFilterResponseModel" = Field()


class GroupsGetMembersResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()
    next_from: typing.Optional[str] = Field(
        default=None,
    )


class GroupsGetMembersResponse(BaseResponse):
    response: "GroupsGetMembersResponseModel" = Field()


class GroupsGetOnlineStatusResponseModel(BaseModel):
    status: "GroupsOnlineStatusType" = Field()
    minutes: typing.Optional[int] = Field(
        default=None,
    )


class GroupsGetOnlineStatusResponse(BaseResponse):
    response: "GroupsGetOnlineStatusResponseModel" = Field()


class GroupsGetRequestsFieldsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["UsersUserFull"] = Field()


class GroupsGetRequestsFieldsResponse(BaseResponse):
    response: "GroupsGetRequestsFieldsResponseModel" = Field()


class GroupsGetRequestsResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class GroupsGetRequestsResponse(BaseResponse):
    response: "GroupsGetRequestsResponseModel" = Field()


class GroupsGetSettingsResponseModel(BaseModel):
    audio: "GroupsGroupAudio" = Field()
    articles: int = Field()
    city_id: int = Field()
    city_name: str = Field()
    description: str = Field()
    docs: "GroupsGroupDocs" = Field()
    obscene_filter: bool = Field()
    obscene_stopwords: bool = Field()
    obscene_words: typing.List[str] = Field()
    toxic_filter: bool = Field()
    disable_replies_from_groups: bool = Field()
    photos: "GroupsGroupPhotos" = Field()
    title: str = Field()
    topics: "GroupsGroupTopics" = Field()
    video: "GroupsGroupVideo" = Field()
    wall: "GroupsGroupWall" = Field()
    wiki: "GroupsGroupWiki" = Field()
    access: typing.Optional["GroupsGroupAccess"] = Field(
        default=None,
    )
    address: typing.Optional[str] = Field(
        default=None,
    )
    recognize_photo: typing.Optional[int] = Field(
        default=None,
    )
    contacts: typing.Optional[bool] = Field(
        default=None,
    )
    links: typing.Optional[bool] = Field(
        default=None,
    )
    sections_list: typing.Optional[typing.List["GroupsSectionsListItem"]] = Field(
        default=None,
    )
    main_section: typing.Optional["GroupsGroupFullSection"] = Field(
        default=None,
    )
    secondary_section: typing.Optional["GroupsGroupFullSection"] = Field(
        default=None,
    )
    age_limits: typing.Optional["GroupsGroupAgeLimits"] = Field(
        default=None,
    )
    events: typing.Optional[bool] = Field(
        default=None,
    )
    addresses: typing.Optional[bool] = Field(
        default=None,
    )
    bots_capabilities: typing.Optional[bool] = Field(
        default=None,
    )
    bots_start_button: typing.Optional[bool] = Field(
        default=None,
    )
    bots_add_to_chat: typing.Optional[bool] = Field(
        default=None,
    )
    bot_online_booking_enabled: typing.Optional[bool] = Field(
        default=None,
    )
    event_group_id: typing.Optional[int] = Field(
        default=None,
    )
    public_category: typing.Optional[int] = Field(
        default=None,
    )
    public_category_list: typing.Optional[typing.List["GroupsGroupPublicCategoryList"]] = Field(
        default=None,
    )
    public_date: typing.Optional[str] = Field(
        default=None,
    )
    public_date_label: typing.Optional[str] = Field(
        default=None,
    )
    public_subcategory: typing.Optional[int] = Field(
        default=None,
    )
    rss: typing.Optional[str] = Field(
        default=None,
    )
    start_date: typing.Optional[int] = Field(
        default=None,
    )
    finish_date: typing.Optional[int] = Field(
        default=None,
    )
    subject: typing.Optional[int] = Field(
        default=None,
    )
    subject_list: typing.Optional[typing.List["GroupsSubjectItem"]] = Field(
        default=None,
    )
    suggested_privacy: typing.Optional["GroupsGroupSuggestedPrivacy"] = Field(
        default=None,
    )
    twitter: typing.Optional["GroupsSettingsTwitter"] = Field(
        default=None,
    )
    website: typing.Optional[str] = Field(
        default=None,
    )
    phone: typing.Optional[str] = Field(
        default=None,
    )
    email: typing.Optional[str] = Field(
        default=None,
    )


class GroupsGetSettingsResponse(BaseResponse):
    response: "GroupsGetSettingsResponseModel" = Field()


class GroupsGetTagListResponse(BaseResponse):
    response: typing.List["GroupsGroupTag"] = Field()


class GroupsGetTokenPermissionsResponseModel(BaseModel):
    mask: int = Field()
    permissions: typing.List["GroupsTokenPermissionSetting"] = Field()


class GroupsGetTokenPermissionsResponse(BaseResponse):
    response: "GroupsGetTokenPermissionsResponseModel" = Field()


class GroupsGetObjectExtendedResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsGroupFull"] = Field()


class GroupsGetObjectExtendedResponse(BaseResponse):
    response: "GroupsGetObjectExtendedResponseModel" = Field()


class GroupsGetResponseModel(BaseModel):
    count: int = Field()
    items: typing.List[int] = Field()


class GroupsGetResponse(BaseResponse):
    response: "GroupsGetResponseModel" = Field()


class GroupsInviteUserIdsListResponseModel(BaseModel):
    invites_send_count: int = Field()


class GroupsInviteUserIdsListResponse(BaseResponse):
    response: "GroupsInviteUserIdsListResponseModel" = Field()


class GroupsIsMemberExtendedResponseModel(BaseModel):
    member: bool = Field()
    invitation: typing.Optional[bool] = Field(
        default=None,
    )
    can_invite: typing.Optional[bool] = Field(
        default=None,
    )
    can_recall: typing.Optional[bool] = Field(
        default=None,
    )
    request: typing.Optional[bool] = Field(
        default=None,
    )


class GroupsIsMemberExtendedResponse(BaseResponse):
    response: "GroupsIsMemberExtendedResponseModel" = Field()


class GroupsIsMemberUserIdsExtendedResponse(BaseResponse):
    response: typing.List["GroupsMemberStatusFull"] = Field()


class GroupsIsMemberUserIdsResponse(BaseResponse):
    response: typing.List["GroupsMemberStatus"] = Field()


class GroupsSearchResponseModel(BaseModel):
    count: int = Field()
    items: typing.List["GroupsGroupFull"] = Field()


class GroupsSearchResponse(BaseResponse):
    response: "GroupsSearchResponseModel" = Field()
