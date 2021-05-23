import typing
from .base_category import BaseCategory
from vkbottle_types.responses import storage, base


class StorageCategory(BaseCategory):
    async def get(
        self,
        key: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        **kwargs
    ) -> storage.GetResponseModel:
        """Returns a value of variable with the name set by key parameter.
        :param key:
        :param keys:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.get", params)
        model = storage.GetResponse
        return model(**response).response

    async def get_keys(
        self,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> storage.GetKeysResponseModel:
        """Returns the names of all variables.
        :param user_id: user id, whose variables names are returned if they were requested with a server method.
        :param offset:
        :param count: amount of variable names the info needs to be collected from.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.getKeys", params)
        model = storage.GetKeysResponse
        return model(**response).response

    async def set(
        self,
        key: str,
        value: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Saves a value of variable with the name set by 'key' parameter.
        :param key:
        :param value:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.set", params)
        model = base.OkResponse
        return model(**response).response
