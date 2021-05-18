import inspect
import typing

from vkbottle_types.objects import (
    AdsAccount,
    AdsAd,
    AdsAdLayout,
    AdsCampaign,
    AdsCategory,
    AdsClient,
    AdsDemoStats,
    AdsFloodStats,
    AdsLinkStatus,
    AdsLookalikeRequest,
    AdsMusician,
    AdsPromotedPostReach,
    AdsRejectReason,
    AdsStats,
    AdsTargetGroup,
    AdsTargSettings,
    AdsTargStats,
    AdsTargSuggestions,
    AdsTargSuggestionsCities,
    AdsTargSuggestionsRegions,
    AdsTargSuggestionsSchools,
    AdsUpdateofficeusersResult,
    AdsUsers,
)

from .base_response import BaseResponse


class AddOfficeUsersResponse(BaseResponse):
    response: typing.Optional["AddOfficeUsersResponseModel"] = None


class CheckLinkResponse(BaseResponse):
    response: typing.Optional["CheckLinkResponseModel"] = None


class CreateAdsResponse(BaseResponse):
    response: typing.Optional["CreateAdsResponseModel"] = None


class CreateCampaignsResponse(BaseResponse):
    response: typing.Optional["CreateCampaignsResponseModel"] = None


class CreateClientsResponse(BaseResponse):
    response: typing.Optional["CreateClientsResponseModel"] = None


class CreateTargetGroupResponse(BaseResponse):
    response: typing.Optional["CreateTargetGroupResponseModel"] = None


class DeleteAdsResponse(BaseResponse):
    response: typing.Optional["DeleteAdsResponseModel"] = None


class DeleteCampaignsResponse(BaseResponse):
    response: typing.Optional["DeleteCampaignsResponseModel"] = None


class DeleteClientsResponse(BaseResponse):
    response: typing.Optional["DeleteClientsResponseModel"] = None


class GetAccountsResponse(BaseResponse):
    response: typing.Optional["GetAccountsResponseModel"] = None


class GetAdsLayoutResponse(BaseResponse):
    response: typing.Optional["GetAdsLayoutResponseModel"] = None


class GetAdsTargetingResponse(BaseResponse):
    response: typing.Optional["GetAdsTargetingResponseModel"] = None


class GetAdsResponse(BaseResponse):
    response: typing.Optional["GetAdsResponseModel"] = None


class GetBudgetResponse(BaseResponse):
    response: typing.Optional["GetBudgetResponseModel"] = None


class GetCampaignsResponse(BaseResponse):
    response: typing.Optional["GetCampaignsResponseModel"] = None


class GetCategoriesResponse(BaseResponse):
    response: typing.Optional["GetCategoriesResponseModel"] = None


class GetClientsResponse(BaseResponse):
    response: typing.Optional["GetClientsResponseModel"] = None


class GetDemographicsResponse(BaseResponse):
    response: typing.Optional["GetDemographicsResponseModel"] = None


class GetFloodStatsResponse(BaseResponse):
    response: typing.Optional["GetFloodStatsResponseModel"] = None


class GetLookalikeRequestsResponse(BaseResponse):
    response: typing.Optional["GetLookalikeRequestsResponseModel"] = None


class GetMusiciansResponse(BaseResponse):
    response: typing.Optional["GetMusiciansResponseModel"] = None


class GetOfficeUsersResponse(BaseResponse):
    response: typing.Optional["GetOfficeUsersResponseModel"] = None


class GetPostsReachResponse(BaseResponse):
    response: typing.Optional["GetPostsReachResponseModel"] = None


class GetRejectionReasonResponse(BaseResponse):
    response: typing.Optional["GetRejectionReasonResponseModel"] = None


class GetStatisticsResponse(BaseResponse):
    response: typing.Optional["GetStatisticsResponseModel"] = None


class GetSuggestionsCitiesResponse(BaseResponse):
    response: typing.Optional["GetSuggestionsCitiesResponseModel"] = None


class GetSuggestionsRegionsResponse(BaseResponse):
    response: typing.Optional["GetSuggestionsRegionsResponseModel"] = None


class GetSuggestionsResponse(BaseResponse):
    response: typing.Optional["GetSuggestionsResponseModel"] = None


