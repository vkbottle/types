from typing import List, Optional

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
    AdsUsers,
)

from .base_response import BaseResponse


class AddOfficeUsersResponse(BaseResponse):
    response: Optional["AddOfficeUsersResponseModel"] = None


class CheckLinkResponse(BaseResponse):
    response: Optional["CheckLinkResponseModel"] = None


class CreateAdsResponse(BaseResponse):
    response: Optional["CreateAdsResponseModel"] = None


class CreateCampaignsResponse(BaseResponse):
    response: Optional["CreateCampaignsResponseModel"] = None


class CreateClientsResponse(BaseResponse):
    response: Optional["CreateClientsResponseModel"] = None


class CreateTargetGroupResponse(BaseResponse):
    response: Optional["CreateTargetGroupResponseModel"] = None


class DeleteAdsResponse(BaseResponse):
    response: Optional["DeleteAdsResponseModel"] = None


class DeleteCampaignsResponse(BaseResponse):
    response: Optional["DeleteCampaignsResponseModel"] = None


class DeleteClientsResponse(BaseResponse):
    response: Optional["DeleteClientsResponseModel"] = None


class GetAccountsResponse(BaseResponse):
    response: Optional["GetAccountsResponseModel"] = None


class GetAdsLayoutResponse(BaseResponse):
    response: Optional["GetAdsLayoutResponseModel"] = None


class GetAdsTargetingResponse(BaseResponse):
    response: Optional["GetAdsTargetingResponseModel"] = None


class GetAdsResponse(BaseResponse):
    response: Optional["GetAdsResponseModel"] = None


class GetBudgetResponse(BaseResponse):
    response: Optional["GetBudgetResponseModel"] = None


class GetCampaignsResponse(BaseResponse):
    response: Optional["GetCampaignsResponseModel"] = None


class GetCategoriesResponse(BaseResponse):
    response: Optional["GetCategoriesResponseModel"] = None


class GetClientsResponse(BaseResponse):
    response: Optional["GetClientsResponseModel"] = None


class GetDemographicsResponse(BaseResponse):
    response: Optional["GetDemographicsResponseModel"] = None


class GetFloodStatsResponse(BaseResponse):
    response: Optional["GetFloodStatsResponseModel"] = None


class GetLookalikeRequestsResponse(BaseResponse):
    response: Optional["GetLookalikeRequestsResponseModel"] = None


class GetMusiciansResponse(BaseResponse):
    response: Optional["GetMusiciansResponseModel"] = None


class GetOfficeUsersResponse(BaseResponse):
    response: Optional["GetOfficeUsersResponseModel"] = None


class GetPostsReachResponse(BaseResponse):
    response: Optional["GetPostsReachResponseModel"] = None


class GetRejectionReasonResponse(BaseResponse):
    response: Optional["GetRejectionReasonResponseModel"] = None


class GetStatisticsResponse(BaseResponse):
    response: Optional["GetStatisticsResponseModel"] = None


class GetSuggestionsCitiesResponse(BaseResponse):
    response: Optional["GetSuggestionsCitiesResponseModel"] = None


class GetSuggestionsRegionsResponse(BaseResponse):
    response: Optional["GetSuggestionsRegionsResponseModel"] = None


class GetSuggestionsResponse(BaseResponse):
    response: Optional["GetSuggestionsResponseModel"] = None


class GetSuggestionsSchoolsResponse(BaseResponse):
    response: Optional["GetSuggestionsSchoolsResponseModel"] = None


class GetTargetGroupsResponse(BaseResponse):
    response: Optional["GetTargetGroupsResponseModel"] = None


class GetTargetingStatsResponse(BaseResponse):
    response: Optional["GetTargetingStatsResponseModel"] = None


class GetUploadURLResponse(BaseResponse):
    response: Optional["GetUploadURLResponseModel"] = None


class GetVideoUploadURLResponse(BaseResponse):
    response: Optional["GetVideoUploadURLResponseModel"] = None


class ImportTargetContactsResponse(BaseResponse):
    response: Optional["ImportTargetContactsResponseModel"] = None


class RemoveOfficeUsersResponse(BaseResponse):
    response: Optional["RemoveOfficeUsersResponseModel"] = None


class UpdateAdsResponse(BaseResponse):
    response: Optional["UpdateAdsResponseModel"] = None


class UpdateCampaignsResponse(BaseResponse):
    response: Optional["UpdateCampaignsResponseModel"] = None


