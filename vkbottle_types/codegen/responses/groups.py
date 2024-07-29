import typing

from vkbottle_types.base_model import Field
from vkbottle_types.objects import (
    GroupsAddress,
    GroupsCallbackSettings,
    GroupsGroupFull,
    GroupsGroupTag,
    GroupsLinksItem,
    GroupsLongPollServer,
    GroupsLongPollSettings,
    GroupsMemberStatus,
    GroupsMemberStatusFull,
)
from vkbottle_types.responses.base_response import BaseResponse


class GroupsAddAddressResponse(BaseResponse):
    response: "GroupsAddress" = Field()


class GroupsAddCallbackServerResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsAddLinkResponse(BaseResponse):
    response: "GroupsLinksItem" = Field()


class GroupsCreateResponse(BaseResponse):
    response: "GroupsGroupFull" = Field()


class GroupsEditAddressResponse(BaseResponse):
    response: "GroupsAddress" = Field()


class GroupsGetAddressesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetBannedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetByIdObjectResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetCallbackConfirmationCodeResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetCallbackServersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetCallbackSettingsResponse(BaseResponse):
    response: "GroupsCallbackSettings" = Field()


class GroupsGetCatalogInfoExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetCatalogInfoResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetInvitedUsersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetInvitesExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetInvitesResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetLongPollServerResponse(BaseResponse):
    response: "GroupsLongPollServer" = Field()


class GroupsGetLongPollSettingsResponse(BaseResponse):
    response: "GroupsLongPollSettings" = Field()


class GroupsGetMembersFieldsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetMembersFilterResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetMembersResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetOnlineStatusResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetRequestsFieldsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetRequestsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetSettingsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetTagListResponse(BaseResponse):
    response: typing.List[GroupsGroupTag] = Field()


class GroupsGetTokenPermissionsResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetObjectExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsGetResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsInviteUserIdsListResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsIsMemberExtendedResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()


class GroupsIsMemberUserIdsExtendedResponse(BaseResponse):
    response: typing.List[GroupsMemberStatusFull] = Field()


class GroupsIsMemberUserIdsResponse(BaseResponse):
    response: typing.List[GroupsMemberStatus] = Field()


class GroupsSearchResponse(BaseResponse):
    response: typing.Dict[str, typing.Any] = Field()
