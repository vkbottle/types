import typing
from typing import Any, List, Optional, Union

from vkbottle_types.objects import (
    BaseBoolInt,
    GroupsAddress,
    GroupsBannedItem,
    GroupsCallbackServer,
    GroupsCallbackSettings,
    GroupsGroup,
    GroupsGroupAccess,
    GroupsGroupAudio,
    GroupsGroupCategory,
    GroupsGroupCategoryFull,
    GroupsGroupDocs,
    GroupsGroupFull,
    GroupsGroupFullMainSection,
    GroupsGroupLink,
    GroupsGroupPublicCategoryList,
    GroupsGroupTopics,
    GroupsGroupVideo,
    GroupsGroupWall,
    GroupsGroupWiki,
    GroupsGroupXtrInvitedBy,
    GroupsLongPollServer,
    GroupsLongPollSettings,
    GroupsMemberRole,
    GroupsMemberStatus,
    GroupsMemberStatusFull,
    GroupsSettingsTwitter,
    GroupsSubjectItem,
    GroupsTokenPermissionSetting,
    GroupsUserXtrRole,
    UsersUserFull,
    UsersUserMin,
)

from .base_response import BaseResponse


class AddAddressResponse(BaseResponse):
    response: Optional["AddAddressResponseModel"] = None


class AddCallbackServerResponse(BaseResponse):
    response: Optional["AddCallbackServerResponseModel"] = None


class AddLinkResponse(BaseResponse):
    response: Optional["AddLinkResponseModel"] = None


class CreateResponse(BaseResponse):
    response: Optional["CreateResponseModel"] = None


class EditAddressResponse(BaseResponse):
    response: Optional["EditAddressResponseModel"] = None


class GetAddressesResponse(BaseResponse):
    response: Optional["GetAddressesResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: Optional["GetBannedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional["GetByIdResponseModel"] = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
    response: Optional["GetCallbackConfirmationCodeResponseModel"] = None


class GetCallbackServersResponse(BaseResponse):
    response: Optional["GetCallbackServersResponseModel"] = None


class GetCallbackSettingsResponse(BaseResponse):
    response: Optional["GetCallbackSettingsResponseModel"] = None


class GetCatalogInfoExtendedResponse(BaseResponse):
    response: Optional["GetCatalogInfoExtendedResponseModel"] = None


class GetCatalogInfoResponse(BaseResponse):
    response: Optional["GetCatalogInfoResponseModel"] = None


class GetCatalogResponse(BaseResponse):
    response: Optional["GetCatalogResponseModel"] = None


class GetInvitedUsersResponse(BaseResponse):
    response: Optional["GetInvitedUsersResponseModel"] = None


class GetInvitesExtendedResponse(BaseResponse):
    response: Optional["GetInvitesExtendedResponseModel"] = None


class GetInvitesResponse(BaseResponse):
    response: Optional["GetInvitesResponseModel"] = None


class GetLongPollServerResponse(BaseResponse):
    response: Optional["GetLongPollServerResponseModel"] = None


class GetLongPollSettingsResponse(BaseResponse):
    response: Optional["GetLongPollSettingsResponseModel"] = None


class GetMembersFieldsResponse(BaseResponse):
    response: Optional["GetMembersFieldsResponseModel"] = None


class GetMembersFilterResponse(BaseResponse):
    response: Optional["GetMembersFilterResponseModel"] = None


class GetMembersResponse(BaseResponse):
    response: Optional["GetMembersResponseModel"] = None


class GetRequestsFieldsResponse(BaseResponse):
    response: Optional["GetRequestsFieldsResponseModel"] = None


class GetRequestsResponse(BaseResponse):
    response: Optional["GetRequestsResponseModel"] = None


class GetSettingsResponse(BaseResponse):
    response: Optional["GetSettingsResponseModel"] = None


class GetTokenPermissionsResponse(BaseResponse):
    response: Optional["GetTokenPermissionsResponseModel"] = None


class GetExtendedResponse(BaseResponse):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class IsMemberExtendedResponse(BaseResponse):
    response: Optional["IsMemberExtendedResponseModel"] = None


class IsMemberResponse(BaseResponse):
    response: Optional["IsMemberResponseModel"] = None


class IsMemberUserIdsExtendedResponse(BaseResponse):
    response: Optional["IsMemberUserIdsExtendedResponseModel"] = None


class IsMemberUserIdsResponse(BaseResponse):
    response: Optional["IsMemberUserIdsResponseModel"] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


AddAddressResponseModel = Optional[GroupsAddress]


class AddCallbackServerResponseModel(BaseResponse):
    server_id: Optional[int] = None


AddLinkResponseModel = Optional[GroupsGroupLink]

CreateResponseModel = Optional[GroupsGroup]

EditAddressResponseModel = Optional[GroupsAddress]


class GetAddressesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsAddress"]] = None


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsBannedItem"]] = None


GetByIdResponseModel = List[GroupsGroupFull]


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
    code: Optional[str] = None


class GetCallbackServersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsCallbackServer"]] = None


GetCallbackSettingsResponseModel = Optional[GroupsCallbackSettings]


class GetCatalogInfoExtendedResponseModel(BaseResponse):
    enabled: Optional[int] = None
    categories: Optional[List["GroupsGroupCategoryFull"]] = None


class GetCatalogInfoResponseModel(BaseResponse):
    enabled: Optional[int] = None
    categories: Optional[List["GroupsGroupCategory"]] = None


class GetCatalogResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsGroup"]] = None


class GetInvitedUsersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetInvitesExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsGroupXtrInvitedBy"]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetInvitesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsGroupXtrInvitedBy"]] = None


