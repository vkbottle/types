import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.base import (
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.calls import *  # noqa: F401,F403  # type: ignore


class CallsCategory(BaseCategory):
    async def force_finish(
        self,
        call_id: str,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `calls.forceFinish()`

        :param call_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("calls.forceFinish", params)
        model = BaseOkResponse
        return model(**response).response

    async def start(
        self,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> CallsStartResponseModel:
        """Method `calls.start()`

        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("calls.start", params)
        model = CallsStartResponse
        return model(**response).response


__all__ = ("CallsCategory",)
