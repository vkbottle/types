import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import (
    MessagesChat,
    MessagesChatFull,
    UsersFields,
)
from vkbottle_types.responses.messages import *  # noqa: F401,F403


class MessagesCategory(BaseCategory):
    @typing.overload
    async def get_chat(
        self,
        *,
        chat_id: int,
        name_case: typing.Optional[str] = None,
    ) -> "MessagesChat": ...

    @typing.overload
    async def get_chat(
        self,
        *,
        chat_id: int,
        fields: typing.List[UsersFields],
        name_case: typing.Optional[str] = None,
    ) -> "MessagesChatFull": ...

    @typing.overload
    async def get_chat(
        self,
        *,
        chat_ids: typing.List[int],
        name_case: typing.Optional[str] = None,
    ) -> typing.List[MessagesChat]: ...

    @typing.overload
    async def get_chat(
        self,
        *,
        chat_ids: typing.List[int],
        fields: typing.List[UsersFields],
        name_case: typing.Optional[str] = None,
    ) -> typing.List[MessagesChatFull]: ...

    async def get_chat(
        self,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        chat_ids: typing.Optional[typing.List[int]] = None,
        chat_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[
        typing.List[MessagesChat],
        "MessagesChatFull",
        typing.List[MessagesChatFull],
        "MessagesChat",
    ]:
        """Method `messages.getChat()`

        :param fields: Profile fields to return.
        :param chat_ids: Chat IDs.
        :param chat_id: Chat ID.
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getChat", params)
        model = self.get_model(
            (
                (("fields", "chat_ids"), MessagesGetChatChatIdsFieldsResponse),
                (("fields", "chat_id"), MessagesGetChatChatIdsFieldsResponse),
                (("fields",), MessagesGetChatFieldsResponse),
                (("chat_ids",), MessagesGetChatChatIdsResponse),
            ),
            default=MessagesGetChatResponse,
            params=params,
        )
        return model(**response).response
