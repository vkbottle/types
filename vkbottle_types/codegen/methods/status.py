import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.base import OkResponse
from vkbottle_types.responses.status import GetResponse, StatusStatus


class StatusCategory(BaseCategory):
    async def get(
        self,
        user_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> StatusStatus:
        """Returns data required to show the status of a user or community.

        :param user_id: User ID or community ID. Use a negative value to designate a community ID.
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("status.get", params)
        model = GetResponse
        return model(**response).response

    async def set(
        self,
        text: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Sets a new status for the current user.

        :param text: Text of the new status.
        :param group_id: Identifier of a community to set a status in. If left blank the status is set to current user.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("status.set", params)
        model = OkResponse
        return model(**response).response


__all__ = ("StatusCategory",)
