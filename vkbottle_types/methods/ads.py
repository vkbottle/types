import typing

from vkbottle_types.codegen.methods.ads import AdsCategory as _AdsCategory  # type: ignore
from vkbottle_types.responses.ads import (
    AdsGetSuggestionsCitiesResponse,
    AdsGetSuggestionsRegionsResponse,
    AdsGetSuggestionsResponse,
    AdsGetSuggestionsSchoolsResponse,
    AdsTargSuggestions,
    AdsTargSuggestionsCities,
    AdsTargSuggestionsRegions,
    AdsTargSuggestionsSchools,
)


class AdsCategory(_AdsCategory):  # type: ignore
    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        q: typing.Literal["regions"],
        country: int,
        ids: list[str] | None = None,
        lang: str | None = None,
    ) -> list[AdsTargSuggestionsRegions]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        q: typing.Literal["schools"],
        cities: list[str],
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
    ) -> list[AdsTargSuggestionsSchools]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
        q: str | None = None,
    ) -> list[AdsTargSuggestions]: ...

    @typing.overload
    async def get_suggestions(
        self,
        section: str,
        *,
        cities: list[str],
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
        q: str | None = None,
    ) -> list[AdsTargSuggestionsCities]: ...

    async def get_suggestions(
        self,
        section: str,
        *,
        cities: list[str] | None = None,
        country: int | None = None,
        ids: list[str] | None = None,
        lang: str | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> list[AdsTargSuggestionsSchools] | list[AdsTargSuggestionsCities] | list[AdsTargSuggestionsRegions] | list[AdsTargSuggestions]:
        """Method `ads.getSuggestions()`

        :param section: Section, suggestions are retrieved in. Available values: *countries - request of a list of countries. If q is not set or blank, a short list of countries is shown. Otherwise, a full list of countries is shown. *regions - requested list of regions. 'country' parameter is required. *cities - requested list of cities. 'country' parameter is required. *districts - requested list of districts. 'cities' parameter is required. *stations - requested list of subway stations. 'cities' parameter is required. *streets - requested list of streets. 'cities' parameter is required. *schools - requested list of educational organizations. 'cities' parameter is required. *interests - requested list of interests. *positions - requested list of positions (professions). *group_types - requested list of group types. *religions - requested list of religious commitments. *browsers - requested list of browsers and mobile devices.
        :param cities: IDs of cities where objects are searched in, separated with a comma.
        :param country: ID of the country objects are searched in.
        :param ids: Objects IDs separated by commas. If the parameter is passed, 'q, country, cities' should not be passed.
        :param lang: Language of the returned string values. Supported languages: *ru - Russian,, *ua - Ukrainian,, *en - English.
        :param q: Filter-line of the request (for countries, regions, cities, streets, schools, interests, positions).
        """

        params = self.get_set_params(locals())  # type: ignore
        response = await self.api.request("ads.getSuggestions", params)  # type: ignore
        model = self.get_model(  # type: ignore
            (
                dict(q=dict(regions=AdsGetSuggestionsRegionsResponse, schools=AdsGetSuggestionsSchoolsResponse)),
                (("cities",), AdsGetSuggestionsCitiesResponse),
            ),
            default=AdsGetSuggestionsResponse,
            params=params,
        )
        return model(**response).response
