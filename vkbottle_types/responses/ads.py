import inspect
import typing
from .base_response import BaseResponse
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
    AdsTargSettings,
    AdsTargStats,
    AdsTargSuggestions,
    AdsTargSuggestionsCities,
    AdsTargSuggestionsRegions,
    AdsTargSuggestionsSchools,
    AdsTargetGroup,
    AdsUpdateOfficeUsersResult,
    AdsUsers
)


class AddOfficeUsersResponse(BaseResponse):
    response: bool = None


class CheckLinkResponse(BaseResponse):
    response: AdsLinkStatus = None


class CreateAdsResponse(BaseResponse):
    response: typing.List[int] = None


class CreateCampaignsResponse(BaseResponse):
    response: typing.List[int] = None


class CreateClientsResponse(BaseResponse):
    response: typing.List[int] = None


class CreateTargetGroupResponse(BaseResponse):
    response: "CreateTargetGroupResponseModel" = None


class DeleteAdsResponse(BaseResponse):
    response: typing.List[int] = None


class DeleteCampaignsResponse(BaseResponse):
    response: int = None


class DeleteClientsResponse(BaseResponse):
    response: int = None


class GetAccountsResponse(BaseResponse):
    response: typing.List["AdsAccount"] = None


class GetAdsLayoutResponse(BaseResponse):
    response: typing.List["AdsAdLayout"] = None


class GetAdsTargetingResponse(BaseResponse):
    response: typing.List["AdsTargSettings"] = None


class GetAdsResponse(BaseResponse):
    response: typing.List["AdsAd"] = None


class GetBudgetResponse(BaseResponse):
    response: int = None


class GetCampaignsResponse(BaseResponse):
    response: typing.List["AdsCampaign"] = None


class GetCategoriesResponse(BaseResponse):
    response: "GetCategoriesResponseModel" = None


class GetClientsResponse(BaseResponse):
    response: typing.List["AdsClient"] = None


class GetDemographicsResponse(BaseResponse):
    response: typing.List["AdsDemoStats"] = None


class GetFloodStatsResponse(BaseResponse):
    response: AdsFloodStats = None


class GetLookalikeRequestsResponse(BaseResponse):
    response: "GetLookalikeRequestsResponseModel" = None


class GetMusiciansResponse(BaseResponse):
    response: "GetMusiciansResponseModel" = None


class GetOfficeUsersResponse(BaseResponse):
    response: typing.List["AdsUsers"] = None


class GetPostsReachResponse(BaseResponse):
    response: typing.List["AdsPromotedPostReach"] = None


class GetRejectionReasonResponse(BaseResponse):
    response: AdsRejectReason = None


class GetStatisticsResponse(BaseResponse):
    response: typing.List["AdsStats"] = None


class GetSuggestionsCitiesResponse(BaseResponse):
    response: typing.List["AdsTargSuggestionsCities"] = None


class GetSuggestionsRegionsResponse(BaseResponse):
    response: typing.List["AdsTargSuggestionsRegions"] = None


class GetSuggestionsResponse(BaseResponse):
    response: typing.List["AdsTargSuggestions"] = None


class GetSuggestionsSchoolsResponse(BaseResponse):
    response: typing.List["AdsTargSuggestionsSchools"] = None


class GetTargetGroupsResponse(BaseResponse):
    response: typing.List["AdsTargetGroup"] = None


class GetTargetingStatsResponse(BaseResponse):
    response: AdsTargStats = None


class GetUploadURLResponse(BaseResponse):
    response: str = None


class GetVideoUploadURLResponse(BaseResponse):
    response: str = None


class ImportTargetContactsResponse(BaseResponse):
    response: int = None


class RemoveOfficeUsersResponse(BaseResponse):
    response: bool = None


class UpdateAdsResponse(BaseResponse):
    response: typing.List[int] = None


class UpdateCampaignsResponse(BaseResponse):
    response: int = None


class UpdateClientsResponse(BaseResponse):
    response: int = None


class UpdateOfficeUsersResponse(BaseResponse):
    response: typing.List["AdsUpdateOfficeUsersResult"] = None


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


for item in locals().copy().values():
    if inspect.isclass(item) and issubclass(item, BaseResponse):
        item.update_forward_refs()
