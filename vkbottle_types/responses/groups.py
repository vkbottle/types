import inspect
import typing

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
    GroupsGroupFullMainSection,
    GroupsGroupLink,
    GroupsGroupPhotos,
    GroupsGroupPublicCategoryList,
    GroupsGroupSuggestedPrivacy,
    GroupsGroupTag,
    GroupsGroupTopics,
    GroupsGroupVideo,
    GroupsGroupWall,
    GroupsGroupWiki,
    GroupsLongPollServer,
    GroupsLongPollSettings,
    GroupsMemberRole,
    GroupsMemberStatus,
    GroupsMemberStatusFull,
    GroupsProfileItem,
    GroupsSectionsListItem,
    GroupsSettingsTwitter,
    GroupsSubjectItem,
    GroupsTokenPermissionSetting,
    GroupsUserXtrRole,
    UsersUserFull,
    UsersUserMin,
)

from .base_response import BaseResponse


class AddAddressResponse(BaseResponse):
    response: typing.Optional["AddAddressResponseModel"] = None


class AddCallbackServerResponse(BaseResponse):
    response: typing.Optional["AddCallbackServerResponseModel"] = None


class AddLinkResponse(BaseResponse):
    response: typing.Optional["AddLinkResponseModel"] = None


class CreateResponse(BaseResponse):
    response: typing.Optional["CreateResponseModel"] = None


class EditAddressResponse(BaseResponse):
    response: typing.Optional["EditAddressResponseModel"] = None


class GetAddressesResponse(BaseResponse):
    response: typing.Optional["GetAddressesResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: typing.Optional["GetBannedResponseModel"] = None


class GetByIdLegacyResponse(BaseResponse):
    response: typing.Optional["GetByIdLegacyResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: typing.Optional["GetByIdResponseModel"] = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
    response: typing.Optional["GetCallbackConfirmationCodeResponseModel"] = None


class GetCallbackServersResponse(BaseResponse):
    response: typing.Optional["GetCallbackServersResponseModel"] = None


class GetCallbackSettingsResponse(BaseResponse):
    response: typing.Optional["GetCallbackSettingsResponseModel"] = None


class GetCatalogInfoExtendedResponse(BaseResponse):
    response: typing.Optional["GetCatalogInfoExtendedResponseModel"] = None


class GetCatalogInfoResponse(BaseResponse):
    response: typing.Optional["GetCatalogInfoResponseModel"] = None


class GetCatalogResponse(BaseResponse):
    response: typing.Optional["GetCatalogResponseModel"] = None


class GetInvitedUsersResponse(BaseResponse):
    response: typing.Optional["GetInvitedUsersResponseModel"] = None


class GetInvitesExtendedResponse(BaseResponse):
    response: typing.Optional["GetInvitesExtendedResponseModel"] = None


class GetInvitesResponse(BaseResponse):
    response: typing.Optional["GetInvitesResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
    response: typing.Optional["GetLongPollServerResponseModel"] = None


class GetLongPollSettingsResponse(BaseResponse):
    response: typing.Optional["GetLongPollSettingsResponseModel"] = None


class GetMembersFieldsResponse(BaseResponse):
    response: typing.Optional["GetMembersFieldsResponseModel"] = None


class GetMembersFilterResponse(BaseResponse):
    response: typing.Optional["GetMembersFilterResponseModel"] = None


class GetMembersResponse(BaseResponse):
    response: typing.Optional["GetMembersResponseModel"] = None


class GetRequestsFieldsResponse(BaseResponse):
    response: typing.Optional["GetRequestsFieldsResponseModel"] = None


class GetRequestsResponse(BaseResponse):
    response: typing.Optional["GetRequestsResponseModel"] = None


class GetSettingsResponse(BaseResponse):
    response: typing.Optional["GetSettingsResponseModel"] = None


class GetTagListResponse(BaseResponse):
    response: typing.Optional["GetTagListResponseModel"] = None


class GetTokenPermissionsResponse(BaseResponse):
    response: typing.Optional["GetTokenPermissionsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: typing.Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: typing.Optional["GetResponseModel"] = None


class IsMemberExtendedResponse(BaseResponse):
    response: typing.Optional["IsMemberExtendedResponseModel"] = None


class IsMemberResponse(BaseResponse):
    response: typing.Optional["IsMemberResponseModel"] = None


class IsMemberUserIdsExtendedResponse(BaseResponse):
    response: typing.Optional["IsMemberUserIdsExtendedResponseModel"] = None


class IsMemberUserIdsResponse(BaseResponse):
    response: typing.Optional["IsMemberUserIdsResponseModel"] = None


class SearchResponse(BaseResponse):
    response: typing.Optional["SearchResponseModel"] = None


AddAddressResponseModel = GroupsAddress


class AddCallbackServerResponseModel(BaseResponse):
    server_id: typing.Optional[int] = None


AddLinkResponseModel = GroupsGroupLink


CreateResponseModel = GroupsGroup


EditAddressResponseModel = GroupsAddress


class GetAddressesResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsAddress"]] = None


class GetBannedResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsBannedItem"]] = None


GetByIdLegacyResponseModel = typing.List[GroupsGroupFull]


class GetByIdResponseModel(BaseResponse):
    groups: typing.Optional[typing.List["GroupsGroupFull"]] = None
    profiles: typing.Optional[typing.List["GroupsProfileItem"]] = None


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
    code: typing.Optional[str] = None


class GetCallbackServersResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsCallbackServer"]] = None


GetCallbackSettingsResponseModel = GroupsCallbackSettings


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


GetLongPollServerResponseModel = GroupsLongPollServer


GetLongPollSettingsResponseModel = GroupsLongPollSettings


class GetMembersFieldsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsUserXtrRole"]] = None


class GetMembersFilterResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsMemberRole"]] = None


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
    main_section: typing.Optional["GroupsGroupFullMainSection"] = None
    secondary_section: typing.Optional[int] = None
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


GetTagListResponseModel = typing.List[GroupsGroupTag]


class GetTokenPermissionsResponseModel(BaseResponse):
    mask: typing.Optional[int] = None
    permissions: typing.Optional[typing.List["GroupsTokenPermissionSetting"]] = None


class GetExtendedResponseModel(BaseResponse):
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


IsMemberResponseModel = BaseBoolInt


IsMemberUserIdsExtendedResponseModel = typing.List[GroupsMemberStatusFull]


IsMemberUserIdsResponseModel = typing.List[GroupsMemberStatus]


class SearchResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["GroupsGroup"]] = None


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
