import typing

from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.storage import GetKeysResponse, GetResponse, StorageValue

from .base_category import BaseCategory


class StorageCategory(BaseCategory):
    async def get(
        self,
        key: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[StorageValue]:
        """Returns a value of variable with the name set by key parameter.

        :param key:
        :param keys:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.get", params)
        model = GetResponse
        return model(**response).response

    async def get_keys(
        self,
        user_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[str]:
        """Returns the names of all variables.

        :param user_id: user id, whose variables names are returned if they were requested with a server method.
        :param offset:
        :param count: amount of variable names the info needs to be collected from.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.getKeys", params)
        model = GetKeysResponse
        return model(**response).response

    async def set(
        self,
        key: str,
        value: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Saves a value of variable with the name set by 'key' parameter.

        :param key:
        :param value:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.set", params)
        model = OkResponse
        return model(**response).response
