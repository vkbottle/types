from .base_response import BaseResponse
from vkbottle_types.objects import ads
from typing import Optional, Any, List, Union
import typing


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


CheckLinkResponseModel = Optional["ads.LinkStatus"]


CreateAdsResponseModel = List[int]


CreateCampaignsResponseModel = List[int]


CreateClientsResponseModel = List[int]


class CreateTargetGroupResponseModel(BaseResponse):
    id: Optional[int] = None
    pixel: Optional[str] = None


DeleteAdsResponseModel = List[int]


DeleteCampaignsResponseModel = int


DeleteClientsResponseModel = int


GetAccountsResponseModel = List["ads.Account"]


GetAdsLayoutResponseModel = List["ads.AdLayout"]


GetAdsTargetingResponseModel = List["ads.TargSettings"]


GetAdsResponseModel = List["ads.Ad"]


GetBudgetResponseModel = int


GetCampaignsResponseModel = List["ads.Campaign"]


class GetCategoriesResponseModel(BaseResponse):
    v1: Optional[List["ads.Category"]] = None
    v2: Optional[List["ads.Category"]] = None


GetClientsResponseModel = List["ads.Client"]


GetDemographicsResponseModel = List["ads.DemoStats"]


GetFloodStatsResponseModel = Optional["ads.FloodStats"]


class GetLookalikeRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["ads.LookalikeRequest"]] = None


class GetMusiciansResponseModel(BaseResponse):
    items: Optional[List["ads.Musician"]] = None


GetOfficeUsersResponseModel = List["ads.Users"]


GetPostsReachResponseModel = List["ads.PromotedPostReach"]


GetRejectionReasonResponseModel = Optional["ads.RejectReason"]


GetStatisticsResponseModel = List["ads.Stats"]


GetSuggestionsCitiesResponseModel = List["ads.TargSuggestionsCities"]


GetSuggestionsRegionsResponseModel = List["ads.TargSuggestionsRegions"]


GetSuggestionsResponseModel = List["ads.TargSuggestions"]


GetSuggestionsSchoolsResponseModel = List["ads.TargSuggestionsSchools"]


GetTargetGroupsResponseModel = List["ads.TargetGroup"]


GetTargetingStatsResponseModel = Optional["ads.TargStats"]


GetUploadURLResponseModel = str


GetVideoUploadURLResponseModel = str


ImportTargetContactsResponseModel = int


RemoveOfficeUsersResponseModel = bool


UpdateAdsResponseModel = List[int]


UpdateCampaignsResponseModel = int


UpdateClientsResponseModel = int
