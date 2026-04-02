from vkbottle_types.base_model import BaseModel, Field
from vkbottle_types.objects import (
    AdsAccount,
    AdsAd,
    AdsAdLayout,
    AdsCampaign,
    AdsCategory,
    AdsClient,
    AdsCreateAdStatus,
    AdsCreateCampaignStatus,
    AdsCreateClientsStatus,
    AdsDemoStats,
    AdsFloodStats,
    AdsLinkStatus,
    AdsLookalikeRequest,
    AdsMusician,
    AdsPromotedPostReach,
    AdsRejectReason,
    AdsStats,
    AdsTargetGroup,
    AdsTargetPixelInfo,
    AdsTargSettings,
    AdsTargStats,
    AdsTargSuggestions,
    AdsTargSuggestionsCities,
    AdsTargSuggestionsRegions,
    AdsTargSuggestionsSchools,
    AdsUpdateAdsStatus,
    AdsUpdateClientsStatus,
    AdsUpdateOfficeUsersResult,
    AdsUsers,
)
from vkbottle_types.responses.base_response import BaseResponse


class AdsAddOfficeUsersResponse(BaseResponse):
    response: list[bool] = Field()


class AdsCheckLinkResponse(BaseResponse):
    response: "AdsLinkStatus" = Field()


class AdsCreateAdsResponse(BaseResponse):
    response: list["AdsCreateAdStatus"] = Field()


class AdsCreateCampaignsResponse(BaseResponse):
    response: list["AdsCreateCampaignStatus"] = Field()


class AdsCreateClientsResponse(BaseResponse):
    response: list["AdsCreateClientsStatus"] = Field()


class AdsCreateLookalikeRequestResponseModel(BaseModel):
    request_id: int | None = Field(
        default=None,
    )


class AdsCreateLookalikeRequestResponse(BaseResponse):
    response: "AdsCreateLookalikeRequestResponseModel" = Field()


class AdsCreateTargetGroupResponseModel(BaseModel):
    id: int | None = Field(
        default=None,
    )
    pixel: str | None = Field(
        default=None,
    )


class AdsCreateTargetGroupResponse(BaseResponse):
    response: "AdsCreateTargetGroupResponseModel" = Field()


class AdsCreateTargetPixelResponseModel(BaseModel):
    id: int | None = Field(
        default=None,
    )
    pixel: str | None = Field(
        default=None,
    )


class AdsCreateTargetPixelResponse(BaseResponse):
    response: "AdsCreateTargetPixelResponseModel" = Field()


class AdsDeleteAdsResponse(BaseResponse):
    response: list[int] = Field()


class AdsDeleteCampaignsResponse(BaseResponse):
    response: list[int] = Field()


class AdsDeleteClientsResponse(BaseResponse):
    response: list[int] = Field()


class AdsGetAccountsResponse(BaseResponse):
    response: list["AdsAccount"] = Field()


class AdsGetAdsLayoutResponse(BaseResponse):
    response: list["AdsAdLayout"] = Field()


class AdsGetAdsTargetingResponse(BaseResponse):
    response: list["AdsTargSettings"] = Field()


class AdsGetAdsResponse(BaseResponse):
    response: list["AdsAd"] = Field()


class AdsGetBudgetResponse(BaseResponse):
    response: str = Field()


class AdsGetCampaignsResponse(BaseResponse):
    response: list["AdsCampaign"] = Field()


class AdsGetCategoriesResponseModel(BaseModel):
    v1: list["AdsCategory"] | None = Field(
        default=None,
    )
    v2: list["AdsCategory"] | None = Field(
        default=None,
    )


class AdsGetCategoriesResponse(BaseResponse):
    response: "AdsGetCategoriesResponseModel" = Field()


class AdsGetClientsResponse(BaseResponse):
    response: list["AdsClient"] = Field()


class AdsGetDemographicsResponse(BaseResponse):
    response: list["AdsDemoStats"] = Field()


class AdsGetFloodStatsResponse(BaseResponse):
    response: "AdsFloodStats" = Field()


class AdsGetLookalikeRequestsResponseModel(BaseModel):
    count: int = Field()
    items: list["AdsLookalikeRequest"] = Field()


class AdsGetLookalikeRequestsResponse(BaseResponse):
    response: "AdsGetLookalikeRequestsResponseModel" = Field()


class AdsGetMusiciansResponseModel(BaseModel):
    items: list["AdsMusician"] = Field()


class AdsGetMusiciansResponse(BaseResponse):
    response: "AdsGetMusiciansResponseModel" = Field()


class AdsGetOfficeUsersResponse(BaseResponse):
    response: list["AdsUsers"] = Field()


class AdsGetPostsReachResponse(BaseResponse):
    response: list["AdsPromotedPostReach"] = Field()


class AdsGetRejectionReasonResponse(BaseResponse):
    response: "AdsRejectReason" = Field()


class AdsGetStatisticsResponse(BaseResponse):
    response: list["AdsStats"] = Field()


