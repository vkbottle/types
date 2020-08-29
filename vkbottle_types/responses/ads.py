import typing
from typing import Optional

from vkbottle_types.objects import ads
from .base_response import BaseResponse


class AddOfficeUsersResponse(BaseResponse):
    response: Optional[bool] = None


class CheckLinkResponse(BaseResponse):
    response: Optional[typing.List["ads.LinkStatus"]] = None


class CreateAdsResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class CreateCampaignsResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class CreateClientsResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class CreateTargetGroupResponse(BaseResponse):
    response: Optional["CreateTargetGroupResponseModel"] = None


class DeleteAdsResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class DeleteCampaignsResponse(BaseResponse):
    response: Optional[int] = None


class DeleteClientsResponse(BaseResponse):
    response: Optional[int] = None


class GetAccountsResponse(BaseResponse):
    response: Optional[typing.List["ads.Account"]] = None


class GetAdsLayoutResponse(BaseResponse):
    response: Optional[typing.List["ads.AdLayout"]] = None


class GetAdsTargetingResponse(BaseResponse):
    response: Optional[typing.List["ads.TargSettings"]] = None


class GetAdsResponse(BaseResponse):
    response: Optional[typing.List["ads.Ad"]] = None


class GetBudgetResponse(BaseResponse):
    response: Optional[int] = None


class GetCampaignsResponse(BaseResponse):
    response: Optional[typing.List["ads.Campaign"]] = None


class GetCategoriesResponse(BaseResponse):
    response: Optional["GetCategoriesResponseModel"] = None


class GetClientsResponse(BaseResponse):
    response: Optional[typing.List["ads.Client"]] = None


class GetDemographicsResponse(BaseResponse):
    response: Optional[typing.List["ads.DemoStats"]] = None


class GetFloodStatsResponse(BaseResponse):
    response: Optional[typing.List["ads.FloodStats"]] = None


class GetLookalikeRequestsResponse(BaseResponse):
    response: Optional["GetLookalikeRequestsResponseModel"] = None


class GetMusiciansResponse(BaseResponse):
    response: Optional["GetMusiciansResponseModel"] = None


class GetOfficeUsersResponse(BaseResponse):
    response: Optional[typing.List["ads.Users"]] = None


class GetPostsReachResponse(BaseResponse):
    response: Optional[typing.List["ads.PromotedPostReach"]] = None


class GetRejectionReasonResponse(BaseResponse):
    response: Optional[typing.List["ads.RejectReason"]] = None


class GetStatisticsResponse(BaseResponse):
    response: Optional[typing.List["ads.Stats"]] = None


class GetSuggestionsCitiesResponse(BaseResponse):
    response: Optional[typing.List["ads.TargSuggestionsCities"]] = None


class GetSuggestionsRegionsResponse(BaseResponse):
    response: Optional[typing.List["ads.TargSuggestionsRegions"]] = None


class GetSuggestionsResponse(BaseResponse):
    response: Optional[typing.List["ads.TargSuggestions"]] = None


class GetSuggestionsSchoolsResponse(BaseResponse):
    response: Optional[typing.List["ads.TargSuggestionsSchools"]] = None


class GetTargetGroupsResponse(BaseResponse):
    response: Optional[typing.List["ads.TargetGroup"]] = None


class GetTargetingStatsResponse(BaseResponse):
    response: Optional[typing.List["ads.TargStats"]] = None


class GetUploadURLResponse(BaseResponse):
    response: Optional[str] = None


class GetVideoUploadURLResponse(BaseResponse):
    response: Optional[str] = None


class ImportTargetContactsResponse(BaseResponse):
    response: Optional[int] = None


class RemoveOfficeUsersResponse(BaseResponse):
    response: Optional[bool] = None


class UpdateAdsResponse(BaseResponse):
    response: Optional[typing.List[int]] = None


class UpdateCampaignsResponse(BaseResponse):
    response: Optional[int] = None


class UpdateClientsResponse(BaseResponse):
    response: Optional[int] = None


class CreateTargetGroupResponseModel(BaseResponse):
    id: Optional[int] = None
    pixel: Optional[str] = None


class GetCategoriesResponseModel(BaseResponse):
    v1: Optional[typing.List["ads.Category"]] = None
    v2: Optional[typing.List["ads.Category"]] = None


class GetLookalikeRequestsResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[typing.List["ads.LookalikeRequest"]] = None


class GetMusiciansResponseModel(BaseResponse):
    items: Optional[typing.List["ads.Musician"]] = None
