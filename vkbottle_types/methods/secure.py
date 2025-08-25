from typing import TYPE_CHECKING, List, Optional, Union

from vkbottle_types.codegen.methods.secure import SecureCategory as _SecureCategory  # type: ignore
from vkbottle_types.responses.secure import (
    SecureSetCounterArrayResponse,
    SecureSetCounterIntegerResponse,
    SecureSetCounterItem,
)

if TYPE_CHECKING:
    from vkbottle import ABCAPI  # type: ignore


class SecureCategory(_SecureCategory):  # type: ignore
    def __init__(self, api: "ABCAPI") -> None:
        super().__init__(api)

    async def set_counter(  # type: ignore
        self,
        counters: Optional[List[str]] = None,
        user_id: Optional[int] = None,
        counter: Optional[int] = None,
        increment: Optional[bool] = None,
        **kwargs,
    ) -> Union[int, List["SecureSetCounterItem"]]:
        """Sets a counter which is shown to the user in bold in the left menu.

        :param counters:
        :param user_id:
        :param counter: counter value.
        :param increment:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("secure.setCounter", params)
        model = SecureSetCounterArrayResponse if counters and counters.count(",") > 0 else SecureSetCounterIntegerResponse
        return model(**response).response


__all__ = ("SecureCategory",)
