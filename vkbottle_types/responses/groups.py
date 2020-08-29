import typing
from typing import Optional

from vkbottle_types.objects import users, base, groups
from .base_response import BaseResponse


class AddAddressResponse(BaseResponse):
    response: Optional[typing.List["groups.Address"]] = None


class AddCallbackServerResponse(BaseResponse):
    response: Optional["AddCallbackServerResponseModel"] = None


class AddLinkResponse(BaseResponse):
    response: Optional[typing.List["groups.GroupLink"]] = None


class CreateResponse(BaseResponse):
    response: Optional[typing.List["groups.Group"]] = None


class EditAddressResponse(BaseResponse):
    response: Optional[typing.List["groups.Address"]] = None


class GetAddressesResponse(BaseResponse):
    response: Optional["GetAddressesResponseModel"] = None


class GetBannedResponse(BaseResponse):
    response: Optional["GetBannedResponseModel"] = None


class GetByIdResponse(BaseResponse):
    response: Optional[typing.List["groups.GroupFull"]] = None


class GetCallbackConfirmationCodeResponse(BaseResponse):
    response: Optional["GetCallbackConfirmationCodeResponseModel"] = None


class GetCallbackServersResponse(BaseResponse):
    response: Optional["GetCallbackServersResponseModel"] = None


class GetCallbackSettingsResponse(BaseResponse):
    response: Optional[typing.List["groups.CallbackSettings"]] = None


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
    response: Optional[typing.List["groups.LongPollServer"]] = None


class GetLongPollSettingsResponse(BaseResponse):
    response: Optional[typing.List["groups.LongPollSettings"]] = None


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
    response: Optional[typing.List["base.BoolInt"]] = None


class IsMemberUserIdsExtendedResponse(BaseResponse):
    response: Optional[typing.List["groups.MemberStatusFull"]] = None


class IsMemberUserIdsResponse(BaseResponse):
    response: Optional[typing.List["groups.MemberStatus"]] = None


class SearchResponse(BaseResponse):
    response: Optional["SearchResponseModel"] = None


class AddCallbackServerResponseModel(BaseResponse):
    server_id: Optional[int] = None


class GetAddressesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.Address"]] = None


class GetBannedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.BannedItem"]] = None


class GetCallbackConfirmationCodeResponseModel(BaseResponse):
    code: Optional[str] = None


class GetCallbackServersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.CallbackServer"]] = None


class GetCatalogInfoExtendedResponseModel(BaseResponse):
    enabled: Optional[int] = None
    categories: Optional[typing.List["groups.GroupCategoryFull"]] = None


class GetCatalogInfoResponseModel(BaseResponse):
    enabled: Optional[int] = None
    categories: Optional[typing.List["groups.GroupCategory"]] = None


class GetCatalogResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.Group"]] = None


class GetInvitedUsersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None


class GetInvitesExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.GroupXtrInvitedBy"]] = None
    profiles: Optional[typing.List["users.UserMin"]] = None
    groups: Optional[typing.List["groups.GroupFull"]] = None


class GetInvitesResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.GroupXtrInvitedBy"]] = None


class GetMembersFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.UserXtrRole"]] = None


class GetMembersFilterResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.MemberRole"]] = None


class GetMembersResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class GetRequestsFieldsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["users.UserFull"]] = None


class GetRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class GetSettingsResponseModel(BaseResponse):
    access: Optional[typing.List["groups.GroupAccess"]] = None
    address: Optional[str] = None
    audio: Optional[typing.List["groups.GroupAudio"]] = None
    articles: Optional[int] = None
    city_id: Optional[int] = None
    contacts: Optional[typing.List["base.BoolInt"]] = None
    links: Optional[typing.List["base.BoolInt"]] = None
    sections_list: Optional["GetSettingsResponseModelModel"] = None
    main_section: Optional[typing.List["groups.GroupFullMainSection"]] = None
    secondary_section: Optional[int] = None
    age_limits: Optional[int] = None
    country_id: Optional[int] = None
    description: Optional[str] = None
    docs: Optional[typing.List["groups.GroupDocs"]] = None
    events: Optional[typing.List["base.BoolInt"]] = None
    obscene_filter: Optional[typing.List["base.BoolInt"]] = None
    obscene_stopwords: Optional[typing.List["base.BoolInt"]] = None
    obscene_words: Optional[typing.List[str]] = None
    event_group_id: Optional[int] = None
    photos: Optional[int] = None
    public_category: Optional[int] = None
    public_category_list: Optional[typing.List["groups.GroupPublicCategoryList"]] = None
    public_date: Optional[str] = None
    public_date_label: Optional[str] = None
    public_subcategory: Optional[int] = None
    rss: Optional[str] = None
    start_date: Optional[int] = None
    finish_date: Optional[int] = None
    subject: Optional[int] = None
    subject_list: Optional[typing.List["groups.SubjectItem"]] = None
    suggested_privacy: Optional[int] = None
    title: Optional[str] = None
    topics: Optional[typing.List["groups.GroupTopics"]] = None
    twitter: Optional[typing.List["groups.SettingsTwitter"]] = None
    video: Optional[typing.List["groups.GroupVideo"]] = None
    wall: Optional[typing.List["groups.GroupWall"]] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    wiki: Optional[typing.List["groups.GroupWiki"]] = None


class GetTokenPermissionsResponseModel(BaseResponse):
    mask: Optional[int] = None
    permissions: Optional[typing.List["groups.TokenPermissionSetting"]] = None


class GetExtendedResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.GroupFull"]] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List[int]] = None


class IsMemberExtendedResponseModel(BaseResponse):
    member: Optional[typing.List["base.BoolInt"]] = None
    invitation: Optional[typing.List["base.BoolInt"]] = None
    can_invite: Optional[typing.List["base.BoolInt"]] = None
    can_recall: Optional[typing.List["base.BoolInt"]] = None
    request: Optional[typing.List["base.BoolInt"]] = None


class SearchResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["groups.Group"]] = None

    items: Optional[dict] = None