GetLongPollServerResponseModel = Optional[GroupsLongPollServer]

GetLongPollSettingsResponseModel = Optional[GroupsLongPollSettings]


class GetMembersFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsUserXtrRole"]] = None


class GetMembersFilterResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[Union["GroupsMemberRole", int]]] = None


class GetMembersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetRequestsFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetSettingsResponseModel(BaseResponse):
    access: Optional["GroupsGroupAccess"] = None
    address: Optional[str] = None
    audio: Optional["GroupsGroupAudio"] = None
    articles: Optional[int] = None
    city_id: Optional[int] = None
    contacts: Optional["BaseBoolInt"] = None
    links: Optional["BaseBoolInt"] = None
    sections_list: Optional[typing.Dict[Any, Any]] = None
    main_section: Optional["GroupsGroupFullMainSection"] = None
    secondary_section: Optional[int] = None
    age_limits: Optional[int] = None
    country_id: Optional[int] = None
    description: Optional[str] = None
    docs: Optional["GroupsGroupDocs"] = None
    events: Optional["BaseBoolInt"] = None
    obscene_filter: Optional["BaseBoolInt"] = None
    obscene_stopwords: Optional["BaseBoolInt"] = None
    obscene_words: Optional[List[str]] = None
    event_group_id: Optional[int] = None
    photos: Optional[int] = None
    public_category: Optional[int] = None
    public_category_list: Optional[List["GroupsGroupPublicCategoryList"]] = None
    public_date: Optional[str] = None
    public_date_label: Optional[str] = None
    public_subcategory: Optional[int] = None
    rss: Optional[str] = None
    start_date: Optional[int] = None
    finish_date: Optional[int] = None
    subject: Optional[int] = None
    subject_list: Optional[List["GroupsSubjectItem"]] = None
    suggested_privacy: Optional[int] = None
    title: Optional[str] = None
    topics: Optional["GroupsGroupTopics"] = None
    twitter: Optional["GroupsSettingsTwitter"] = None
    video: Optional["GroupsGroupVideo"] = None
    wall: Optional["GroupsGroupWall"] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    wiki: Optional["GroupsGroupWiki"] = None


class GetTokenPermissionsResponseModel(BaseResponse):
    mask: Optional[int] = None
    permissions: Optional[List["GroupsTokenPermissionSetting"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsGroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class IsMemberExtendedResponseModel(BaseResponse):
    member: Optional["BaseBoolInt"] = None
    invitation: Optional["BaseBoolInt"] = None
    can_invite: Optional["BaseBoolInt"] = None
    can_recall: Optional["BaseBoolInt"] = None
    request: Optional["BaseBoolInt"] = None


IsMemberResponseModel = Optional[BaseBoolInt]

IsMemberUserIdsExtendedResponseModel = List[GroupsMemberStatusFull]

IsMemberUserIdsResponseModel = List[GroupsMemberStatus]


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GroupsGroup"]] = None


AddAddressResponse.update_forward_refs()
AddCallbackServerResponse.update_forward_refs()
AddLinkResponse.update_forward_refs()
CreateResponse.update_forward_refs()
EditAddressResponse.update_forward_refs()
GetAddressesResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCallbackConfirmationCodeResponse.update_forward_refs()
GetCallbackServersResponse.update_forward_refs()
GetCallbackSettingsResponse.update_forward_refs()
GetCatalogInfoExtendedResponse.update_forward_refs()
GetCatalogInfoResponse.update_forward_refs()
GetCatalogResponse.update_forward_refs()
GetInvitedUsersResponse.update_forward_refs()
GetInvitesExtendedResponse.update_forward_refs()
GetInvitesResponse.update_forward_refs()
GetLongPollServerResponse.update_forward_refs()
GetLongPollSettingsResponse.update_forward_refs()
GetMembersFieldsResponse.update_forward_refs()
GetMembersFilterResponse.update_forward_refs()
GetMembersResponse.update_forward_refs()
GetRequestsFieldsResponse.update_forward_refs()
GetRequestsResponse.update_forward_refs()
GetSettingsResponse.update_forward_refs()
GetTokenPermissionsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
IsMemberExtendedResponse.update_forward_refs()
IsMemberResponse.update_forward_refs()
IsMemberUserIdsExtendedResponse.update_forward_refs()
IsMemberUserIdsResponse.update_forward_refs()
SearchResponse.update_forward_refs()
