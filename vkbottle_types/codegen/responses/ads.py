import typing

from vkbottle_types.objects import (
    AdsAccount,
    AdsAd,
    AdsAdLayout,
    AdsCampaign,
    AdsCategory,
    AdsClient,
    AdsCreateAdStatus,
    AdsCreateCampaignStatus,
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
    AdsUpdateOfficeUsersResult,
    AdsUsers,
)
from vkbottle_types.responses.base_response import BaseResponse


class AddOfficeUsersResponse(BaseResponse):
    response: bool


class CheckLinkResponse(BaseResponse):
    response: AdsLinkStatus


class CreateAdsResponse(BaseResponse):
    response: typing.List["AdsCreateAdStatus"]


class CreateCampaignsResponse(BaseResponse):
    response: typing.List["AdsCreateCampaignStatus"]


class CreateClientsResponse(BaseResponse):
    response: typing.List[int]


class CreateTargetGroupResponse(BaseResponse):
    response: "CreateTargetGroupResponseModel"


class DeleteAdsResponse(BaseResponse):
    response: typing.List[int]


class DeleteCampaignsResponse(BaseResponse):
    response: typing.List[int]


class DeleteClientsResponse(BaseResponse):
    response: typing.List[int]


class GetAccountsResponse(BaseResponse):
    response: typing.List["AdsAccount"]


class GetAdsLayoutResponse(BaseResponse):
    response: typing.List["AdsAdLayout"]


class GetAdsTargetingResponse(BaseResponse):
    response: typing.List["AdsTargSettings"]


class GetAdsResponse(BaseResponse):
    response: typing.List["AdsAd"]


class GetBudgetResponse(BaseResponse):
    response: int


class GetCampaignsResponse(BaseResponse):
    response: typing.List["AdsCampaign"]


class GetCategoriesResponse(BaseResponse):
    response: "GetCategoriesResponseModel"


class GetClientsResponse(BaseResponse):
    response: typing.List["AdsClient"]


class GetDemographicsResponse(BaseResponse):
    response: typing.List["AdsDemoStats"]


class GetFloodStatsResponse(BaseResponse):
    response: AdsFloodStats


class GetLookalikeRequestsResponse(BaseResponse):
    response: "GetLookalikeRequestsResponseModel"


class GetMusiciansResponse(BaseResponse):
    response: "GetMusiciansResponseModel"


class GetOfficeUsersResponse(BaseResponse):
    response: typing.List["AdsUsers"]


class GetPostsReachResponse(BaseResponse):
    response: typing.List["AdsPromotedPostReach"]


class GetRejectionReasonResponse(BaseResponse):
    response: AdsRejectReason


class GetStatisticsResponse(BaseResponse):
    response: typing.List["AdsStats"]


class GetSuggestionsCitiesResponse(BaseResponse):
    response: typing.List["AdsTargSuggestionsCities"]


class GetSuggestionsRegionsResponse(BaseResponse):
    response: typing.List["AdsTargSuggestionsRegions"]


class GetSuggestionsResponse(BaseResponse):
    response: typing.List["AdsTargSuggestions"]


class GetSuggestionsSchoolsResponse(BaseResponse):
    response: typing.List["AdsTargSuggestionsSchools"]


class GetTargetGroupsResponse(BaseResponse):
    response: typing.List["AdsTargetGroup"]


class GetTargetingStatsResponse(BaseResponse):
    response: AdsTargStats


class GetUploadURLResponse(BaseResponse):
    response: str


class GetVideoUploadURLResponse(BaseResponse):
    response: str


class ImportTargetContactsResponse(BaseResponse):
    response: int


class RemoveOfficeUsersResponse(BaseResponse):
    response: bool


class UpdateAdsResponse(BaseResponse):
    response: typing.List[int]


class UpdateCampaignsResponse(BaseResponse):
    response: int


class UpdateClientsResponse(BaseResponse):
    response: int


class UpdateOfficeUsersResponse(BaseResponse):
    response: typing.List["AdsUpdateOfficeUsersResult"]


class CreateTargetGroupResponseModel(BaseResponse):
    id: typing.Optional[int] = None
    pixel: typing.Optional[str] = None


class GetCategoriesResponseModel(BaseResponse):
    v1: typing.Optional[typing.List["AdsCategory"]] = None
    v2: typing.Optional[typing.List["AdsCategory"]] = None


class GetLookalikeRequestsResponseModel(BaseResponse):
    count: typing.Optional[int] = None
    items: typing.Optional[typing.List["AdsLookalikeRequest"]] = None


class GetMusiciansResponseModel(BaseResponse):
    items: typing.Optional[typing.List["AdsMusician"]] = None


__all__ = (
    "AddOfficeUsersResponse",
    "AdsAccount",
    "AdsAd",
    "AdsAdLayout",
    "AdsCampaign",
    "AdsCategory",
    "AdsClient",
    "AdsCreateAdStatus",
    "AdsCreateCampaignStatus",
    "AdsDemoStats",
    "AdsFloodStats",
    "AdsLinkStatus",
    "AdsLookalikeRequest",
    "AdsMusician",
    "AdsPromotedPostReach",
    "AdsRejectReason",
    "AdsStats",
    "AdsTargSettings",
    "AdsTargStats",
    "AdsTargSuggestions",
    "AdsTargSuggestionsCities",
    "AdsTargSuggestionsRegions",
    "AdsTargSuggestionsSchools",
    "AdsTargetGroup",
    "AdsUpdateOfficeUsersResult",
    "AdsUsers",
    "CheckLinkResponse",
    "CreateAdsResponse",
    "CreateCampaignsResponse",
    "CreateClientsResponse",
    "CreateTargetGroupResponse",
    "CreateTargetGroupResponseModel",
    "DeleteAdsResponse",
    "DeleteCampaignsResponse",
    "DeleteClientsResponse",
    "GetAccountsResponse",
    "GetAdsLayoutResponse",
    "GetAdsResponse",
    "GetAdsTargetingResponse",
    "GetBudgetResponse",
    "GetCampaignsResponse",
    "GetCategoriesResponse",
    "GetCategoriesResponseModel",
    "GetClientsResponse",
    "GetDemographicsResponse",
    "GetFloodStatsResponse",
    "GetLookalikeRequestsResponse",
    "GetLookalikeRequestsResponseModel",
    "GetMusiciansResponse",
    "GetMusiciansResponseModel",
    "GetOfficeUsersResponse",
    "GetPostsReachResponse",
    "GetRejectionReasonResponse",
    "GetStatisticsResponse",
    "GetSuggestionsCitiesResponse",
    "GetSuggestionsRegionsResponse",
    "GetSuggestionsResponse",
    "GetSuggestionsSchoolsResponse",
    "GetTargetGroupsResponse",
    "GetTargetingStatsResponse",
    "GetUploadURLResponse",
    "GetVideoUploadURLResponse",
    "ImportTargetContactsResponse",
    "RemoveOfficeUsersResponse",
    "UpdateAdsResponse",
    "UpdateCampaignsResponse",
    "UpdateClientsResponse",
    "UpdateOfficeUsersResponse",
)
