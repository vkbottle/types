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
    ) -> base.OkResponseModel:
        """Checks a user's phone number for correctness.
        :param phone: Phone number.
        :param client_id: User ID.
        :param client_secret:
        :param auth_by_phone:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(**await self.api.request("auth.checkPhone", params))

    async def restore(self, phone: str, last_name: str) -> auth.RestoreResponseModel:
        """Allows to restore account access using a code received via SMS. " This method is only available for apps with [vk.com/dev/auth_direct|Direct authorization] access. "
        :param phone: User phone number.
        :param last_name: User last name.
        """

        params = self.get_set_params(locals())
        return auth.RestoreResponse(**await self.api.request("auth.restore", params))
