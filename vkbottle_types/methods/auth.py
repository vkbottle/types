from vkbottle_types.responses import auth, base
from typing import Optional, Any, List
from .base_category import BaseCategory


class AuthCategory(BaseCategory):
    async def check_phone(
        self,
        phone: str,
        client_id: Optional[int] = None,
        client_secret: Optional[str] = None,
        auth_by_phone: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Checks a user's phone number for correctness.
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret:
        :param auth_by_phone:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("auth.checkPhone", params)
        model = base.OkResponse
        return model(**response).response

    async def restore(
        self, phone: str, last_name: str, **kwargs
    ) -> auth.RestoreResponseModel:
        """Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        :param phone: User phone number.
        :param last_name: User last name.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("auth.restore", params)
        model = auth.RestoreResponse
        return model(**response).response
