import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import (
    AdsAccount,
    AdsAd,
    AdsAdLayout,
    AdsCampaign,
    AdsClient,
    AdsCreateAdStatus,
    AdsCreateCampaignStatus,
    AdsCreateClientsStatus,
    AdsDemoStats,
    AdsFloodStats,
    AdsLinkStatus,
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
from vkbottle_types.responses.ads import *  # noqa: F401,F403  # type: ignore
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
    BaseUndefinedResponse,
)


class AdsCategory(BaseCategory):
    async def add_office_users(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[bool]:
        """Method `ads.addOfficeUsers()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.addOfficeUsers", params)
        model = AdsAddOfficeUsersResponse
        return model(**response).response

    async def check_link(
        self,
        account_id: int,
        link_type: str,
        link_url: str,
        campaign_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "AdsLinkStatus":
        """Method `ads.checkLink()`

        :param account_id: Advertising account ID.
        :param link_type: Object type: *'community' - community,, *'post' - community post,, *'application' - VK application,, *'video' - video,, *'site' - external site.
        :param link_url: Object URL.
        :param campaign_id: Campaign ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.checkLink", params)
        model = AdsCheckLinkResponse
        return model(**response).response

    async def create_ads(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsCreateAdStatus]:
        """Method `ads.createAds()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.createAds", params)
        model = AdsCreateAdsResponse
        return model(**response).response

    async def create_campaigns(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsCreateCampaignStatus]:
        """Method `ads.createCampaigns()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.createCampaigns", params)
        model = AdsCreateCampaignsResponse
        return model(**response).response

    async def create_clients(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsCreateClientsStatus]:
        """Method `ads.createClients()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.createClients", params)
        model = AdsCreateClientsResponse
        return model(**response).response

    async def create_lookalike_request(
        self,
        account_id: int,
        source_type: str,
        client_id: typing.Optional[int] = None,
        retargeting_group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AdsCreateLookalikeRequestResponseModel:
        """Method `ads.createLookalikeRequest()`

        :param account_id:
        :param source_type:
        :param client_id:
        :param retargeting_group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.createLookalikeRequest", params)
        model = AdsCreateLookalikeRequestResponse
        return model(**response).response

    async def create_target_group(
        self,
        account_id: int,
        lifetime: int,
        name: str,
        client_id: typing.Optional[int] = None,
        target_pixel_id: typing.Optional[int] = None,
        target_pixel_rules: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdsCreateTargetGroupResponseModel:
        """Method `ads.createTargetGroup()`

        :param account_id: Advertising account ID.
        :param lifetime: 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param name: Name of the target group - a string up to 64 characters long.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param target_pixel_id:
        :param target_pixel_rules:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.createTargetGroup", params)
        model = AdsCreateTargetGroupResponse
        return model(**response).response

    async def create_target_pixel(
        self,
        account_id: int,
        category_id: int,
        name: str,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdsCreateTargetPixelResponseModel:
        """Method `ads.createTargetPixel()`

        :param account_id:
        :param category_id:
        :param name:
        :param client_id:
        :param domain:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.createTargetPixel", params)
        model = AdsCreateTargetPixelResponse
        return model(**response).response

    async def delete_ads(
        self,
        account_id: int,
        ids: str,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
        """Method `ads.deleteAds()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with ad IDs.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteAds", params)
        model = AdsDeleteAdsResponse
        return model(**response).response

    async def delete_campaigns(
        self,
        account_id: int,
        ids: str,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
        """Method `ads.deleteCampaigns()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted campaigns.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteCampaigns", params)
        model = AdsDeleteCampaignsResponse
        return model(**response).response

    async def delete_clients(
        self,
        account_id: int,
        ids: str,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
        """Method `ads.deleteClients()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted clients.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteClients", params)
        model = AdsDeleteClientsResponse
        return model(**response).response

    async def delete_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `ads.deleteTargetGroup()`

        :param account_id: Advertising account ID.
        :param target_group_id: Group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteTargetGroup", params)
        model = BaseOkResponse
        return model(**response).response

    async def delete_target_pixel(
        self,
        account_id: int,
        target_pixel_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Dict[str, typing.Any]:
        """Method `ads.deleteTargetPixel()`

        :param account_id:
        :param target_pixel_id:
        :param client_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.deleteTargetPixel", params)
        model = BaseUndefinedResponse
        return model(**response).response

    async def get_accounts(
        self,
        **kwargs: typing.Any,
    ) -> typing.List[AdsAccount]:
        """Method `ads.getAccounts()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAccounts", params)
        model = AdsGetAccountsResponse
        return model(**response).response

    async def get_ads(
        self,
        account_id: int,
        ad_ids: typing.Optional[str] = None,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        only_deleted: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsAd]:
        """Method `ads.getAds()`

        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown: *0 - show only active ads,, *1 - show all ads.
        :param limit: Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 - show all ads,, *1 - show only archived ads. Available when include_deleted flag is *1
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAds", params)
        model = AdsGetAdsResponse
        return model(**response).response

    async def get_ads_layout(
        self,
        account_id: int,
        ad_ids: typing.Optional[str] = None,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        only_deleted: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsAdLayout]:
        """Method `ads.getAdsLayout()`

        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 - show only active ads,, *1 - show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 - show all ads,, *1 - show only archived ads. Available when include_deleted flag is *1
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAdsLayout", params)
        model = AdsGetAdsLayoutResponse
        return model(**response).response

    async def get_ads_targeting(
        self,
        account_id: int,
        ad_ids: typing.Optional[str] = None,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        include_deleted: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        only_deleted: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargSettings]:
        """Method `ads.getAdsTargeting()`

        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: flag that specifies whether archived ads shall be shown: *0 - show only active ads,, *1 - show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset needed to return a specific subset of results.
        :param only_deleted:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getAdsTargeting", params)
        model = AdsGetAdsTargetingResponse
        return model(**response).response

    async def get_budget(
        self,
        account_id: int,
        **kwargs: typing.Any,
    ) -> str:
        """Method `ads.getBudget()`

        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getBudget", params)
        model = AdsGetBudgetResponse
        return model(**response).response

    async def get_campaigns(
        self,
        account_id: int,
        campaign_ids: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[typing.Literal["ads_count"]]] = None,
        include_deleted: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsCampaign]:
        """Method `ads.getCampaigns()`

        :param account_id: Advertising account ID.
        :param campaign_ids: Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :param client_id: 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param fields:
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 - show only active campaigns,, *1 - show all campaigns.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getCampaigns", params)
        model = AdsGetCampaignsResponse
        return model(**response).response

    async def get_categories(
        self,
        lang: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdsGetCategoriesResponseModel:
        """Method `ads.getCategories()`

        :param lang: Language. The full list of supported languages is [vk.ru/dev/api_requests|here].
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getCategories", params)
        model = AdsGetCategoriesResponse
        return model(**response).response

    async def get_clients(
        self,
        account_id: int,
        **kwargs: typing.Any,
    ) -> typing.List[AdsClient]:
        """Method `ads.getClients()`

        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getClients", params)
        model = AdsGetClientsResponse
        return model(**response).response

    async def get_demographics(
        self,
        account_id: int,
        date_from: str,
        date_to: str,
        ids: str,
        ids_type: str,
        period: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsDemoStats]:
        """Method `ads.getDemographics()`

        :param account_id: Advertising account ID.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - day it was created on,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - current day,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - current month,, *overall: 0.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns.
        :param period: Data grouping by dates: *day - statistics by days,, *month - statistics by months,, *overall - overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getDemographics", params)
        model = AdsGetDemographicsResponse
        return model(**response).response

    async def get_flood_stats(
        self,
        account_id: int,
        **kwargs: typing.Any,
    ) -> "AdsFloodStats":
        """Method `ads.getFloodStats()`

        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getFloodStats", params)
        model = AdsGetFloodStatsResponse
        return model(**response).response

    async def get_lookalike_requests(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        requests_ids: typing.Optional[str] = None,
        sort_by: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> AdsGetLookalikeRequestsResponseModel:
        """Method `ads.getLookalikeRequests()`

        :param account_id:
        :param client_id:
        :param limit:
        :param offset:
        :param requests_ids:
        :param sort_by:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getLookalikeRequests", params)
        model = AdsGetLookalikeRequestsResponse
        return model(**response).response

    async def get_musicians(
        self,
        artist_name: str,
        **kwargs: typing.Any,
    ) -> AdsGetMusiciansResponseModel:
        """Method `ads.getMusicians()`

        :param artist_name:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getMusicians", params)
        model = AdsGetMusiciansResponse
        return model(**response).response

    async def get_musicians_by_ids(
        self,
        ids: typing.List[int],
        **kwargs: typing.Any,
    ) -> AdsGetMusiciansResponseModel:
        """Method `ads.getMusiciansByIds()`

        :param ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getMusiciansByIds", params)
        model = AdsGetMusiciansResponse
        return model(**response).response

    async def get_office_users(
        self,
        account_id: int,
        **kwargs: typing.Any,
    ) -> typing.List[AdsUsers]:
        """Method `ads.getOfficeUsers()`

        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getOfficeUsers", params)
        model = AdsGetOfficeUsersResponse
        return model(**response).response

    async def get_posts_reach(
        self,
        account_id: int,
        ids: str,
        ids_type: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsPromotedPostReach]:
        """Method `ads.getPostsReach()`

        :param account_id: Advertising account ID.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getPostsReach", params)
        model = AdsGetPostsReachResponse
        return model(**response).response

    async def get_rejection_reason(
        self,
        account_id: int,
        ad_id: int,
        **kwargs: typing.Any,
    ) -> "AdsRejectReason":
        """Method `ads.getRejectionReason()`

        :param account_id: Advertising account ID.
        :param ad_id: Ad ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getRejectionReason", params)
        model = AdsGetRejectionReasonResponse
        return model(**response).response

    async def get_statistics(
        self,
        account_id: int,
        date_from: str,
        date_to: str,
        ids: str,
        ids_type: str,
        period: str,
        stats_fields: typing.Optional[typing.List[typing.Literal["views_times"]]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsStats]:
        """Method `ads.getStatistics()`

        :param account_id: Advertising account ID.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - day it was created on,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 - September 27, 2011, **0 - current day,, *month: YYYY-MM, example: 2011-09 - September 2011, **0 - current month,, *overall: 0.
        :param ids: IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad - ads,, *campaign - campaigns,, *client - clients,, *office - account.
        :param period: Data grouping by dates: *day - statistics by days,, *month - statistics by months,, *overall - overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param stats_fields: Additional fields to add to statistics
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getStatistics", params)
        model = AdsGetStatisticsResponse
        return model(**response).response

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        cities: str,
        country: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargSuggestionsRegions]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        cities: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargSuggestionsCities]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        cities: str,
        country: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargSuggestionsSchools]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        cities: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargSuggestions]: ...

    async def get_suggestions(
        self,
        section: str,
        cities: typing.Optional[str] = None,
        country: typing.Optional[int] = None,
        ids: typing.Optional[str] = None,
        lang: typing.Optional[str] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[
        typing.List[AdsTargSuggestionsSchools],
        typing.List[AdsTargSuggestions],
        typing.List[AdsTargSuggestionsCities],
        typing.List[AdsTargSuggestionsRegions],
    ]:
        """Method `ads.getSuggestions()`

        :param section: Section, suggestions are retrieved in. Available values: *countries - request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions - requested list of regions. 'country' parameter is required. *cities - requested list of cities. 'country' parameter is required. *districts - requested list of districts. 'cities' parameter is required. *stations - requested list of subway stations. 'cities' parameter is required. *streets - requested list of streets. 'cities' parameter is required. *schools - requested list of educational organizations. 'cities' parameter is required. *interests - requested list of interests. *positions - requested list of positions (professions). *group_types - requested list of group types. *religions - requested list of religious commitments. *browsers - requested list of browsers and mobile devices.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param country: ID of the country objects are searched in.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param lang: Language of the returned string values. Supported languages: *ru - Russian,, *ua - Ukrainian,, *en - English.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getSuggestions", params)
        model = self.get_model(
            (
                (("cities",), AdsGetSuggestionsRegionsResponse),
                (("regions",), AdsGetSuggestionsRegionsResponse),
                (("schools",), AdsGetSuggestionsSchoolsResponse),
            ),
            default=AdsGetSuggestionsResponse,
            params=params,
        )
        return model(**response).response

    async def get_target_groups(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargetGroup]:
        """Method `ads.getTargetGroups()`

        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: '1' - to return pixel code.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getTargetGroups", params)
        model = AdsGetTargetGroupsResponse
        return model(**response).response

    async def get_target_pixels(
        self,
        account_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[AdsTargetPixelInfo]:
        """Method `ads.getTargetPixels()`

        :param account_id:
        :param client_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getTargetPixels", params)
        model = AdsGetTargetPixelsResponse
        return model(**response).response

    async def get_targeting_stats(
        self,
        account_id: int,
        link_url: str,
        ad_format: typing.Optional[int] = None,
        ad_id: typing.Optional[int] = None,
        ad_platform: typing.Optional[str] = None,
        ad_platform_no_ad_network: typing.Optional[str] = None,
        ad_platform_no_wall: typing.Optional[str] = None,
        client_id: typing.Optional[int] = None,
        criteria: typing.Optional[str] = None,
        impressions_limit_period: typing.Optional[int] = None,
        link_domain: typing.Optional[str] = None,
        need_precise: typing.Optional[bool] = None,
        publisher_platforms: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "AdsTargStats":
        """Method `ads.getTargetingStats()`

        :param account_id: Advertising account ID.
        :param link_url: URL for the advertised object.
        :param ad_format: Ad format. Possible values: *'1' - image and text,, *'2' - big image,, *'3' - exclusive format,, *'4' - community, square image,, *'7' - special app format,, *'8' - special community format,, *'9' - post in community,, *'10' - app board.
        :param ad_id: ID of an ad which targeting parameters shall be analyzed.
        :param ad_platform: Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' - VK and partner sites,, *'1' - VK only. (for 'ad_format' = '9'), *'all' - all platforms,, *'desktop' - desktop version,, *'mobile' - mobile version and apps.
        :param ad_platform_no_ad_network:
        :param ad_platform_no_wall:
        :param client_id:
        :param criteria: Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param impressions_limit_period: Impressions limit period in seconds, must be a multiple of 86400(day)
        :param link_domain: Domain of the advertised object.
        :param need_precise: Additionally return recommended cpc and cpm to reach 5,10..95 percents of audience.
        :param publisher_platforms:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getTargetingStats", params)
        model = AdsGetTargetingStatsResponse
        return model(**response).response

    async def get_upload_url(
        self,
        ad_format: int,
        icon: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> str:
        """Method `ads.getUploadURL()`

        :param ad_format: Ad format: *1 - image and text,, *2 - big image,, *3 - exclusive format,, *4 - community, square image,, *7 - special app format.
        :param icon:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getUploadURL", params)
        model = AdsGetUploadURLResponse
        return model(**response).response

    async def get_video_upload_url(
        self,
        **kwargs: typing.Any,
    ) -> str:
        """Method `ads.getVideoUploadURL()`"""

        params = self.get_set_params(locals())
        response = await self.api.request("ads.getVideoUploadURL", params)
        model = AdsGetVideoUploadURLResponse
        return model(**response).response

    async def import_target_contacts(
        self,
        account_id: int,
        contacts: str,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> int:
        """Method `ads.importTargetContacts()`

        :param account_id: Advertising account ID.
        :param contacts: List of phone numbers, emails or user IDs separated with a comma.
        :param target_group_id: Target group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.importTargetContacts", params)
        model = AdsImportTargetContactsResponse
        return model(**response).response

    async def remove_office_users(
        self,
        account_id: int,
        ids: str,
        **kwargs: typing.Any,
    ) -> typing.List[bool]:
        """Method `ads.removeOfficeUsers()`

        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted managers.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.removeOfficeUsers", params)
        model = AdsRemoveOfficeUsersResponse
        return model(**response).response

    async def remove_target_contacts(
        self,
        account_id: int,
        contacts: str,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AdsRemoveTargetContactsResponseModel:
        """Method `ads.removeTargetContacts()`

        :param account_id:
        :param contacts:
        :param target_group_id:
        :param client_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.removeTargetContacts", params)
        model = AdsRemoveTargetContactsResponse
        return model(**response).response

    async def save_lookalike_request_result(
        self,
        account_id: int,
        level: int,
        request_id: int,
        client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AdsSaveLookalikeRequestResultResponseModel:
        """Method `ads.saveLookalikeRequestResult()`

        :param account_id:
        :param level:
        :param request_id:
        :param client_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.saveLookalikeRequestResult", params)
        model = AdsSaveLookalikeRequestResultResponse
        return model(**response).response

    async def share_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        share_with_client_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> AdsShareTargetGroupResponseModel:
        """Method `ads.shareTargetGroup()`

        :param account_id:
        :param target_group_id:
        :param client_id:
        :param share_with_client_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.shareTargetGroup", params)
        model = AdsShareTargetGroupResponse
        return model(**response).response

    async def update_ads(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsUpdateAdsStatus]:
        """Method `ads.updateAds()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateAds", params)
        model = AdsUpdateAdsResponse
        return model(**response).response

    async def update_campaigns(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsCreateCampaignStatus]:
        """Method `ads.updateCampaigns()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateCampaigns", params)
        model = AdsUpdateCampaignsResponse
        return model(**response).response

    async def update_clients(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsUpdateClientsStatus]:
        """Method `ads.updateClients()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateClients", params)
        model = AdsUpdateClientsResponse
        return model(**response).response

    async def update_office_users(
        self,
        account_id: int,
        data: str,
        **kwargs: typing.Any,
    ) -> typing.List[AdsUpdateOfficeUsersResult]:
        """Method `ads.updateOfficeUsers()`

        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateOfficeUsers", params)
        model = AdsUpdateOfficeUsersResponse
        return model(**response).response

    async def update_target_group(
        self,
        account_id: int,
        lifetime: int,
        name: str,
        target_group_id: int,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        target_pixel_id: typing.Optional[int] = None,
        target_pixel_rules: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `ads.updateTargetGroup()`

        :param account_id: Advertising account ID.
        :param lifetime: 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' - automatic exclusion is off.
        :param name: New name of the target group - a string up to 64 characters long.
        :param target_group_id: Group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param domain: Domain of the site where user accounting code will be placed.
        :param target_pixel_id:
        :param target_pixel_rules:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateTargetGroup", params)
        model = BaseOkResponse
        return model(**response).response

    async def update_target_pixel(
        self,
        account_id: int,
        category_id: int,
        name: str,
        target_pixel_id: int,
        client_id: typing.Optional[int] = None,
        domain: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Dict[str, typing.Any]:
        """Method `ads.updateTargetPixel()`

        :param account_id:
        :param category_id:
        :param name:
        :param target_pixel_id:
        :param client_id:
        :param domain:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("ads.updateTargetPixel", params)
        model = BaseUndefinedResponse
        return model(**response).response


__all__ = ("AdsCategory",)
