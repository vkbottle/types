import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseCountry, DatabaseCitiesFields, DatabaseCityById, DatabaseSchoolClass, DatabaseStation
from vkbottle_types.responses.database import *  # noqa: F401,F403  # type: ignore


class DatabaseCategory(BaseCategory):
    async def get_chairs(
        self,
        faculty_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetChairsResponseModel:
        """Method `database.getChairs()`

        :param faculty_id: id of the faculty to get chairs from
        :param count: amount of chairs to get
        :param offset: offset required to get a certain subset of chairs
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getChairs", params)
        model = DatabaseGetChairsResponse
        return model(**response).response

    async def get_cities(
        self,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[DatabaseCitiesFields]] = None,
        need_all: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        region_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetCitiesResponseModel:
        """Method `database.getCities()`

        :param count: Number of cities to return.
        :param fields: Cities fields to return. Sample values: 'fias_guid'
        :param need_all: '1' - to return all cities in the country, '0' - to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param q: Search query.
        :param region_id: Region ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCities", params)
        model = DatabaseGetCitiesResponse
        return model(**response).response

    async def get_cities_by_id(
        self,
        city_ids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[DatabaseCitiesFields]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[DatabaseCityById]:
        """Method `database.getCitiesById()`

        :param city_ids: City IDs.
        :param fields: Cities fields to return. Sample values: 'fias_guid'
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCitiesById", params)
        model = DatabaseGetCitiesByIdResponse
        return model(**response).response

    async def get_countries(
        self,
        code: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        need_all: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetCountriesResponseModel:
        """Method `database.getCountries()`

        :param code: Country codes in [vk.ru/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param count: Number of countries to return.
        :param need_all: '1' - to return a full list of all countries, '0' - to return a list of countries near the current user's country (default).
        :param offset: Offset needed to return a specific subset of countries.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCountries", params)
        model = DatabaseGetCountriesResponse
        return model(**response).response

    async def get_countries_by_id(
        self,
        country_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[BaseCountry]:
        """Method `database.getCountriesById()`

        :param country_ids: Country IDs.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCountriesById", params)
        model = DatabaseGetCountriesByIdResponse
        return model(**response).response

    async def get_faculties(
        self,
        university_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetFacultiesResponseModel:
        """Method `database.getFaculties()`

        :param university_id: University ID.
        :param count: Number of faculties to return.
        :param offset: Offset needed to return a specific subset of faculties.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getFaculties", params)
        model = DatabaseGetFacultiesResponse
        return model(**response).response

    async def get_metro_stations(
        self,
        city_id: int,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetMetroStationsResponseModel:
        """Method `database.getMetroStations()`

        :param city_id:
        :param count:
        :param extended:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getMetroStations", params)
        model = DatabaseGetMetroStationsResponse
        return model(**response).response

    async def get_metro_stations_by_id(
        self,
        station_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[DatabaseStation]:
        """Method `database.getMetroStationsById()`

        :param station_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getMetroStationsById", params)
        model = DatabaseGetMetroStationsByIdResponse
        return model(**response).response

    async def get_regions(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetRegionsResponseModel:
        """Method `database.getRegions()`

        :param count: Number of regions to return.
        :param offset: Offset needed to return specific subset of regions.
        :param q: Search query.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getRegions", params)
        model = DatabaseGetRegionsResponse
        return model(**response).response

    async def get_school_classes(
        self,
        country_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[DatabaseSchoolClass]:
        """Method `database.getSchoolClasses()`

        :param country_id: Country ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getSchoolClasses", params)
        model = DatabaseGetSchoolClassesNewResponse
        return model(**response).response

    async def get_schools(
        self,
        city_id: int,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetSchoolsResponseModel:
        """Method `database.getSchools()`

        :param city_id: City ID.
        :param count: Number of schools to return.
        :param offset: Offset needed to return a specific subset of schools.
        :param q: Search query.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getSchools", params)
        model = DatabaseGetSchoolsResponse
        return model(**response).response

    async def get_universities(
        self,
        city_id: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> DatabaseGetUniversitiesResponseModel:
        """Method `database.getUniversities()`

        :param city_id: City ID.
        :param count: Number of universities to return.
        :param offset: Offset needed to return a specific subset of universities.
        :param q: Search query.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getUniversities", params)
        model = DatabaseGetUniversitiesResponse
        return model(**response).response


__all__ = ("DatabaseCategory",)
