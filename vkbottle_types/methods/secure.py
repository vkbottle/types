from typing import List, Optional, Union

from vkbottle_types.codegen.methods.secure import SecureCategory
from vkbottle_types.responses.secure import (
    SecureSetCounterItem,
    SetCounterArrayResponse,
    SetCounterIntegerResponse,
)


class SecureCategory(SecureCategory):
    async def set_counter(
        self,
        counters: Optional[List[str]] = None,
        user_id: Optional[int] = None,
        counter: Optional[int] = None,
        increment: Optional[bool] = None,
        **kwargs
    ) -> Union[int, List["SecureSetCounterItem"]]:
        """Sets a counter which is shown to the user in bold in the left menu.

        :param counters:
        :param user_id:
        :param counter: counter value.
        :param increment:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.setCounter", params)
        if counters and counters.count(",") > 0:
            model = SetCounterArrayResponse
        else:
            model = SetCounterIntegerResponse
        return model(**response).response


__all__ = ("SecureCategory",)
