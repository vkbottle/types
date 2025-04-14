import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import StatusStatus
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.status import *  # noqa: F401,F403  # type: ignore


class StatusCategory(BaseCategory):
    async def get(
        self,
        group_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "StatusStatus":
        """Method `status.get()`

        :param group_id:
        :param user_id: User ID or community ID. Use a negative value to designate a community ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("status.get", params)
        model = StatusGetResponse
        return model(**response).response

    async def set(
        self,
        group_id: typing.Optional[int] = None,
        text: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `status.set()`

        :param group_id: Identifier of a community to set a status in. If left blank the status is set to current user.
        :param text: Text of the new status.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("status.set", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("StatusCategory",)
