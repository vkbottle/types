from vkbottle_types.responses import auth, base



class AuthCategory(BaseCategory):
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