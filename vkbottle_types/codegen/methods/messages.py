import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import (
    BaseUserGroupFields,
    MessagesChat,
    MessagesChatFull,
    MessagesGetConversationById,
    MessagesGetConversationByIdExtended,
    MessagesGetConversationMembers,
    MessagesLastActivity,
    MessagesLongpollParams,
    MessagesPinnedMessage,
    UsersFields,
)
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.base_response import DictResponse
from vkbottle_types.responses.messages import *  # noqa: F401,F403  # type: ignore


class MessagesCategory(BaseCategory):
    async def add_chat_user(
        self,
        chat_id: int,
        user_id: int | None = None,
        visible_messages_count: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.addChatUser()`

        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.addChatUser", params)
        model = BaseOkResponse
        return model(**response).response

    async def add_chat_users(
        self,
        chat_id: int | None = None,
        visible_messages_count: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesAddChatUsersResponseModel:
        """Method `messages.addChatUsers()`

        :param chat_id:
        :param visible_messages_count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.addChatUsers", params)
        model = MessagesAddChatUsersResponse
        return model(**response).response

    async def allow_messages_from_group(
        self,
        group_id: int,
        key: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.allowMessagesFromGroup()`

        :param group_id: Group ID.
        :param key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.allowMessagesFromGroup", params)
        model = BaseOkResponse
        return model(**response).response

    async def create_chat(
        self,
        group_id: int | None = None,
        title: str | None = None,
        user_ids: list[int] | None = None,
        **kwargs: typing.Any,
    ) -> MessagesCreateChatWithPeerIdsResponseModel:
        """Method `messages.createChat()`

        :param group_id:
        :param title: Chat title.
        :param user_ids: IDs of the users to be added to the chat.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.createChat", params)
        model = MessagesCreateChatWithPeerIdsResponse
        return model(**response).response

    async def delete(
        self,
        cmids: list[int] | None = None,
        delete_for_all: bool | None = None,
        group_id: int | None = None,
        message_ids: list[int] | None = None,
        peer_id: int | None = None,
        reason: int | None = None,
        spam: bool | None = None,
        **kwargs: typing.Any,
    ) -> list[MessagesDeleteFullResponseItem]:
        """Method `messages.delete()`

        :param cmids: Conversation message IDs.
        :param delete_for_all: '1' - delete message for for all.
        :param group_id: Group ID (for group messages with user access token)
        :param message_ids: Message IDs.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param reason: Reason for spam
        :param spam: '1' - to mark message as spam.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.delete", params)
        model = MessagesDeleteFullResponse
        return model(**response).response

    async def delete_chat_photo(
        self,
        chat_id: int,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesDeleteChatPhotoResponseModel:
        """Method `messages.deleteChatPhoto()`

        :param chat_id: Chat ID.
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.deleteChatPhoto", params)
        model = MessagesDeleteChatPhotoResponse
        return model(**response).response

    async def delete_conversation(
        self,
        group_id: int | None = None,
        peer_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesDeleteConversationResponseModel:
        """Method `messages.deleteConversation()`

        :param group_id: Group ID (for group messages with user access token)
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param user_id: User ID. To clear a chat history use 'chat_id'
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.deleteConversation", params)
        model = MessagesDeleteConversationResponse
        return model(**response).response

    async def delete_reaction(
        self,
        cmid: int,
        peer_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `messages.deleteReaction()`

        :param cmid:
        :param peer_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.deleteReaction", params)
        model = BaseBoolResponse
        return model(**response).response

    async def deny_messages_from_group(
        self,
        group_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.denyMessagesFromGroup()`

        :param group_id: Group ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.denyMessagesFromGroup", params)
        model = BaseOkResponse
        return model(**response).response

    async def edit(
        self,
        peer_id: int,
        attachment: str | None = None,
        cmid: int | None = None,
        disable_mentions: bool | None = None,
        dont_parse_links: bool | None = None,
        group_id: int | None = None,
        keep_forward_messages: bool | None = None,
        keep_snippets: bool | None = None,
        keyboard: str | None = None,
        lat: float | None = None,
        long: float | None = None,
        message: str | None = None,
        message_id: int | None = None,
        template: str | None = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `messages.edit()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'wall' - wall post, '<owner_id>' - ID of the media attachment owner. '<media_id>' - media attachment ID. Example: "photo100172_166443618"
        :param cmid:
        :param disable_mentions:
        :param dont_parse_links:
        :param group_id: Group ID (for group messages with user access token)
        :param keep_forward_messages: '1' - to keep forwarded, messages.
        :param keep_snippets: '1' - to keep attached snippets.
        :param keyboard:
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param message_id:
        :param template:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.edit", params)
        model = BaseBoolResponse
        return model(**response).response

    async def edit_chat(
        self,
        chat_id: int,
        title: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.editChat()`

        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.editChat", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def get_by_conversation_message_id(
        self,
        conversation_message_ids: list[int],
        peer_id: int,
        extended: typing.Literal[True],
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByConversationMessageIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_conversation_message_id(
        self,
        conversation_message_ids: list[int],
        peer_id: int,
        extended: typing.Literal[False] | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByConversationMessageIdResponseModel: ...

    async def get_by_conversation_message_id(
        self,
        conversation_message_ids: list[int],
        peer_id: int,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByConversationMessageIdExtendedResponseModel | MessagesGetByConversationMessageIdResponseModel:
        """Method `messages.getByConversationMessageId()`

        :param conversation_message_ids: Conversation message IDs.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getByConversationMessageId", params)
        model = self.get_model(
            ((("extended",), MessagesGetByConversationMessageIdExtendedResponse),),
            default=MessagesGetByConversationMessageIdResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_by_id(
        self,
        extended: typing.Literal[True],
        cmids: list[int] | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        message_ids: list[int] | None = None,
        peer_id: int | None = None,
        preview_length: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_id(
        self,
        extended: typing.Literal[False] | None = None,
        cmids: list[int] | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        message_ids: list[int] | None = None,
        peer_id: int | None = None,
        preview_length: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByIdResponseModel: ...

    async def get_by_id(
        self,
        extended: bool | None = None,
        cmids: list[int] | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        message_ids: list[int] | None = None,
        peer_id: int | None = None,
        preview_length: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByIdExtendedResponseModel | MessagesGetByIdResponseModel:
        """Method `messages.getById()`

        :param extended: Information whether the response should be extended
        :param cmids:
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param message_ids: Message IDs.
        :param peer_id:
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getById", params)
        model = self.get_model(
            ((("extended",), MessagesGetByIdExtendedResponse),),
            default=MessagesGetByIdResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_chat(
        self,
        chat_ids: list[int],
        fields: list[UsersFields],
        chat_id: int | None = None,
        name_case: str | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesChatFull": ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: list[int] | None = None,
        fields: list[UsersFields] | None = None,
        chat_id: int | None = None,
        name_case: str | None = None,
        **kwargs: typing.Any,
    ) -> list[MessagesChat]: ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: list[int],
        fields: list[UsersFields],
        chat_id: int | None = None,
        name_case: str | None = None,
        **kwargs: typing.Any,
    ) -> list[MessagesChatFull]: ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: list[int] | None = None,
        fields: list[UsersFields] | None = None,
        chat_id: int | None = None,
        name_case: str | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesChat": ...

    async def get_chat(
        self,
        chat_ids: list[int] | None = None,
        fields: list[UsersFields] | None = None,
        chat_id: int | None = None,
        name_case: str | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesChat | list[MessagesChat] | list[MessagesChatFull] | MessagesChatFull":
        """Method `messages.getChat()`

        :param chat_ids: Chat IDs.
        :param fields: Profile fields to return.
        :param chat_id: Chat ID.
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getChat", params)
        model = self.get_model(
            (
                (("chat_ids",), MessagesGetChatFieldsResponse),
                (("fields",), MessagesGetChatFieldsResponse),
            ),
            default=MessagesGetChatResponse,
            params=params,
        )
        return model(**response).response

    async def get_chat_preview(
        self,
        fields: list[UsersFields] | None = None,
        link: str | None = None,
        peer_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetChatPreviewResponseModel:
        """Method `messages.getChatPreview()`

        :param fields: Profile fields to return.
        :param link: Invitation link.
        :param peer_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getChatPreview", params)
        model = MessagesGetChatPreviewResponse
        return model(**response).response

    async def get_conversation_members(
        self,
        peer_id: int,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        member_ids: list[int] | None = None,
        offset: int | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesGetConversationMembers":
        """Method `messages.getConversationMembers()`

        :param peer_id: Peer ID.
        :param count:
        :param extended: Extended flag
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param member_ids:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getConversationMembers", params)
        model = MessagesGetConversationMembersResponse
        return model(**response).response

    async def get_conversations(
        self,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        filter: str | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        start_message_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetConversationsResponseModel:
        """Method `messages.getConversations()`

        :param count: Number of conversations to return.
        :param extended: '1' - return extra information about users and communities
        :param fields: Profile and communities fields to return.
        :param filter: Filter to apply: 'all' - all conversations, 'unread' - conversations with unread messages, 'important' - conversations, marked as important (only for community messages), 'unanswered' - conversations, marked as unanswered (only for community messages)
        :param group_id: Group ID (for group messages with group access token)
        :param offset: Offset needed to return a specific subset of conversations.
        :param start_message_id: ID of the message from what to return dialogs.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getConversations", params)
        model = MessagesGetConversationsResponse
        return model(**response).response

    @typing.overload
    async def get_conversations_by_id(
        self,
        peer_ids: list[int],
        extended: typing.Literal[True],
        fields: list[BaseUserGroupFields] | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesGetConversationByIdExtended": ...

    @typing.overload
    async def get_conversations_by_id(
        self,
        peer_ids: list[int],
        extended: typing.Literal[False] | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesGetConversationById": ...

    async def get_conversations_by_id(
        self,
        peer_ids: list[int],
        extended: bool | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesGetConversationById | MessagesGetConversationByIdExtended":
        """Method `messages.getConversationsById()`

        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getConversationsById", params)
        model = self.get_model(
            ((("extended",), MessagesGetConversationsByIdExtendedResponse),),
            default=MessagesGetConversationsByIdResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def get_history(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        rev: int | None = None,
        start_message_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryExtendedResponseModel: ...

    @typing.overload
    async def get_history(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        rev: int | None = None,
        start_message_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryResponseModel: ...

    async def get_history(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        rev: int | None = None,
        start_message_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryResponseModel | MessagesGetHistoryExtendedResponseModel:
        """Method `messages.getHistory()`

        :param extended: Information whether the response should be extended
        :param count: Number of messages to return.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param offset: Offset needed to return a specific subset of messages.
        :param peer_id:
        :param rev: Sort order: '1' - return messages in chronological order. '0' - return messages in reverse chronological order.
        :param start_message_id: Starting message ID from which to return history.
        :param user_id: ID of the user whose message history you want to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getHistory", params)
        model = self.get_model(
            ((("extended",), MessagesGetHistoryExtendedResponse),),
            default=MessagesGetHistoryResponse,
            params=params,
        )
        return model(**response).response

    async def get_history_attachments(
        self,
        attachment_position: int | None = None,
        attachment_types: list[
            typing.Literal[
                "app_action_games",
                "app_action_mini_apps",
                "audio",
                "audio_message",
                "clip",
                "doc",
                "graffiti",
                "link",
                "market",
                "photo",
                "share",
                "video",
                "wall",
            ]
        ]
        | None = None,
        cmid: int | None = None,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        max_forwards_level: int | None = None,
        media_type: str | None = None,
        message_video: bool | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        photo_sizes: bool | None = None,
        preserve_order: bool | None = None,
        start_from: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryAttachmentsResponseModel:
        """Method `messages.getHistoryAttachments()`

        :param attachment_position:
        :param attachment_types:
        :param cmid:
        :param count: Number of objects to return.
        :param extended:
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with group access token)
        :param max_forwards_level:
        :param media_type: Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param message_video:
        :param offset:
        :param peer_id: Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param photo_sizes: '1' - to return photo sizes in a
        :param preserve_order:
        :param start_from: Message ID to start return results from.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getHistoryAttachments", params)
        model = MessagesGetHistoryAttachmentsResponse
        return model(**response).response

    @typing.overload
    async def get_important_messages(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        preview_length: int | None = None,
        start_message_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetImportantMessagesExtendedResponseModel: ...

    @typing.overload
    async def get_important_messages(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        preview_length: int | None = None,
        start_message_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetImportantMessagesResponseModel: ...

    async def get_important_messages(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        preview_length: int | None = None,
        start_message_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetImportantMessagesExtendedResponseModel | MessagesGetImportantMessagesResponseModel:
        """Method `messages.getImportantMessages()`

        :param extended: Return extended properties
        :param count: Amount of needed important messages.
        :param fields: Actors fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param offset:
        :param preview_length: Maximum length of messages body.
        :param start_message_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getImportantMessages", params)
        model = self.get_model(
            ((("extended",), MessagesGetImportantMessagesExtendedResponse),),
            default=MessagesGetImportantMessagesResponse,
            params=params,
        )
        return model(**response).response

    async def get_intent_users(
        self,
        intent: str,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[str] | None = None,
        name_case: str | None = None,
        offset: int | None = None,
        subscribe_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetIntentUsersResponseModel:
        """Method `messages.getIntentUsers()`

        :param intent:
        :param count:
        :param extended:
        :param fields:
        :param name_case:
        :param offset:
        :param subscribe_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getIntentUsers", params)
        model = MessagesGetIntentUsersResponse
        return model(**response).response

    async def get_invite_link(
        self,
        peer_id: int,
        group_id: int | None = None,
        reset: bool | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetInviteLinkResponseModel:
        """Method `messages.getInviteLink()`

        :param peer_id: Destination ID.
        :param group_id: Group ID
        :param reset: 1 - to generate new link (revoke previous), 0 - to return previous link.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getInviteLink", params)
        model = MessagesGetInviteLinkResponse
        return model(**response).response

    async def get_last_activity(
        self,
        user_id: int,
        **kwargs: typing.Any,
    ) -> "MessagesLastActivity":
        """Method `messages.getLastActivity()`

        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLastActivity", params)
        model = MessagesGetLastActivityResponse
        return model(**response).response

    async def get_long_poll_history(
        self,
        credentials: bool | None = None,
        events_limit: int | None = None,
        extended: bool | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        last_n: int | None = None,
        lp_version: int | None = None,
        max_msg_id: int | None = None,
        msgs_limit: int | None = None,
        onlines: bool | None = None,
        preview_length: int | None = None,
        pts: int | None = None,
        ts: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetLongPollHistoryResponseModel:
        """Method `messages.getLongPollHistory()`

        :param credentials:
        :param events_limit: Maximum number of events to return.
        :param extended:
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with user access token)
        :param last_n:
        :param lp_version:
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param msgs_limit: Maximum number of messages to return.
        :param onlines: '1' - to return history with online users only.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param pts: Last value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLongPollHistory", params)
        model = MessagesGetLongPollHistoryResponse
        return model(**response).response

    async def get_long_poll_server(
        self,
        group_id: int | None = None,
        lp_version: int | None = None,
        need_pts: bool | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesLongpollParams":
        """Method `messages.getLongPollServer()`

        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        :param need_pts: '1' - to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLongPollServer", params)
        model = MessagesGetLongPollServerResponse
        return model(**response).response

    async def get_messages_reactions(
        self,
        cmids: list[int],
        peer_id: int,
        **kwargs: typing.Any,
    ) -> MessagesGetMessagesReactionsResponseModel:
        """Method `messages.getMessagesReactions()`

        :param cmids:
        :param peer_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getMessagesReactions", params)
        model = MessagesGetMessagesReactionsResponse
        return model(**response).response

    async def get_reacted_peers(
        self,
        cmid: int,
        peer_id: int,
        reaction_id: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetReactedPeersResponseModel:
        """Method `messages.getReactedPeers()`

        :param cmid:
        :param peer_id:
        :param reaction_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getReactedPeers", params)
        model = MessagesGetReactedPeersResponse
        return model(**response).response

    async def get_reactions_assets(
        self,
        client_version: int | None = None,
        **kwargs: typing.Any,
    ) -> MessagesGetReactionsAssetsResponseModel:
        """Method `messages.getReactionsAssets()`

        :param client_version:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getReactionsAssets", params)
        model = MessagesGetReactionsAssetsResponse
        return model(**response).response

    async def is_messages_from_group_allowed(
        self,
        group_id: int,
        user_id: int,
        **kwargs: typing.Any,
    ) -> MessagesIsMessagesFromGroupAllowedResponseModel:
        """Method `messages.isMessagesFromGroupAllowed()`

        :param group_id: Group ID.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.isMessagesFromGroupAllowed", params)
        model = MessagesIsMessagesFromGroupAllowedResponse
        return model(**response).response

    async def join_chat_by_invite_link(
        self,
        link: str,
        **kwargs: typing.Any,
    ) -> MessagesJoinChatByInviteLinkResponseModel:
        """Method `messages.joinChatByInviteLink()`

        :param link: Invitation link.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.joinChatByInviteLink", params)
        model = MessagesJoinChatByInviteLinkResponse
        return model(**response).response

    async def mark_as_answered_conversation(
        self,
        peer_id: int,
        answered: bool | None = None,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.markAsAnsweredConversation()`

        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' - to mark as answered, '0' - to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsAnsweredConversation", params)
        model = BaseOkResponse
        return model(**response).response

    async def mark_as_important(
        self,
        important: int | None = None,
        message_ids: list[int] | None = None,
        **kwargs: typing.Any,
    ) -> list[int]:
        """Method `messages.markAsImportant()`

        :param important: '1' - to add a star (mark as important), '0' - to remove the star
        :param message_ids: IDs of messages to mark as important.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsImportant", params)
        model = MessagesMarkAsImportantDeprecatedResponse
        return model(**response).response

    async def mark_as_important_conversation(
        self,
        peer_id: int,
        group_id: int | None = None,
        important: bool | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.markAsImportantConversation()`

        :param peer_id: ID of conversation to mark as important.
        :param group_id: Group ID (for group messages with group access token)
        :param important: '1' - to add a star (mark as important), '0' - to remove the star
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsImportantConversation", params)
        model = BaseOkResponse
        return model(**response).response

    async def mark_as_read(
        self,
        group_id: int | None = None,
        mark_conversation_as_read: bool | None = None,
        message_ids: list[int] | None = None,
        peer_id: int | None = None,
        start_message_id: int | None = None,
        up_to_cmid: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.markAsRead()`

        :param group_id: Group ID (for group messages with user access token)
        :param mark_conversation_as_read:
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param up_to_cmid:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsRead", params)
        model = BaseOkResponse
        return model(**response).response

    async def mark_reactions_as_read(
        self,
        peer_id: int,
        cmids: list[int] | None = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `messages.markReactionsAsRead()`

        :param peer_id:
        :param cmids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markReactionsAsRead", params)
        model = BaseBoolResponse
        return model(**response).response

    async def mute_chat_mentions(
        self,
        mention_status: str,
        peer_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.muteChatMentions()`

        :param mention_status:
        :param peer_id: Chat id
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.muteChatMentions", params)
        model = BaseOkResponse
        return model(**response).response

    async def pin(
        self,
        peer_id: int,
        cmid: int | None = None,
        message_id: int | None = None,
        **kwargs: typing.Any,
    ) -> "MessagesPinnedMessage":
        """Method `messages.pin()`

        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param cmid: Conversation message ID
        :param message_id: Message ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.pin", params)
        model = MessagesPinResponse
        return model(**response).response

    async def remove_chat_user(
        self,
        chat_id: int,
        member_id: int | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.removeChatUser()`

        :param chat_id: Chat ID.
        :param member_id:
        :param user_id: ID of the user to be removed from the chat.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.removeChatUser", params)
        model = BaseOkResponse
        return model(**response).response

    async def restore(
        self,
        cmid: int | None = None,
        group_id: int | None = None,
        message_id: int | None = None,
        peer_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.restore()`

        :param cmid:
        :param group_id: Group ID (for group messages with user access token)
        :param message_id: ID of a previously-deleted message to restore.
        :param peer_id: Destination ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.restore", params)
        model = BaseOkResponse
        return model(**response).response

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        date: int | None = None,
        fields: list[str] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        preview_length: int | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        date: int | None = None,
        fields: list[str] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        preview_length: int | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchResponseModel: ...

    async def search(
        self,
        extended: bool | None = None,
        count: int | None = None,
        date: int | None = None,
        fields: list[str] | None = None,
        group_id: int | None = None,
        offset: int | None = None,
        peer_id: int | None = None,
        preview_length: int | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchExtendedResponseModel | MessagesSearchResponseModel:
        """Method `messages.search()`

        :param extended:
        :param count: Number of messages to return.
        :param date: Date to search message before in Unixtime.
        :param fields:
        :param group_id: Group ID (for group messages with group access token)
        :param offset: Offset needed to return a specific subset of messages.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param q: Search query string.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.search", params)
        model = self.get_model(
            ((("extended",), MessagesSearchExtendedResponse),),
            default=MessagesSearchResponse,
            params=params,
        )
        return model(**response).response

    @typing.overload
    async def search_conversations(
        self,
        extended: typing.Literal[True],
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchConversationsExtendedResponseModel: ...

    @typing.overload
    async def search_conversations(
        self,
        extended: typing.Literal[False] | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchConversationsResponseModel: ...

    async def search_conversations(
        self,
        extended: bool | None = None,
        count: int | None = None,
        fields: list[UsersFields] | None = None,
        group_id: int | None = None,
        q: str | None = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchConversationsExtendedResponseModel | MessagesSearchConversationsResponseModel:
        """Method `messages.searchConversations()`

        :param extended: '1' - return extra information about users and communities
        :param count: Maximum number of results.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)
        :param q: Search query string.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.searchConversations", params)
        model = self.get_model(
            ((("extended",), MessagesSearchConversationsExtendedResponse),),
            default=MessagesSearchConversationsResponse,
            params=params,
        )
        return model(**response).response

    async def send(
        self,
        attachment: str | None = None,
        chat_id: int | None = None,
        content_source: str | None = None,
        disable_mentions: bool | None = None,
        domain: str | None = None,
        dont_parse_links: bool | None = None,
        forward: str | None = None,
        forward_messages: list[int] | None = None,
        group_id: int | None = None,
        intent: str | None = None,
        keyboard: str | None = None,
        lat: float | None = None,
        long: float | None = None,
        message: str | None = None,
        payload: str | None = None,
        peer_id: int | None = None,
        peer_ids: list[int] | None = None,
        random_id: int | None = None,
        reply_to: int | None = None,
        sticker_id: int | None = None,
        subscribe_id: int | None = None,
        template: str | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> dict[str, typing.Any]:
        """Method `messages.send()`

        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'wall' - wall post, '<owner_id>' - ID of the media attachment owner. '<media_id>' - media attachment ID. Example: "photo100172_166443618"
        :param chat_id: ID of conversation the message will relate to.
        :param content_source: JSON describing the content source in the message
        :param disable_mentions:
        :param domain: User's short address (for example, 'illarionov').
        :param dont_parse_links:
        :param forward: JSON describing the forwarded message or reply
        :param forward_messages: ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param group_id: Group ID (for group messages with group access token)
        :param intent:
        :param keyboard:
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param payload:
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param peer_ids: IDs of message recipients. (See peer_id)
        :param random_id: Unique identifier to avoid resending the message.
        :param reply_to:
        :param sticker_id: Sticker id.
        :param subscribe_id:
        :param template:
        :param user_id: User ID (by default - current user).
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.send", params)
        model = DictResponse
        return model(**response).response

    async def send_message_event_answer(
        self,
        event_id: str,
        peer_id: int,
        user_id: int,
        event_data: str | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.sendMessageEventAnswer()`

        :param event_id:
        :param peer_id:
        :param user_id:
        :param event_data:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.sendMessageEventAnswer", params)
        model = BaseOkResponse
        return model(**response).response

    async def send_reaction(
        self,
        cmid: int,
        peer_id: int,
        reaction_id: int,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `messages.sendReaction()`

        :param cmid:
        :param peer_id:
        :param reaction_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.sendReaction", params)
        model = BaseBoolResponse
        return model(**response).response

    async def set_activity(
        self,
        group_id: int | None = None,
        peer_id: int | None = None,
        type: str | None = None,
        user_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.setActivity()`

        :param group_id: Group ID (for group messages with group access token)
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param type: 'typing' - user has started to type.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.setActivity", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_chat_photo(
        self,
        file: str,
        **kwargs: typing.Any,
    ) -> MessagesSetChatPhotoResponseModel:
        """Method `messages.setChatPhoto()`

        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.setChatPhoto", params)
        model = MessagesSetChatPhotoResponse
        return model(**response).response

    async def unpin(
        self,
        peer_id: int,
        group_id: int | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `messages.unpin()`

        :param peer_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.unpin", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("MessagesCategory",)
