import datetime

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
    items: list["GroupsAddress"] = Field()


class GroupsGetAddressesResponse(BaseResponse):
    response: "GroupsGetAddressesResponseModel" = Field()


class GroupsGetBannedResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsOwnerXtrBanInfo"] = Field()


class GroupsGetBannedResponse(BaseResponse):
    response: "GroupsGetBannedResponseModel" = Field()


class GroupsGetByIdObjectResponseModel(BaseModel):
    groups: list["GroupsGroupFull"] | None = Field(
        default=None,
    )
    profiles: list["GroupsProfileItem"] | None = Field(
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
    items: list["GroupsCallbackServer"] = Field()


class GroupsGetCallbackServersResponse(BaseResponse):
    response: "GroupsGetCallbackServersResponseModel" = Field()


class GroupsGetCallbackSettingsResponse(BaseResponse):
    response: "GroupsCallbackSettings" = Field()


class GroupsGetCatalogInfoExtendedResponseModel(BaseModel):
    enabled: bool = Field()
    categories: list["GroupsGroupCategoryFull"] | None = Field(
        default=None,
    )


class GroupsGetCatalogInfoExtendedResponse(BaseResponse):
    response: "GroupsGetCatalogInfoExtendedResponseModel" = Field()


class GroupsGetCatalogInfoResponseModel(BaseModel):
    enabled: bool = Field()
    categories: list["GroupsGroupCategory"] | None = Field(
        default=None,
    )


class GroupsGetCatalogInfoResponse(BaseResponse):
    response: "GroupsGetCatalogInfoResponseModel" = Field()


class GroupsGetInvitedUsersResponseModel(BaseModel):
    count: int = Field()
    items: list["UsersUserFull"] = Field()


class GroupsGetInvitedUsersResponse(BaseResponse):
    response: "GroupsGetInvitedUsersResponseModel" = Field()


class GroupsGetInvitesExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsGroupFull"] = Field()
    profiles: list["UsersUserMin"] = Field()
    groups: list["GroupsGroupFull"] = Field()


class GroupsGetInvitesExtendedResponse(BaseResponse):
    response: "GroupsGetInvitesExtendedResponseModel" = Field()


class GroupsGetInvitesResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsGroupFull"] = Field()


class GroupsGetInvitesResponse(BaseResponse):
    response: "GroupsGetInvitesResponseModel" = Field()


class GroupsGetLongPollServerResponse(BaseResponse):
    response: "GroupsLongPollServer" = Field()


class GroupsGetLongPollSettingsResponse(BaseResponse):
    response: "GroupsLongPollSettings" = Field()


class GroupsGetMembersFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsUserXtrRole"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class GroupsGetMembersFieldsResponse(BaseResponse):
    response: "GroupsGetMembersFieldsResponseModel" = Field()


class GroupsGetMembersFilterResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsMemberRole"] = Field()
    next_from: str | None = Field(
        default=None,
    )


class GroupsGetMembersFilterResponse(BaseResponse):
    response: "GroupsGetMembersFilterResponseModel" = Field()


class GroupsGetMembersResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()
    next_from: str | None = Field(
        default=None,
    )


class GroupsGetMembersResponse(BaseResponse):
    response: "GroupsGetMembersResponseModel" = Field()


class GroupsGetOnlineStatusResponseModel(BaseModel):
    status: "GroupsOnlineStatusType" = Field()
    minutes: int | None = Field(
        default=None,
    )


class GroupsGetOnlineStatusResponse(BaseResponse):
    response: "GroupsGetOnlineStatusResponseModel" = Field()


class GroupsGetRequestsFieldsResponseModel(BaseModel):
    count: int = Field()
    items: list["UsersUserFull"] = Field()


class GroupsGetRequestsFieldsResponse(BaseResponse):
    response: "GroupsGetRequestsFieldsResponseModel" = Field()


class GroupsGetRequestsResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


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
    obscene_words: list[str] = Field()
    toxic_filter: bool = Field()
    disable_replies_from_groups: bool = Field()
    photos: "GroupsGroupPhotos" = Field()
    title: str = Field()
    topics: "GroupsGroupTopics" = Field()
    video: "GroupsGroupVideo" = Field()
    wall: "GroupsGroupWall" = Field()
    wiki: "GroupsGroupWiki" = Field()
    access: "GroupsGroupAccess | None" = Field(
        default=None,
    )
    address: str | None = Field(
        default=None,
    )
    recognize_photo: int | None = Field(
        default=None,
    )
    contacts: bool | None = Field(
        default=None,
    )
    links: bool | None = Field(
        default=None,
    )
    sections_list: list["GroupsSectionsListItem"] | None = Field(
        default=None,
    )
    main_section: "GroupsGroupFullSection | None" = Field(
        default=None,
    )
    secondary_section: "GroupsGroupFullSection | None" = Field(
        default=None,
    )
    age_limits: "GroupsGroupAgeLimits | None" = Field(
        default=None,
    )
    events: bool | None = Field(
        default=None,
    )
    addresses: bool | None = Field(
        default=None,
    )
    bots_capabilities: bool | None = Field(
        default=None,
    )
    bots_start_button: bool | None = Field(
        default=None,
    )
    bots_add_to_chat: bool | None = Field(
        default=None,
    )
    bot_online_booking_enabled: bool | None = Field(
        default=None,
    )
    event_group_id: int | None = Field(
        default=None,
    )
    public_category: int | None = Field(
        default=None,
    )
    public_category_list: list["GroupsGroupPublicCategoryList"] | None = Field(
        default=None,
    )
    public_date: str | None = Field(
        default=None,
    )
    public_date_label: str | None = Field(
        default=None,
    )
    public_subcategory: int | None = Field(
        default=None,
    )
    rss: str | None = Field(
        default=None,
    )
    start_date: datetime.datetime | None = Field(
        default=None,
    )
    finish_date: datetime.datetime | None = Field(
        default=None,
    )
    subject: int | None = Field(
        default=None,
    )
    subject_list: list["GroupsSubjectItem"] | None = Field(
        default=None,
    )
    suggested_privacy: "GroupsGroupSuggestedPrivacy | None" = Field(
        default=None,
    )
    twitter: "GroupsSettingsTwitter | None" = Field(
        default=None,
    )
    website: str | None = Field(
        default=None,
    )
    phone: str | None = Field(
        default=None,
    )
    email: str | None = Field(
        default=None,
    )


class GroupsGetSettingsResponse(BaseResponse):
    response: "GroupsGetSettingsResponseModel" = Field()


class GroupsGetTagListResponse(BaseResponse):
    response: list["GroupsGroupTag"] = Field()


class GroupsGetTokenPermissionsResponseModel(BaseModel):
    mask: int = Field()
    permissions: list["GroupsTokenPermissionSetting"] = Field()


class GroupsGetTokenPermissionsResponse(BaseResponse):
    response: "GroupsGetTokenPermissionsResponseModel" = Field()


class GroupsGetObjectExtendedResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsGroupFull"] = Field()


class GroupsGetObjectExtendedResponse(BaseResponse):
    response: "GroupsGetObjectExtendedResponseModel" = Field()


class GroupsGetResponseModel(BaseModel):
    count: int = Field()
    items: list[int] = Field()


class GroupsGetResponse(BaseResponse):
    response: "GroupsGetResponseModel" = Field()


class GroupsInviteUserIdsListResponseModel(BaseModel):
    invites_send_count: int = Field()


class GroupsInviteUserIdsListResponse(BaseResponse):
    response: "GroupsInviteUserIdsListResponseModel" = Field()


class GroupsIsMemberExtendedResponseModel(BaseModel):
    member: bool = Field()
    invitation: bool | None = Field(
        default=None,
    )
    can_invite: bool | None = Field(
        default=None,
    )
    can_recall: bool | None = Field(
        default=None,
    )
    request: bool | None = Field(
        default=None,
    )


class GroupsIsMemberExtendedResponse(BaseResponse):
    response: "GroupsIsMemberExtendedResponseModel" = Field()


class GroupsIsMemberUserIdsExtendedResponse(BaseResponse):
    response: list["GroupsMemberStatusFull"] = Field()


class GroupsIsMemberUserIdsResponse(BaseResponse):
    response: list["GroupsMemberStatus"] = Field()


class GroupsSearchResponseModel(BaseModel):
    count: int = Field()
    items: list["GroupsGroupFull"] = Field()


class GroupsSearchResponse(BaseResponse):
    response: "GroupsSearchResponseModel" = Field()


__all__ = (
    "GroupsAddAddressResponse",
    "GroupsAddCallbackServerResponse",
    "GroupsAddCallbackServerResponseModel",
    "GroupsAddLinkResponse",
    "GroupsCreateResponse",
    "GroupsEditAddressResponse",
    "GroupsGetAddressesResponse",
    "GroupsGetAddressesResponseModel",
    "GroupsGetBannedResponse",
    "GroupsGetBannedResponseModel",
    "GroupsGetByIdObjectResponse",
    "GroupsGetByIdObjectResponseModel",
    "GroupsGetCallbackConfirmationCodeResponse",
    "GroupsGetCallbackConfirmationCodeResponseModel",
    "GroupsGetCallbackServersResponse",
    "GroupsGetCallbackServersResponseModel",
    "GroupsGetCallbackSettingsResponse",
    "GroupsGetCatalogInfoExtendedResponse",
    "GroupsGetCatalogInfoExtendedResponseModel",
    "GroupsGetCatalogInfoResponse",
    "GroupsGetCatalogInfoResponseModel",
    "GroupsGetInvitedUsersResponse",
    "GroupsGetInvitedUsersResponseModel",
    "GroupsGetInvitesExtendedResponse",
    "GroupsGetInvitesExtendedResponseModel",
    "GroupsGetInvitesResponse",
    "GroupsGetInvitesResponseModel",
    "GroupsGetLongPollServerResponse",
    "GroupsGetLongPollSettingsResponse",
    "GroupsGetMembersFieldsResponse",
    "GroupsGetMembersFieldsResponseModel",
    "GroupsGetMembersFilterResponse",
    "GroupsGetMembersFilterResponseModel",
    "GroupsGetMembersResponse",
    "GroupsGetMembersResponseModel",
    "GroupsGetObjectExtendedResponse",
    "GroupsGetObjectExtendedResponseModel",
    "GroupsGetOnlineStatusResponse",
    "GroupsGetOnlineStatusResponseModel",
    "GroupsGetRequestsFieldsResponse",
    "GroupsGetRequestsFieldsResponseModel",
    "GroupsGetRequestsResponse",
    "GroupsGetRequestsResponseModel",
    "GroupsGetResponse",
    "GroupsGetResponseModel",
    "GroupsGetSettingsResponse",
    "GroupsGetSettingsResponseModel",
    "GroupsGetTagListResponse",
    "GroupsGetTokenPermissionsResponse",
    "GroupsGetTokenPermissionsResponseModel",
    "GroupsInviteUserIdsListResponse",
    "GroupsInviteUserIdsListResponseModel",
    "GroupsIsMemberExtendedResponse",
    "GroupsIsMemberExtendedResponseModel",
    "GroupsIsMemberUserIdsExtendedResponse",
    "GroupsIsMemberUserIdsResponse",
    "GroupsSearchResponse",
    "GroupsSearchResponseModel",
)