class GetSuggestionsSchoolsResponse(BaseResponse):
    response: typing.Optional["GetSuggestionsSchoolsResponseModel"] = None


class GetTargetGroupsResponse(BaseResponse):
    response: typing.Optional["GetTargetGroupsResponseModel"] = None


class GetTargetingStatsResponse(BaseResponse):
    response: typing.Optional["GetTargetingStatsResponseModel"] = None


class GetUploadURLResponse(BaseResponse):
    response: typing.Optional["GetUploadURLResponseModel"] = None


class GetVideoUploadURLResponse(BaseResponse):
    response: typing.Optional["GetVideoUploadURLResponseModel"] = None


class ImportTargetContactsResponse(BaseResponse):
    response: typing.Optional["ImportTargetContactsResponseModel"] = None


class RemoveOfficeUsersResponse(BaseResponse):
    response: typing.Optional["RemoveOfficeUsersResponseModel"] = None


class UpdateAdsResponse(BaseResponse):
    response: typing.Optional["UpdateAdsResponseModel"] = None


class UpdateCampaignsResponse(BaseResponse):
    response: typing.Optional["UpdateCampaignsResponseModel"] = None


class UpdateClientsResponse(BaseResponse):
    response: typing.Optional["UpdateClientsResponseModel"] = None


class UpdateOfficeUsersResponse(BaseResponse):
    response: typing.Optional["UpdateOfficeUsersResponseModel"] = None


AddOfficeUsersResponseModel = bool


CheckLinkResponseModel = AdsLinkStatus


CreateAdsResponseModel = typing.List[int]


CreateCampaignsResponseModel = typing.List[int]


CreateClientsResponseModel = typing.List[int]


class CreateTargetGroupResponseModel(BaseResponse):
    id: typing.Optional[int] = None
    pixel: typing.Optional[str] = None


DeleteAdsResponseModel = typing.List[int]


DeleteCampaignsResponseModel = int


DeleteClientsResponseModel = int


GetAccountsResponseModel = typing.List[AdsAccount]


GetAdsLayoutResponseModel = typing.List[AdsAdLayout]


GetAdsTargetingResponseModel = typing.List[AdsTargSettings]


GetAdsResponseModel = typing.List[AdsAd]


GetBudgetResponseModel = int


GetCampaignsResponseModel = typing.List[AdsCampaign]


class GetCategoriesResponseModel(BaseResponse):
    v1: typing.Optional[typing.List["AdsCategory"]] = None
    v2: typing.Optional[typing.List["AdsCategory"]] = None


GetClientsResponseModel = typing.List[AdsClient]


GetDemographicsResponseModel = typing.List[AdsDemoStats]


GetFloodStatsResponseModel = AdsFloodStats


class GetLookalikeRequestsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AdsLookalikeRequest"]] = None


class GetMusiciansResponseModel(BaseResponse):
    items: typing.Optional[typing.List["AdsMusician"]] = None


GetOfficeUsersResponseModel = typing.List[AdsUsers]


GetPostsReachResponseModel = typing.List[AdsPromotedPostReach]


GetRejectionReasonResponseModel = AdsRejectReason


GetStatisticsResponseModel = typing.List[AdsStats]


GetSuggestionsCitiesResponseModel = typing.List[AdsTargSuggestionsCities]


GetSuggestionsRegionsResponseModel = typing.List[AdsTargSuggestionsRegions]


GetSuggestionsResponseModel = typing.List[AdsTargSuggestions]


GetSuggestionsSchoolsResponseModel = typing.List[AdsTargSuggestionsSchools]


GetTargetGroupsResponseModel = typing.List[AdsTargetGroup]


GetTargetingStatsResponseModel = AdsTargStats


GetUploadURLResponseModel = str


GetVideoUploadURLResponseModel = str


ImportTargetContactsResponseModel = int


RemoveOfficeUsersResponseModel = bool


UpdateAdsResponseModel = typing.List[int]


UpdateCampaignsResponseModel = int


UpdateClientsResponseModel = int


UpdateOfficeUsersResponseModel = typing.List[AdsUpdateofficeusersResult]


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
