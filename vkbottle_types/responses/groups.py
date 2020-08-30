from .base_response import BaseResponse
from vkbottle_types.objects import users, base, groups
from typing import Optional, Any, List, Union
import typing


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


AddAddressResponseModel = Optional["groups.Address"]


class AddCallbackServerResponseModel(BaseResponse):
    server_id: Optional[int] = None


AddLinkResponseModel = Optional["groups.GroupLink"]


CreateResponseModel = Optional["groups.Group"]


EditAddressResponseModel = Optional["groups.Address"]


class GetAddressesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.Address"]] = None


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.BannedItem"]] = None


GetByIdResponseModel = List["groups.GroupFull"]


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
    code: Optional[str] = None


class GetCallbackServersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.CallbackServer"]] = None


GetCallbackSettingsResponseModel = Optional["groups.CallbackSettings"]


class GetCatalogInfoExtendedResponseModel(BaseResponse):
    enabled: Optional[int] = None
    categories: Optional[List["groups.GroupCategoryFull"]] = None


class GetCatalogInfoResponseModel(BaseResponse):
    enabled: Optional[int] = None
    categories: Optional[List["groups.GroupCategory"]] = None


class GetCatalogResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.Group"]] = None


class GetInvitedUsersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["users.UserFull"]] = None


class GetInvitesExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.GroupXtrInvitedBy"]] = None
    profiles: Optional[List["users.UserMin"]] = None
    groups: Optional[List["groups.GroupFull"]] = None


class GetInvitesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.GroupXtrInvitedBy"]] = None


GetLongPollServerResponseModel = Optional["groups.LongPollServer"]


GetLongPollSettingsResponseModel = Optional["groups.LongPollSettings"]


class GetMembersFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.UserXtrRole"]] = None


class GetMembersFilterResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.MemberRole"]] = None


class GetMembersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetRequestsFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["users.UserFull"]] = None


class GetRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetSettingsResponseModel(BaseResponse):
    access: Optional["groups.GroupAccess"] = None
    address: Optional[str] = None
    audio: Optional["groups.GroupAudio"] = None
    articles: Optional[int] = None
    city_id: Optional[int] = None
    contacts: Optional["base.BoolInt"] = None
    links: Optional["base.BoolInt"] = None
    sections_list: Optional[typing.Dict[Any, Any]] = None
    main_section: Optional["groups.GroupFullMainSection"] = None
    secondary_section: Optional[int] = None
    age_limits: Optional[int] = None
    country_id: Optional[int] = None
    description: Optional[str] = None
    docs: Optional["groups.GroupDocs"] = None
    events: Optional["base.BoolInt"] = None
    obscene_filter: Optional["base.BoolInt"] = None
    obscene_stopwords: Optional["base.BoolInt"] = None
    obscene_words: Optional[List[str]] = None
    event_group_id: Optional[int] = None
    photos: Optional[int] = None
    public_category: Optional[int] = None
    public_category_list: Optional[List["groups.GroupPublicCategoryList"]] = None
    public_date: Optional[str] = None
    public_date_label: Optional[str] = None
    public_subcategory: Optional[int] = None
    rss: Optional[str] = None
    start_date: Optional[int] = None
    finish_date: Optional[int] = None
    subject: Optional[int] = None
    subject_list: Optional[List["groups.SubjectItem"]] = None
    suggested_privacy: Optional[int] = None
    title: Optional[str] = None
    topics: Optional["groups.GroupTopics"] = None
    twitter: Optional["groups.SettingsTwitter"] = None
    video: Optional["groups.GroupVideo"] = None
    wall: Optional["groups.GroupWall"] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    wiki: Optional["groups.GroupWiki"] = None


class GetTokenPermissionsResponseModel(BaseResponse):
    mask: Optional[int] = None
    permissions: Optional[List["groups.TokenPermissionSetting"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.GroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class IsMemberExtendedResponseModel(BaseResponse):
    member: Optional["base.BoolInt"] = None
    invitation: Optional["base.BoolInt"] = None
    can_invite: Optional["base.BoolInt"] = None
    can_recall: Optional["base.BoolInt"] = None
    request: Optional["base.BoolInt"] = None


IsMemberResponseModel = Optional["base.BoolInt"]


IsMemberUserIdsExtendedResponseModel = List["groups.MemberStatusFull"]


IsMemberUserIdsResponseModel = List["groups.MemberStatus"]


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["groups.Group"]] = None
