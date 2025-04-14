import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import StorageValue
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.storage import *  # noqa: F401,F403  # type: ignore


class StorageCategory(BaseCategory):
    async def get(
        self,
        key: typing.Optional[str] = None,
        keys: typing.Optional[typing.List[str]] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[StorageValue]:
        """Method `storage.get()`

        :param key:
        :param keys:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.get", params)
        model = StorageGetResponse
        return model(**response).response

    async def get_keys(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.List[str]:
        """Method `storage.getKeys()`

        :param count: amount of variable names the info needs to be collected from.
        :param offset:
        :param user_id: user id, whose variables names are returned if they were requested with a server method.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.getKeys", params)
        model = StorageGetKeysResponse
        return model(**response).response

    async def set(
        self,
        key: str,
        user_id: typing.Optional[int] = None,
        value: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `storage.set()`

        :param key:
        :param user_id:
        :param value:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.set", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("StorageCategory",)
