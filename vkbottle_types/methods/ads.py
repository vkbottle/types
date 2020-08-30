from typing import Optional, List

from vkbottle_types.responses import ads, base
from .base_category import BaseCategory


class AdsCategory(BaseCategory):
    async def add_office_users(
        self, account_id: int, data: str, **kwargs
    ) -> ads.AddOfficeUsersResponseModel:
        """Adds managers and/or supervisors to advertising account.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe added managers. Description of 'user_specification' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.AddOfficeUsersResponse(
            **await self.api.request("ads.addOfficeUsers", params)
        )

    async def check_link(
        self,
        account_id: int,
        link_type: str,
        link_url: str,
        campaign_id: Optional[int] = None,
        **kwargs
    ) -> ads.CheckLinkResponseModel:
        """Allows to check the ad link.
        :param account_id: Advertising account ID.
        :param link_type: Object type: *'community' — community,, *'post' — community post,, *'application' — VK application,, *'video' — video,, *'site' — external site.
        :param link_url: Object URL.
        :param campaign_id: Campaign ID
        """

        params = self.get_set_params(locals())
        return ads.CheckLinkResponse(**await self.api.request("ads.checkLink", params))

    async def create_ads(
        self, account_id: int, data: str, **kwargs
    ) -> ads.CreateAdsResponseModel:
        """Creates ads.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created ads. Description of 'ad_specification' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.CreateAdsResponse(**await self.api.request("ads.createAds", params))

    async def create_campaigns(
        self, account_id: int, data: str, **kwargs
    ) -> ads.CreateCampaignsResponseModel:
        """Creates advertising campaigns.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'campaign_specification' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.CreateCampaignsResponse(
            **await self.api.request("ads.createCampaigns", params)
        )

    async def create_clients(
        self, account_id: int, data: str, **kwargs
    ) -> ads.CreateClientsResponseModel:
        """Creates clients of an advertising agency.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe created campaigns. Description of 'client_specification' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.CreateClientsResponse(
            **await self.api.request("ads.createClients", params)
        )

    async def create_target_group(
        self,
        account_id: int,
        name: str,
        lifetime: int,
        client_id: Optional[int] = None,
        target_pixel_id: Optional[int] = None,
        target_pixel_rules: Optional[str] = None,
        **kwargs
    ) -> ads.CreateTargetGroupResponseModel:
        """Creates a group to re-target ads for users who visited advertiser's site (viewed information about the product, registered, etc.).
        :param account_id: Advertising account ID.
        :param name: Name of the target group — a string up to 64 characters long.
        :param lifetime: 'For groups with auditory created with pixel code only.', , Number of days after that users will be automatically removed from the group.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param target_pixel_id:
        :param target_pixel_rules:
        """

        params = self.get_set_params(locals())
        return ads.CreateTargetGroupResponse(
            **await self.api.request("ads.createTargetGroup", params)
        )

    async def delete_ads(
        self, account_id: int, ids: str, **kwargs
    ) -> ads.DeleteAdsResponseModel:
        """Archives ads.
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with ad IDs.
        """

        params = self.get_set_params(locals())
        return ads.DeleteAdsResponse(**await self.api.request("ads.deleteAds", params))

    async def delete_campaigns(
        self, account_id: int, ids: str, **kwargs
    ) -> ads.DeleteCampaignsResponseModel:
        """Archives advertising campaigns.
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted campaigns.
        """

        params = self.get_set_params(locals())
        return ads.DeleteCampaignsResponse(
            **await self.api.request("ads.deleteCampaigns", params)
        )

    async def delete_clients(
        self, account_id: int, ids: str, **kwargs
    ) -> ads.DeleteClientsResponseModel:
        """Archives clients of an advertising agency.
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted clients.
        """

        params = self.get_set_params(locals())
        return ads.DeleteClientsResponse(
            **await self.api.request("ads.deleteClients", params)
        )

    async def delete_target_group(
        self,
        account_id: int,
        target_group_id: int,
        client_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Deletes a retarget group.
        :param account_id: Advertising account ID.
        :param target_group_id: Group ID.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("ads.deleteTargetGroup", params)
        )

    async def get_accounts(self, **kwargs) -> ads.GetAccountsResponseModel:
        """Returns a list of advertising accounts."""

        params = self.get_set_params(locals())
        return ads.GetAccountsResponse(
            **await self.api.request("ads.getAccounts", params)
        )

    async def get_ads(
        self,
        account_id: int,
        ad_ids: Optional[str] = None,
        campaign_ids: Optional[str] = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        only_deleted: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> ads.GetAdsResponseModel:
        """Returns number of ads.
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'Available and required for advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param only_deleted: Flag that specifies whether to show only archived ads: *0 — show all ads,, *1 — show only archived ads. Available when include_deleted flag is *1
        :param limit: Limit of number of returned ads. Used only if ad_ids parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """

        params = self.get_set_params(locals())
        return ads.GetAdsResponse(**await self.api.request("ads.getAds", params))

    async def get_ads_layout(
        self,
        account_id: int,
        ad_ids: Optional[str] = None,
        campaign_ids: Optional[str] = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> ads.GetAdsLayoutResponseModel:
        """Returns descriptions of ad layouts.
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset. Used in the same cases as 'limit' parameter.
        """

        params = self.get_set_params(locals())
        return ads.GetAdsLayoutResponse(
            **await self.api.request("ads.getAdsLayout", params)
        )

    async def get_ads_targeting(
        self,
        account_id: int,
        ad_ids: Optional[str] = None,
        campaign_ids: Optional[str] = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> ads.GetAdsTargetingResponseModel:
        """Returns ad targeting parameters.
        :param account_id: Advertising account ID.
        :param ad_ids: Filter by ads. Serialized JSON array with ad IDs. If the parameter is null, all ads will be shown.
        :param campaign_ids: Filter by advertising campaigns. Serialized JSON array with campaign IDs. If the parameter is null, ads of all campaigns will be shown.
        :param client_id: 'For advertising agencies.' ID of the client ads are retrieved from.
        :param include_deleted: flag that specifies whether archived ads shall be shown: *0 — show only active ads,, *1 — show all ads.
        :param limit: Limit of number of returned ads. Used only if 'ad_ids' parameter is null, and 'campaign_ids' parameter contains ID of only one campaign.
        :param offset: Offset needed to return a specific subset of results.
        """

        params = self.get_set_params(locals())
        return ads.GetAdsTargetingResponse(
            **await self.api.request("ads.getAdsTargeting", params)
        )

    async def get_budget(self, account_id: int, **kwargs) -> ads.GetBudgetResponseModel:
        """Returns current budget of the advertising account.
        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        return ads.GetBudgetResponse(**await self.api.request("ads.getBudget", params))

    async def get_campaigns(
        self,
        account_id: int,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        campaign_ids: Optional[str] = None,
        fields: Optional[List[str]] = None,
        **kwargs
    ) -> ads.GetCampaignsResponseModel:
        """Returns a list of campaigns in an advertising account.
        :param account_id: Advertising account ID.
        :param client_id: 'For advertising agencies'. ID of the client advertising campaigns are retrieved from.
        :param include_deleted: Flag that specifies whether archived ads shall be shown. *0 — show only active campaigns,, *1 — show all campaigns.
        :param campaign_ids: Filter of advertising campaigns to show. Serialized JSON array with campaign IDs. Only campaigns that exist in 'campaign_ids' and belong to the specified advertising account will be shown. If the parameter is null, all campaigns will be shown.
        :param fields:
        """

        params = self.get_set_params(locals())
        return ads.GetCampaignsResponse(
            **await self.api.request("ads.getCampaigns", params)
        )

    async def get_categories(
        self, lang: Optional[str] = None, **kwargs
    ) -> ads.GetCategoriesResponseModel:
        """Returns a list of possible ad categories.
        :param lang: Language. The full list of supported languages is [vk.com/dev/api_requests|here].
        """

        params = self.get_set_params(locals())
        return ads.GetCategoriesResponse(
            **await self.api.request("ads.getCategories", params)
        )

    async def get_clients(
        self, account_id: int, **kwargs
    ) -> ads.GetClientsResponseModel:
        """Returns a list of advertising agency's clients.
        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        return ads.GetClientsResponse(
            **await self.api.request("ads.getClients", params)
        )

    async def get_demographics(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        **kwargs
    ) -> ads.GetDemographicsResponseModel:
        """Returns demographics for ads or campaigns.
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        """

        params = self.get_set_params(locals())
        return ads.GetDemographicsResponse(
            **await self.api.request("ads.getDemographics", params)
        )

    async def get_flood_stats(
        self, account_id: int, **kwargs
    ) -> ads.GetFloodStatsResponseModel:
        """Returns information about current state of a counter — number of remaining runs of methods and time to the next counter nulling in seconds.
        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        return ads.GetFloodStatsResponse(
            **await self.api.request("ads.getFloodStats", params)
        )

    async def get_lookalike_requests(
        self,
        account_id: int,
        client_id: Optional[int] = None,
        requests_ids: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        **kwargs
    ) -> ads.GetLookalikeRequestsResponseModel:
        """ads.getLookalikeRequests method
        :param account_id:
        :param client_id:
        :param requests_ids:
        :param offset:
        :param limit:
        :param sort_by:
        """

        params = self.get_set_params(locals())
        return ads.GetLookalikeRequestsResponse(
            **await self.api.request("ads.getLookalikeRequests", params)
        )

    async def get_musicians(
        self, artist_name: str, **kwargs
    ) -> ads.GetMusiciansResponseModel:
        """ads.getMusicians method
        :param artist_name:
        """

        params = self.get_set_params(locals())
        return ads.GetMusiciansResponse(
            **await self.api.request("ads.getMusicians", params)
        )

    async def get_office_users(
        self, account_id: int, **kwargs
    ) -> ads.GetOfficeUsersResponseModel:
        """Returns a list of managers and supervisors of advertising account.
        :param account_id: Advertising account ID.
        """

        params = self.get_set_params(locals())
        return ads.GetOfficeUsersResponse(
            **await self.api.request("ads.getOfficeUsers", params)
        )

    async def get_posts_reach(
        self, account_id: int, ids_type: str, ids: str, **kwargs
    ) -> ads.GetPostsReachResponseModel:
        """Returns detailed statistics of promoted posts reach from campaigns and ads.
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns.
        :param ids: IDs requested ads or campaigns, separated with a comma, depending on the value set in 'ids_type'. Maximum 100 objects.
        """

        params = self.get_set_params(locals())
        return ads.GetPostsReachResponse(
            **await self.api.request("ads.getPostsReach", params)
        )

    async def get_rejection_reason(
        self, account_id: int, ad_id: int, **kwargs
    ) -> ads.GetRejectionReasonResponseModel:
        """Returns a reason of ad rejection for pre-moderation.
        :param account_id: Advertising account ID.
        :param ad_id: Ad ID.
        """

        params = self.get_set_params(locals())
        return ads.GetRejectionReasonResponse(
            **await self.api.request("ads.getRejectionReason", params)
        )

    async def get_statistics(
        self,
        account_id: int,
        ids_type: str,
        ids: str,
        period: str,
        date_from: str,
        date_to: str,
        stats_fields: Optional[List[str]] = None,
        **kwargs
    ) -> ads.GetStatisticsResponseModel:
        """Returns statistics of performance indicators for ads, campaigns, clients or the whole account.
        :param account_id: Advertising account ID.
        :param ids_type: Type of requested objects listed in 'ids' parameter: *ad — ads,, *campaign — campaigns,, *client — clients,, *office — account.
        :param ids: IDs requested ads, campaigns, clients or account, separated with a comma, depending on the value set in 'ids_type'. Maximum 2000 objects.
        :param period: Data grouping by dates: *day — statistics by days,, *month — statistics by months,, *overall — overall statistics. 'date_from' and 'date_to' parameters set temporary limits.
        :param date_from: Date to show statistics from. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — day it was created on,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — month it was created in,, *overall: 0.
        :param date_to: Date to show statistics to. For different value of 'period' different date format is used: *day: YYYY-MM-DD, example: 2011-09-27 — September 27, 2011, **0 — current day,, *month: YYYY-MM, example: 2011-09 — September 2011, **0 — current month,, *overall: 0.
        :param stats_fields: Additional fields to add to statistics
        """

        params = self.get_set_params(locals())
        return ads.GetStatisticsResponse(
            **await self.api.request("ads.getStatistics", params)
        )

    async def get_suggestions(
        self,
        section: str,
        ids: Optional[str] = None,
        q: Optional[str] = None,
        country: Optional[int] = None,
        cities: Optional[str] = None,
        lang: Optional[str] = None,
        **kwargs
    ) -> ads.GetSuggestionsResponseModel:
        """Returns a set of auto-suggestions for various targeting parameters.
        :param section: Section, suggestions are retrieved in. Available values: *countries — request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions — requested list of regions. 'country' parameter is required. *cities — requested list of cities. 'country' parameter is required. *districts — requested list of districts. 'cities' parameter is required. *stations — requested list of subway stations. 'cities' parameter is required. *streets — requested list of streets. 'cities' parameter is required. *schools — requested list of educational organizations. 'cities' parameter is required. *interests — requested list of interests. *positions — requested list of positions (professions). *group_types — requested list of group types. *religions — requested list of religious commitments. *browsers — requested list of browsers and mobile devices.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        :param country: ID of the country objects are searched in.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param lang: Language of the returned string values. Supported languages: *ru — Russian,, *ua — Ukrainian,, *en — English.
        """

        params = self.get_set_params(locals())
        return ads.GetSuggestionsResponse(
            **await self.api.request("ads.getSuggestions", params)
        )

    async def get_target_groups(
        self,
        account_id: int,
        client_id: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> ads.GetTargetGroupsResponseModel:
        """Returns a list of target groups.
        :param account_id: Advertising account ID.
        :param client_id: 'Only for advertising agencies.', ID of the client with the advertising account where the group will be created.
        :param extended: '1' — to return pixel code.
        """

        params = self.get_set_params(locals())
        return ads.GetTargetGroupsResponse(
            **await self.api.request("ads.getTargetGroups", params)
        )

    async def get_targeting_stats(
        self,
        account_id: int,
        link_url: str,
        client_id: Optional[int] = None,
        criteria: Optional[str] = None,
        ad_id: Optional[int] = None,
        ad_format: Optional[int] = None,
        ad_platform: Optional[str] = None,
        ad_platform_no_wall: Optional[str] = None,
        ad_platform_no_ad_network: Optional[str] = None,
        link_domain: Optional[str] = None,
        need_precise: Optional[bool] = None,
        **kwargs
    ) -> ads.GetTargetingStatsResponseModel:
        """Returns the size of targeting audience, and also recommended values for CPC and CPM.
        :param account_id: Advertising account ID.
        :param link_url: URL for the advertised object.
        :param client_id:
        :param criteria: Serialized JSON object that describes targeting parameters. Description of 'criteria' object see below.
        :param ad_id: ID of an ad which targeting parameters shall be analyzed.
        :param ad_format: Ad format. Possible values: *'1' — image and text,, *'2' — big image,, *'3' — exclusive format,, *'4' — community, square image,, *'7' — special app format,, *'8' — special community format,, *'9' — post in community,, *'10' — app board.
        :param ad_platform: Platforms to use for ad showing. Possible values: (for 'ad_format' = '1'), *'0' — VK and partner sites,, *'1' — VK only. (for 'ad_format' = '9'), *'all' — all platforms,, *'desktop' — desktop version,, *'mobile' — mobile version and apps.
        :param ad_platform_no_wall:
        :param ad_platform_no_ad_network:
        :param link_domain: Domain of the advertised object.
        :param need_precise: Additionally return recommended cpc and cpm to reach 5,10..95 percents of audience.
        """

        params = self.get_set_params(locals())
        return ads.GetTargetingStatsResponse(
            **await self.api.request("ads.getTargetingStats", params)
        )

    async def get_upload_url(
        self, ad_format: int, icon: Optional[int] = None, **kwargs
    ) -> ads.GetUploadURLResponseModel:
        """Returns URL to upload an ad photo to.
        :param ad_format: Ad format: *1 — image and text,, *2 — big image,, *3 — exclusive format,, *4 — community, square image,, *7 — special app format.
        :param icon:
        """

        params = self.get_set_params(locals())
        return ads.GetUploadURLResponse(
            **await self.api.request("ads.getUploadURL", params)
        )

    async def get_video_upload_url(
        self, **kwargs
    ) -> ads.GetVideoUploadURLResponseModel:
        """Returns URL to upload an ad video to."""

        params = self.get_set_params(locals())
        return ads.GetVideoUploadURLResponse(
            **await self.api.request("ads.getVideoUploadURL", params)
        )

    async def import_target_contacts(
        self,
        account_id: int,
        target_group_id: int,
        contacts: str,
        client_id: Optional[int] = None,
        **kwargs
    ) -> ads.ImportTargetContactsResponseModel:
        """Imports a list of advertiser's contacts to count VK registered users against the target group.
        :param account_id: Advertising account ID.
        :param target_group_id: Target group ID.
        :param contacts: List of phone numbers, emails or user IDs separated with a comma.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        """

        params = self.get_set_params(locals())
        return ads.ImportTargetContactsResponse(
            **await self.api.request("ads.importTargetContacts", params)
        )

    async def remove_office_users(
        self, account_id: int, ids: str, **kwargs
    ) -> ads.RemoveOfficeUsersResponseModel:
        """Removes managers and/or supervisors from advertising account.
        :param account_id: Advertising account ID.
        :param ids: Serialized JSON array with IDs of deleted managers.
        """

        params = self.get_set_params(locals())
        return ads.RemoveOfficeUsersResponse(
            **await self.api.request("ads.removeOfficeUsers", params)
        )

    async def update_ads(
        self, account_id: int, data: str, **kwargs
    ) -> ads.UpdateAdsResponseModel:
        """Edits ads.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in ads. Description of 'ad_edit_specification' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.UpdateAdsResponse(**await self.api.request("ads.updateAds", params))

    async def update_campaigns(
        self, account_id: int, data: str, **kwargs
    ) -> ads.UpdateCampaignsResponseModel:
        """Edits advertising campaigns.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in campaigns. Description of 'campaign_mod' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.UpdateCampaignsResponse(
            **await self.api.request("ads.updateCampaigns", params)
        )

    async def update_clients(
        self, account_id: int, data: str, **kwargs
    ) -> ads.UpdateClientsResponseModel:
        """Edits clients of an advertising agency.
        :param account_id: Advertising account ID.
        :param data: Serialized JSON array of objects that describe changes in clients. Description of 'client_mod' objects see below.
        """

        params = self.get_set_params(locals())
        return ads.UpdateClientsResponse(
            **await self.api.request("ads.updateClients", params)
        )

    async def update_target_group(
        self,
        account_id: int,
        target_group_id: int,
        name: str,
        lifetime: int,
        client_id: Optional[int] = None,
        domain: Optional[str] = None,
        target_pixel_id: Optional[int] = None,
        target_pixel_rules: Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Edits a retarget group.
        :param account_id: Advertising account ID.
        :param target_group_id: Group ID.
        :param name: New name of the target group — a string up to 64 characters long.
        :param lifetime: 'Only for the groups that get audience from sites with user accounting code.', Time in days when users added to a retarget group will be automatically excluded from it. '0' - automatic exclusion is off.
        :param client_id: 'Only for advertising agencies.' , ID of the client with the advertising account where the group will be created.
        :param domain: Domain of the site where user accounting code will be placed.
        :param target_pixel_id:
        :param target_pixel_rules:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("ads.updateTargetGroup", params)
        )