class UpdateClientsResponse(BaseResponse):
    response: Optional["UpdateClientsResponseModel"] = None


AddOfficeUsersResponseModel = bool

CheckLinkResponseModel = Optional[AdsLinkStatus]

CreateAdsResponseModel = List[int]

CreateCampaignsResponseModel = List[int]


CreateClientsResponseModel = List[int]


class CreateTargetGroupResponseModel(BaseResponse):
    id: Optional[int] = None
    pixel: Optional[str] = None


DeleteAdsResponseModel = List[int]


DeleteCampaignsResponseModel = int


DeleteClientsResponseModel = int

GetAccountsResponseModel = List[AdsAccount]

GetAdsLayoutResponseModel = List[AdsAdLayout]

GetAdsTargetingResponseModel = List[AdsTargSettings]

GetAdsResponseModel = List[AdsAd]


GetBudgetResponseModel = int

GetCampaignsResponseModel = List[AdsCampaign]


class GetCategoriesResponseModel(BaseResponse):
    v1: Optional[List["AdsCategory"]] = None
    v2: Optional[List["AdsCategory"]] = None


GetClientsResponseModel = List[AdsClient]

GetDemographicsResponseModel = List[AdsDemoStats]

GetFloodStatsResponseModel = Optional[AdsFloodStats]


class GetLookalikeRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["AdsLookalikeRequest"]] = None


class GetMusiciansResponseModel(BaseResponse):
    items: Optional[List["AdsMusician"]] = None


GetOfficeUsersResponseModel = List[AdsUsers]

GetPostsReachResponseModel = List[AdsPromotedPostReach]

GetRejectionReasonResponseModel = Optional[AdsRejectReason]

GetStatisticsResponseModel = List[AdsStats]

GetSuggestionsCitiesResponseModel = List[AdsTargSuggestionsCities]

GetSuggestionsRegionsResponseModel = List[AdsTargSuggestionsRegions]

GetSuggestionsResponseModel = List[AdsTargSuggestions]

GetSuggestionsSchoolsResponseModel = List[AdsTargSuggestionsSchools]

GetTargetGroupsResponseModel = List[AdsTargetGroup]

GetTargetingStatsResponseModel = Optional[AdsTargStats]


GetUploadURLResponseModel = str


GetVideoUploadURLResponseModel = str


ImportTargetContactsResponseModel = int


RemoveOfficeUsersResponseModel = bool


UpdateAdsResponseModel = List[int]


UpdateCampaignsResponseModel = int


UpdateClientsResponseModel = int

AddOfficeUsersResponse.update_forward_refs()
CheckLinkResponse.update_forward_refs()
CreateAdsResponse.update_forward_refs()
CreateCampaignsResponse.update_forward_refs()
CreateClientsResponse.update_forward_refs()
CreateTargetGroupResponse.update_forward_refs()
DeleteAdsResponse.update_forward_refs()
DeleteCampaignsResponse.update_forward_refs()
DeleteClientsResponse.update_forward_refs()
GetAccountsResponse.update_forward_refs()
GetAdsLayoutResponse.update_forward_refs()
GetAdsTargetingResponse.update_forward_refs()
GetAdsResponse.update_forward_refs()
GetBudgetResponse.update_forward_refs()
GetCampaignsResponse.update_forward_refs()
GetCategoriesResponse.update_forward_refs()
GetClientsResponse.update_forward_refs()
GetDemographicsResponse.update_forward_refs()
GetFloodStatsResponse.update_forward_refs()
GetLookalikeRequestsResponse.update_forward_refs()
GetMusiciansResponse.update_forward_refs()
GetOfficeUsersResponse.update_forward_refs()
GetPostsReachResponse.update_forward_refs()
GetRejectionReasonResponse.update_forward_refs()
GetStatisticsResponse.update_forward_refs()
GetSuggestionsCitiesResponse.update_forward_refs()
GetSuggestionsRegionsResponse.update_forward_refs()
GetSuggestionsResponse.update_forward_refs()
GetSuggestionsSchoolsResponse.update_forward_refs()
GetTargetGroupsResponse.update_forward_refs()
GetTargetingStatsResponse.update_forward_refs()
GetUploadURLResponse.update_forward_refs()
GetVideoUploadURLResponse.update_forward_refs()
ImportTargetContactsResponse.update_forward_refs()
RemoveOfficeUsersResponse.update_forward_refs()
UpdateAdsResponse.update_forward_refs()
UpdateCampaignsResponse.update_forward_refs()
UpdateClientsResponse.update_forward_refs()