class AdsGetSuggestionsCitiesResponse(BaseResponse):
    response: list["AdsTargSuggestionsCities"] = Field()


class AdsGetSuggestionsRegionsResponse(BaseResponse):
    response: list["AdsTargSuggestionsRegions"] = Field()


class AdsGetSuggestionsResponse(BaseResponse):
    response: list["AdsTargSuggestions"] = Field()


class AdsGetSuggestionsSchoolsResponse(BaseResponse):
    response: list["AdsTargSuggestionsSchools"] = Field()


class AdsGetTargetGroupsResponse(BaseResponse):
    response: list["AdsTargetGroup"] = Field()


class AdsGetTargetPixelsResponse(BaseResponse):
    response: list["AdsTargetPixelInfo"] = Field()


class AdsGetTargetingStatsResponse(BaseResponse):
    response: "AdsTargStats" = Field()


class AdsGetUploadURLResponse(BaseResponse):
    response: str = Field()


class AdsGetVideoUploadURLResponse(BaseResponse):
    response: str = Field()


class AdsImportTargetContactsResponse(BaseResponse):
    response: int = Field()


class AdsRemoveOfficeUsersResponse(BaseResponse):
    response: list[bool] = Field()


class AdsRemoveTargetContactsResponseModel(BaseModel):
    result: int = Field()


class AdsRemoveTargetContactsResponse(BaseResponse):
    response: "AdsRemoveTargetContactsResponseModel" = Field()


class AdsSaveLookalikeRequestResultResponseModel(BaseModel):
    retargeting_group_id: int = Field()
    audience_count: int = Field()


class AdsSaveLookalikeRequestResultResponse(BaseResponse):
    response: "AdsSaveLookalikeRequestResultResponseModel" = Field()


class AdsShareTargetGroupResponseModel(BaseModel):
    id: int = Field()


class AdsShareTargetGroupResponse(BaseResponse):
    response: "AdsShareTargetGroupResponseModel" = Field()


class AdsUpdateAdsResponse(BaseResponse):
    response: list["AdsUpdateAdsStatus"] = Field()


class AdsUpdateCampaignsResponse(BaseResponse):
    response: list["AdsCreateCampaignStatus"] = Field()


class AdsUpdateClientsResponse(BaseResponse):
    response: list["AdsUpdateClientsStatus"] = Field()


class AdsUpdateOfficeUsersResponse(BaseResponse):
    response: list["AdsUpdateOfficeUsersResult"] = Field()


__all__ = (
    "AdsAddOfficeUsersResponse",
    "AdsCheckLinkResponse",
    "AdsCreateAdsResponse",
    "AdsCreateCampaignsResponse",
    "AdsCreateClientsResponse",
    "AdsCreateLookalikeRequestResponse",
    "AdsCreateLookalikeRequestResponseModel",
    "AdsCreateTargetGroupResponse",
    "AdsCreateTargetGroupResponseModel",
    "AdsCreateTargetPixelResponse",
    "AdsCreateTargetPixelResponseModel",
    "AdsDeleteAdsResponse",
    "AdsDeleteCampaignsResponse",
    "AdsDeleteClientsResponse",
    "AdsGetAccountsResponse",
    "AdsGetAdsLayoutResponse",
    "AdsGetAdsResponse",
    "AdsGetAdsTargetingResponse",
    "AdsGetBudgetResponse",
    "AdsGetCampaignsResponse",
    "AdsGetCategoriesResponse",
    "AdsGetCategoriesResponseModel",
    "AdsGetClientsResponse",
    "AdsGetDemographicsResponse",
    "AdsGetFloodStatsResponse",
    "AdsGetLookalikeRequestsResponse",
    "AdsGetLookalikeRequestsResponseModel",
    "AdsGetMusiciansResponse",
    "AdsGetMusiciansResponseModel",
    "AdsGetOfficeUsersResponse",
    "AdsGetPostsReachResponse",
    "AdsGetRejectionReasonResponse",
    "AdsGetStatisticsResponse",
    "AdsGetSuggestionsCitiesResponse",
    "AdsGetSuggestionsRegionsResponse",
    "AdsGetSuggestionsResponse",
    "AdsGetSuggestionsSchoolsResponse",
    "AdsGetTargetGroupsResponse",
    "AdsGetTargetPixelsResponse",
    "AdsGetTargetingStatsResponse",
    "AdsGetUploadURLResponse",
    "AdsGetVideoUploadURLResponse",
    "AdsImportTargetContactsResponse",
    "AdsRemoveOfficeUsersResponse",
    "AdsRemoveTargetContactsResponse",
    "AdsRemoveTargetContactsResponseModel",
    "AdsSaveLookalikeRequestResultResponse",
    "AdsSaveLookalikeRequestResultResponseModel",
    "AdsShareTargetGroupResponse",
    "AdsShareTargetGroupResponseModel",
    "AdsUpdateAdsResponse",
    "AdsUpdateCampaignsResponse",
    "AdsUpdateClientsResponse",
    "AdsUpdateOfficeUsersResponse",
)
