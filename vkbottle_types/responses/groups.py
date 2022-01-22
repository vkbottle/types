import inspect
import typing
from .base_response import BaseResponse
from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsAddress,
    GroupsBannedItem,
    GroupsCallbackServer,
    GroupsCallbackSettings,
    GroupsGroup,
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
    GroupsSectionsListItem,
    GroupsSettingsTwitter,
    GroupsSubjectItem,
    GroupsTokenPermissionSetting,
    GroupsUserXtrRole,
    UsersUserFull,
    UsersUserMin,
)


class AddAddressResponse(BaseResponse):
    response: GroupsAddress = None


class AddCallbackServerResponse(BaseResponse):
    response: "AddCallbackServerResponseModel" = None


class AddLinkResponse(BaseResponse):
    response: GroupsLinksItem = None


class CreateResponse(BaseResponse):
    response: GroupsGroup = None


class EditAddressResponse(BaseResponse):
    response: GroupsAddress = None


class GetAddressesResponse(BaseResponse):
    response: "GetAddressesResponseModel" = None


class GetBannedResponse(BaseResponse):
    response: "GetBannedResponseModel" = None


class GetByIdObjectLegacyResponse(BaseResponse):
    response: typing.List["GroupsGroupFull"] = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
    response: "GetCallbackConfirmationCodeResponseModel" = None


class GetCallbackServersResponse(BaseResponse):
    response: "GetCallbackServersResponseModel" = None


class GetCallbackSettingsResponse(BaseResponse):
    response: GroupsCallbackSettings = None


class GetCatalogInfoExtendedResponse(BaseResponse):
    response: "GetCatalogInfoExtendedResponseModel" = None


class GetCatalogInfoResponse(BaseResponse):
    response: "GetCatalogInfoResponseModel" = None


class GetCatalogResponse(BaseResponse):
    response: "GetCatalogResponseModel" = None


class GetInvitedUsersResponse(BaseResponse):
    response: "GetInvitedUsersResponseModel" = None


class GetInvitesExtendedResponse(BaseResponse):
    response: "GetInvitesExtendedResponseModel" = None


class GetInvitesResponse(BaseResponse):
    response: "GetInvitesResponseModel" = None


class GetLongPollServerResponse(BaseResponse):
    response: GroupsLongPollServer = None


class GetLongPollSettingsResponse(BaseResponse):
    response: GroupsLongPollSettings = None


class GetMembersFieldsResponse(BaseResponse):
    response: "GetMembersFieldsResponseModel" = None


class GetMembersFilterManagersResponse(BaseResponse):
    response: "GetMembersFilterManagersResponseModel" = None


class GetMembersFieldsFilterManagersResponse(BaseResponse):
    response: "GetMembersFilterManagersResponseModel" = None


class GetMembersResponse(BaseResponse):
    response: "GetMembersResponseModel" = None


class GetRequestsFieldsResponse(BaseResponse):
    response: "GetRequestsFieldsResponseModel" = None


class GetRequestsResponse(BaseResponse):
    response: "GetRequestsResponseModel" = None


class GetSettingsResponse(BaseResponse):
    response: "GetSettingsResponseModel" = None


class GetTagListResponse(BaseResponse):
    response: typing.List["GroupsGroupTag"] = None


class GetTokenPermissionsResponse(BaseResponse):
    response: "GetTokenPermissionsResponseModel" = None


class GetObjectExtendedResponse(BaseResponse):
    response: "GetObjectExtendedResponseModel" = None


class GetResponse(BaseResponse):
    response: "GetResponseModel" = None


class IsMemberExtendedResponse(BaseResponse):
    response: "IsMemberExtendedResponseModel" = None


class IsMemberResponse(BaseResponse):
    response: BaseBoolInt = None


class IsMemberUserIdsExtendedResponse(BaseResponse):
    response: typing.List["GroupsMemberStatusFull"] = None


class IsMemberUserIdsResponse(BaseResponse):
    response: typing.List["GroupsMemberStatus"] = None


class SearchResponse(BaseResponse):
    response: "SearchResponseModel" = None


class AddCallbackServerResponseModel(BaseResponse):
    server_id: typing.Optional[int] = None


class GetAddressesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsAddress"]] = None


class GetBannedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsBannedItem"]] = None


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
    code: typing.Optional[str] = None


class GetCallbackServersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsCallbackServer"]] = None


class GetCatalogInfoExtendedResponseModel(BaseResponse):
    enabled: typing.Optional["BaseBoolInt"] = None
    categories: typing.Optional[typing.List["GroupsGroupCategoryFull"]] = None


class GetCatalogInfoResponseModel(BaseResponse):
    enabled: typing.Optional["BaseBoolInt"] = None
    categories: typing.Optional[typing.List["GroupsGroupCategory"]] = None


class GetCatalogResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsGroup"]] = None


class GetInvitedUsersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetInvitesExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsGroupFull"]] = None
    profiles: typing.Optional[typing.List["UsersUserMin"]] = None
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetInvitesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetMembersFieldsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetMembersFilterManagersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsMemberRole"]] = None


class GetMembersFieldsFilterManagersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsUserXtrRole"]] = None


class GetMembersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class GetRequestsFieldsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["UsersUserFull"]] = None


class GetRequestsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class GetSettingsResponseModel(BaseResponse):
    access: typing.Optional["GroupsGroupAccess"] = None
    address: typing.Optional[str] = None
    audio: typing.Optional["GroupsGroupAudio"] = None
    articles: typing.Optional[int] = None
    recognize_photo: typing.Optional[int] = None
    city_id: typing.Optional[int] = None
    contacts: typing.Optional["BaseBoolInt"] = None
    links: typing.Optional["BaseBoolInt"] = None
    sections_list: typing.Optional[typing.List["GroupsSectionsListItem"]] = None
    main_section: typing.Optional["GroupsGroupFullSection"] = None
    secondary_section: typing.Optional["GroupsGroupFullSection"] = None
    age_limits: typing.Optional["GroupsGroupAgeLimits"] = None
    country_id: typing.Optional[int] = None
    description: typing.Optional[str] = None
    docs: typing.Optional["GroupsGroupDocs"] = None
    events: typing.Optional["BaseBoolInt"] = None
    obscene_filter: typing.Optional["BaseBoolInt"] = None
    obscene_stopwords: typing.Optional["BaseBoolInt"] = None
    obscene_words: typing.Optional[typing.List[str]] = None
    event_group_id: typing.Optional[int] = None
    photos: typing.Optional["GroupsGroupPhotos"] = None
    public_category: typing.Optional[int] = None
    public_category_list: typing.Optional[
        typing.List["GroupsGroupPublicCategoryList"]
    ] = None
    public_date: typing.Optional[str] = None
    public_date_label: typing.Optional[str] = None
    public_subcategory: typing.Optional[int] = None
    rss: typing.Optional[str] = None
    start_date: typing.Optional[int] = None
    finish_date: typing.Optional[int] = None
    subject: typing.Optional[int] = None
    subject_list: typing.Optional[typing.List["GroupsSubjectItem"]] = None
    suggested_privacy: typing.Optional["GroupsGroupSuggestedPrivacy"] = None
    title: typing.Optional[str] = None
    topics: typing.Optional["GroupsGroupTopics"] = None
    twitter: typing.Optional["GroupsSettingsTwitter"] = None
    video: typing.Optional["GroupsGroupVideo"] = None
    wall: typing.Optional["GroupsGroupWall"] = None
    website: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    email: typing.Optional[str] = None
    wiki: typing.Optional["GroupsGroupWiki"] = None


class GetTokenPermissionsResponseModel(BaseResponse):
    mask: typing.Optional[int] = None
    permissions: typing.Optional[typing.List["GroupsTokenPermissionSetting"]] = None


class GetObjectExtendedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsGroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List[int]] = None


class IsMemberExtendedResponseModel(BaseResponse):
    member: typing.Optional["BaseBoolInt"] = None
    invitation: typing.Optional["BaseBoolInt"] = None
    can_invite: typing.Optional["BaseBoolInt"] = None
    can_recall: typing.Optional["BaseBoolInt"] = None
    request: typing.Optional["BaseBoolInt"] = None


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsGroup"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
