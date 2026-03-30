import typing

from typing_extensions import Literal

from vkbottle_types.codegen.methods.messages import MessagesCategory as _MessagesCategory  # type: ignore
from vkbottle_types.objects import UsersFields
from vkbottle_types.responses.messages import (
    MessagesChat,
    MessagesChatFull,
    MessagesGetChatChatIdsFieldsResponse,
    MessagesGetChatChatIdsResponse,
    MessagesGetChatFieldsResponse,
    MessagesGetChatResponse,
    MessagesSendDeprecatedResponse,
    MessagesSendPeerIdsResponse,
    MessagesSendUserIdsResponse,
    MessagesSendUserIdsResponseItem,
)


class MessagesCategory(_MessagesCategory):  # type: ignore
    @typing.overload  # type: ignore
    async def send(  # type: ignore
        self,
        user_id: int | None = None,
        random_id: int | None = None,
        peer_id: int | None = None,
        peer_ids: list[int] | None = None,
        domain: str | None = None,
        chat_id: int | None = None,
        user_ids: Literal[None] | None = ...,
        message: str | None = None,
        lat: float | None = None,
        long: float | None = None,
        attachment: str | None = None,
        reply_to: int | None = None,
        forward_messages: list[int] | None = None,
        forward: str | None = None,
        sticker_id: int | None = None,
        group_id: int | None = None,
        keyboard: str | None = None,
        template: str | None = None,
        payload: str | None = None,
        content_source: str | None = None,
        dont_parse_links: bool | None = None,
        disable_mentions: bool | None = None,
        intent: (
            Literal[
                "account_update",
                "bot_ad_invite",
                "bot_ad_promo",
                "confirmed_notification",
                "customer_support",
                "default",
                "game_notification",
                "moderated_newsletter",
                "non_promo_newsletter",
                "promo_newsletter",
                "purchase_update",
            ]
            | None
        ) = None,
        subscribe_id: int | None = None,
    ) -> int: ...

    @typing.overload
    async def send(
        self,
        user_id: int | None = None,
        random_id: int | None = None,
        peer_id: int | None = None,
        peer_ids: list[int] | None = None,
        domain: str | None = None,
        chat_id: int | None = None,
        user_ids: list[int] = ...,
        message: str | None = None,
        lat: float | None = None,
        long: float | None = None,
        attachment: str | None = None,
        reply_to: int | None = None,
        forward_messages: list[int] | None = None,
        forward: str | None = None,
        sticker_id: int | None = None,
        group_id: int | None = None,
        keyboard: str | None = None,
        template: str | None = None,
        payload: str | None = None,
        content_source: str | None = None,
        dont_parse_links: bool | None = None,
        disable_mentions: bool | None = None,
        intent: (
            Literal[
                "account_update",
                "bot_ad_invite",
                "bot_ad_promo",
                "confirmed_notification",
                "customer_support",
                "default",
                "game_notification",
                "moderated_newsletter",
                "non_promo_newsletter",
                "promo_newsletter",
                "purchase_update",
            ]
            | None
        ) = None,
        subscribe_id: int | None = None,
    ) -> list[MessagesSendUserIdsResponseItem]: ...

    @typing.overload
    async def send(
        self,
        user_id: int | None = None,
        random_id: int | None = None,
        peer_id: int | None = None,
        peer_ids: list[int] = ...,
        domain: str | None = None,
        chat_id: int | None = None,
        user_ids: list[int] | None = None,
        message: str | None = None,
        lat: float | None = None,
        long: float | None = None,
        attachment: str | None = None,
        reply_to: int | None = None,
        forward_messages: list[int] | None = None,
        forward: str | None = None,
        sticker_id: int | None = None,
        group_id: int | None = None,
        keyboard: str | None = None,
        template: str | None = None,
        payload: str | None = None,
        content_source: str | None = None,
        dont_parse_links: bool | None = None,
        disable_mentions: bool | None = None,
        intent: (
            Literal[
                "account_update",
                "bot_ad_invite",
                "bot_ad_promo",
                "confirmed_notification",
                "customer_support",
                "default",
                "game_notification",
                "moderated_newsletter",
                "non_promo_newsletter",
                "promo_newsletter",
                "purchase_update",
            ]
            | None
        ) = None,
        subscribe_id: int | None = None,
    ) -> list[MessagesSendUserIdsResponseItem]: ...

    async def send(
        self,
        user_id=None,
        random_id=None,
        peer_id=None,
        peer_ids=None,
        domain=None,
        chat_id=None,
        user_ids=None,
        message=None,
        lat=None,
        long=None,
        attachment=None,
        reply_to=None,
        forward_messages=None,
        forward=None,
        sticker_id=None,
        group_id=None,
        keyboard=None,
        template=None,
        payload=None,
        content_source=None,
        dont_parse_links=None,
        disable_mentions=None,
        intent=None,
        subscribe_id=None,
        **kwargs,
    ) -> list[MessagesSendUserIdsResponseItem] | int:
        """Sends a message.

        :param user_id: User ID (by default — current user).
        :param random_id: Unique identifier to avoid resending the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param peer_ids: IDs of message recipients. (See peer_id)
        :param domain: User's short address (for example, 'illarionov').
        :param chat_id: ID of conversation the message will relate to.
        :param user_ids: IDs of message recipients (if new conversation shall be started).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to:
        :param forward_messages: ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param forward: JSON describing the forwarded message or reply
        :param sticker_id: Sticker id.
        :param group_id: Group ID (for group messages with group access token)
        :param keyboard:
        :param template:
        :param payload:
        :param content_source: JSON describing the content source in the message
        :param dont_parse_links:
        :param disable_mentions:
        :param intent:
        :param subscribe_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.send", params)
        model = self.get_model(
            (
                (("user_ids",), MessagesSendUserIdsResponse),
                (("peer_ids",), MessagesSendPeerIdsResponse),
            ),
            default=MessagesSendDeprecatedResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload  # type: ignore
    async def get_chat(
        self,
        *,
        chat_id: int,
        name_case: str | None = None,
    ) -> "MessagesChat": ...

    @typing.overload
    async def get_chat(
        self,
        *,
        chat_id: int,
        fields: list[UsersFields],
        name_case: str | None = None,
    ) -> "MessagesChatFull": ...

    @typing.overload
    async def get_chat(
        self,
        *,
        chat_ids: list[int],
        name_case: str | None = None,
    ) -> list[MessagesChat]: ...

    @typing.overload
    async def get_chat(
        self,
        *,
        chat_ids: list[int],
        fields: list[UsersFields],
        name_case: str | None = None,
    ) -> list[MessagesChatFull]: ...

    async def get_chat(
        self,
        fields: list[UsersFields] | None = None,
        chat_ids: list[int] | None = None,
        chat_id: int | None = None,
        name_case: str | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesChat" | "MessagesChatFull" | list[MessagesChat] | list[MessagesChatFull]:
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
                (("fields", "chat_id"), MessagesGetChatFieldsResponse),
                (("fields", "chat_ids"), MessagesGetChatChatIdsFieldsResponse),
                (("chat_id",), MessagesGetChatResponse),
                (("chat_ids",), MessagesGetChatChatIdsResponse),
            ),
            default=MessagesGetChatResponse,
            params=params,
        )
        return model(**response).response


__all__ = ("MessagesCategory",)
