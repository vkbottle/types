from vkbottle_types.responses import storage, base
from typing import Optional, Any, List
from .base_category import BaseCategory


class StorageCategory(BaseCategory):
    async def get(
        self,
        key: Optional[str] = None,
        keys: Optional[List[str]] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> storage.GetV5110ResponseModel:
        """Returns a value of variable with the name set by key parameter.
        :param key:
        :param keys:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("storage.get", params)
        model = self.get_model(
            {("keys",): storage.GetWithKeysResponse},
            default=storage.GetV5110Response,
            params=params,
        )
        return model(**response).response

    async def get_keys(
        self,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
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
        value: Optional[str] = None,
        user_id: Optional[int] = None,
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
