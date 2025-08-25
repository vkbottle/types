import typing

from vkbottle_types.codegen.methods.utils import UtilsCategory as _UtilsCategory  # type: ignore
from vkbottle_types.objects import UtilsDomainResolved
from vkbottle_types.responses import UtilsResolveScreenNameResponse  # noqa: F401,F403  # type: ignore


class UtilsCategory(_UtilsCategory):  # type: ignore
    async def resolve_screen_name(  # type: ignore
        self,
        screen_name: str,
        **kwargs: typing.Any,
    ) -> typing.Union[UtilsDomainResolved, typing.List[typing.Any]]:
        """Method `utils.resolveScreenName()`

        :param screen_name: Screen name of the user, community (e.g., 'apiclub,' 'andrew', or 'rules_of_war'), or application.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("utils.resolveScreenName", params)
        model = UtilsResolveScreenNameResponse
        return model(**response).response


__all__ = ("UtilsCategory",)
