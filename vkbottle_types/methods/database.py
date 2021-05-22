import typing
from .base_category import BaseCategory
from vkbottle_types.responses import database


class DatabaseCategory(BaseCategory):
    async def get_chairs(
        self,
        faculty_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetChairsResponseModel:
        """Returns list of chairs on a specified faculty.
        :param faculty_id: id of the faculty to get chairs from
        :param offset: offset required to get a certain subset of chairs
        :param count: amount of chairs to get
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getChairs", params)
        model = database.GetChairsResponse
        return model(**response).response

    async def get_cities(
        self,
        country_id: int,
        region_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        need_all: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetCitiesResponseModel:
        """Returns a list of cities.
        :param country_id: Country ID.
        :param region_id: Region ID.
        :param q: Search query.
        :param need_all: '1' — to return all cities in the country, '0' — to return major cities in the country (default),
        :param offset: Offset needed to return a specific subset of cities.
        :param count: Number of cities to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCities", params)
        model = database.GetCitiesResponse
        return model(**response).response

    async def get_cities_by_id(
        self, city_ids: typing.Optional[typing.List[int]] = None, **kwargs
    ) -> database.GetCitiesByIdResponseModel:
        """Returns information about cities by their IDs.
        :param city_ids: City IDs.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCitiesById", params)
        model = database.GetCitiesByIdResponse
        return model(**response).response

    async def get_countries(
        self,
        need_all: typing.Optional[bool] = None,
        code: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetCountriesResponseModel:
        """Returns a list of countries.
        :param need_all: '1' — to return a full list of all countries, '0' — to return a list of countries near the current user's country (default).
        :param code: Country codes in [vk.com/dev/country_codes|ISO 3166-1 alpha-2] standard.
        :param offset: Offset needed to return a specific subset of countries.
        :param count: Number of countries to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCountries", params)
        model = database.GetCountriesResponse
        return model(**response).response

    async def get_countries_by_id(
        self, country_ids: typing.Optional[typing.List[int]] = None, **kwargs
    ) -> database.GetCountriesByIdResponseModel:
        """Returns information about countries by their IDs.
        :param country_ids: Country IDs.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getCountriesById", params)
        model = database.GetCountriesByIdResponse
        return model(**response).response

    async def get_faculties(
        self,
        university_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetFacultiesResponseModel:
        """Returns a list of faculties (i.e., university departments).
        :param university_id: University ID.
        :param offset: Offset needed to return a specific subset of faculties.
        :param count: Number of faculties to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getFaculties", params)
        model = database.GetFacultiesResponse
        return model(**response).response

    async def get_metro_stations(
        self,
        city_id: int,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        **kwargs
    ) -> database.GetMetroStationsResponseModel:
        """Get metro stations by city
        :param city_id:
        :param offset:
        :param count:
        :param extended:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getMetroStations", params)
        model = database.GetMetroStationsResponse
        return model(**response).response

    async def get_metro_stations_by_id(
        self, station_ids: typing.Optional[typing.List[int]] = None, **kwargs
    ) -> database.GetMetroStationsByIdResponseModel:
        """Get metro station by his id
        :param station_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getMetroStationsById", params)
        model = database.GetMetroStationsByIdResponse
        return model(**response).response

    async def get_regions(
        self,
        country_id: int,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetRegionsResponseModel:
        """Returns a list of regions.
        :param country_id: Country ID, received in [vk.com/dev/database.getCountries|database.getCountries] method.
        :param q: Search query.
        :param offset: Offset needed to return specific subset of regions.
        :param count: Number of regions to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getRegions", params)
        model = database.GetRegionsResponse
        return model(**response).response

    async def get_school_classes(
        self, country_id: typing.Optional[int] = None, **kwargs
    ) -> database.GetSchoolClassesResponseModel:
        """Returns a list of school classes specified for the country.
        :param country_id: Country ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getSchoolClasses", params)
        model = database.GetSchoolClassesResponse
        return model(**response).response

    async def get_schools(
        self,
        city_id: int,
        q: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetSchoolsResponseModel:
        """Returns a list of schools.
        :param city_id: City ID.
        :param q: Search query.
        :param offset: Offset needed to return a specific subset of schools.
        :param count: Number of schools to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getSchools", params)
        model = database.GetSchoolsResponse
        return model(**response).response

    async def get_universities(
        self,
        q: typing.Optional[str] = None,
        country_id: typing.Optional[int] = None,
        city_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> database.GetUniversitiesResponseModel:
        """Returns a list of higher education institutions.
        :param q: Search query.
        :param country_id: Country ID.
        :param city_id: City ID.
        :param offset: Offset needed to return a specific subset of universities.
        :param count: Number of universities to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("database.getUniversities", params)
        model = database.GetUniversitiesResponse
        return model(**response).response
