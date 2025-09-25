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
        user_id: typing.Optional[int] = None,
        visible_messages_count: typing.Optional[int] = None,
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
        chat_id: typing.Optional[int] = None,
        visible_messages_count: typing.Optional[int] = None,
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
        key: typing.Optional[str] = None,
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
        group_id: typing.Optional[int] = None,
        title: typing.Optional[str] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
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
        cmids: typing.Optional[typing.List[int]] = None,
        delete_for_all: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        reason: typing.Optional[int] = None,
        spam: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> typing.List[MessagesDeleteFullResponseItem]:
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
        group_id: typing.Optional[int] = None,
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
        group_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
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
        attachment: typing.Optional[str] = None,
        cmid: typing.Optional[int] = None,
        disable_mentions: typing.Optional[bool] = None,
        dont_parse_links: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        keep_forward_messages: typing.Optional[bool] = None,
        keep_snippets: typing.Optional[bool] = None,
        keyboard: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
        message: typing.Optional[str] = None,
        message_id: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
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
        title: typing.Optional[str] = None,
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
        conversation_message_ids: typing.List[int],
        peer_id: int,
        extended: typing.Literal[True],
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByConversationMessageIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_conversation_message_id(
        self,
        conversation_message_ids: typing.List[int],
        peer_id: int,
        extended: typing.Optional[typing.Literal[False]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByConversationMessageIdResponseModel: ...

    async def get_by_conversation_message_id(
        self,
        conversation_message_ids: typing.List[int],
        peer_id: int,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MessagesGetByConversationMessageIdExtendedResponseModel, MessagesGetByConversationMessageIdResponseModel]:
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
        cmids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByIdExtendedResponseModel: ...

    @typing.overload
    async def get_by_id(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        cmids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetByIdResponseModel: ...

    async def get_by_id(
        self,
        extended: typing.Optional[bool] = None,
        cmids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MessagesGetByIdResponseModel, MessagesGetByIdExtendedResponseModel]:
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
        chat_ids: typing.List[int],
        fields: typing.List[UsersFields],
        chat_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "MessagesChatFull": ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        chat_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[MessagesChat]: ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: typing.List[int],
        fields: typing.List[UsersFields],
        chat_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.List[MessagesChatFull]: ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        chat_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> "MessagesChat": ...

    async def get_chat(
        self,
        chat_ids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        chat_id: typing.Optional[int] = None,
        name_case: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union["MessagesChatFull", typing.List[MessagesChatFull], "MessagesChat", typing.List[MessagesChat]]:
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
        fields: typing.Optional[typing.List[UsersFields]] = None,
        link: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
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
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        member_ids: typing.Optional[typing.List[int]] = None,
        offset: typing.Optional[int] = None,
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
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filter: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
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
        peer_ids: typing.List[int],
        extended: typing.Literal[True],
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "MessagesGetConversationByIdExtended": ...

    @typing.overload
    async def get_conversations_by_id(
        self,
        peer_ids: typing.List[int],
        extended: typing.Optional[typing.Literal[False]] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> "MessagesGetConversationById": ...

    async def get_conversations_by_id(
        self,
        peer_ids: typing.List[int],
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union["MessagesGetConversationById", "MessagesGetConversationByIdExtended"]:
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
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        rev: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryExtendedResponseModel: ...

    @typing.overload
    async def get_history(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        rev: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryResponseModel: ...

    async def get_history(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        rev: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MessagesGetHistoryExtendedResponseModel, MessagesGetHistoryResponseModel]:
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
        attachment_position: typing.Optional[int] = None,
        attachment_types: typing.Optional[
            typing.List[
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
        ] = None,
        cmid: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        max_forwards_level: typing.Optional[int] = None,
        media_type: typing.Optional[str] = None,
        message_video: typing.Optional[bool] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        photo_sizes: typing.Optional[bool] = None,
        preserve_order: typing.Optional[bool] = None,
        start_from: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetHistoryAttachmentsResponseModel:
        """Method `messages.getHistoryAttachments()`

        :param attachment_position:
        :param attachment_types:
        :param cmid:
        :param count: Number of objects to return.
        :param extended:
        :param fields: Additional profile [vk.ru/dev/fields|fields] to return.
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
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetImportantMessagesExtendedResponseModel: ...

    @typing.overload
    async def get_important_messages(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetImportantMessagesResponseModel: ...

    async def get_important_messages(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MessagesGetImportantMessagesExtendedResponseModel, MessagesGetImportantMessagesResponseModel]:
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
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        name_case: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
        subscribe_id: typing.Optional[int] = None,
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
        group_id: typing.Optional[int] = None,
        reset: typing.Optional[bool] = None,
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
        credentials: typing.Optional[bool] = None,
        events_limit: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        last_n: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
        max_msg_id: typing.Optional[int] = None,
        msgs_limit: typing.Optional[int] = None,
        onlines: typing.Optional[bool] = None,
        preview_length: typing.Optional[int] = None,
        pts: typing.Optional[int] = None,
        ts: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> MessagesGetLongPollHistoryResponseModel:
        """Method `messages.getLongPollHistory()`

        :param credentials:
        :param events_limit: Maximum number of events to return.
        :param extended:
        :param fields: Additional profile [vk.ru/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with user access token)
        :param last_n:
        :param lp_version:
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param msgs_limit: Maximum number of messages to return.
        :param onlines: '1' - to return history with online users only.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param pts: Last value of 'pts' parameter returned from the Long Poll server or by using [vk.ru/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.ru/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLongPollHistory", params)
        model = MessagesGetLongPollHistoryResponse
        return model(**response).response

    async def get_long_poll_server(
        self,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
        need_pts: typing.Optional[bool] = None,
        **kwargs: typing.Any,
    ) -> "MessagesLongpollParams":
        """Method `messages.getLongPollServer()`

        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        :param need_pts: '1' - to return the 'pts' field, needed for the [vk.ru/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLongPollServer", params)
        model = MessagesGetLongPollServerResponse
        return model(**response).response

    async def get_messages_reactions(
        self,
        cmids: typing.List[int],
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
        reaction_id: typing.Optional[int] = None,
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
        client_version: typing.Optional[int] = None,
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
        answered: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
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
        important: typing.Optional[int] = None,
        message_ids: typing.Optional[typing.List[int]] = None,
        **kwargs: typing.Any,
    ) -> typing.List[int]:
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
        group_id: typing.Optional[int] = None,
        important: typing.Optional[bool] = None,
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
        group_id: typing.Optional[int] = None,
        mark_conversation_as_read: typing.Optional[bool] = None,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        up_to_cmid: typing.Optional[int] = None,
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
        cmids: typing.Optional[typing.List[int]] = None,
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
        cmid: typing.Optional[int] = None,
        message_id: typing.Optional[int] = None,
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
        member_id: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
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
        cmid: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        message_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
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
        count: typing.Optional[int] = None,
        date: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchExtendedResponseModel: ...

    @typing.overload
    async def search(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        date: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchResponseModel: ...

    async def search(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        date: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MessagesSearchResponseModel, MessagesSearchExtendedResponseModel]:
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
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchConversationsExtendedResponseModel: ...

    @typing.overload
    async def search_conversations(
        self,
        extended: typing.Optional[typing.Literal[False]] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> MessagesSearchConversationsResponseModel: ...

    async def search_conversations(
        self,
        extended: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        q: typing.Optional[str] = None,
        **kwargs: typing.Any,
    ) -> typing.Union[MessagesSearchConversationsResponseModel, MessagesSearchConversationsExtendedResponseModel]:
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
        attachment: typing.Optional[str] = None,
        chat_id: typing.Optional[int] = None,
        content_source: typing.Optional[str] = None,
        disable_mentions: typing.Optional[bool] = None,
        domain: typing.Optional[str] = None,
        dont_parse_links: typing.Optional[bool] = None,
        forward: typing.Optional[str] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        group_id: typing.Optional[int] = None,
        intent: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
        message: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        peer_ids: typing.Optional[typing.List[int]] = None,
        random_id: typing.Optional[int] = None,
        reply_to: typing.Optional[int] = None,
        sticker_id: typing.Optional[int] = None,
        subscribe_id: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
        **kwargs: typing.Any,
    ) -> typing.Dict[str, typing.Any]:
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
        event_data: typing.Optional[str] = None,
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
        group_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        user_id: typing.Optional[int] = None,
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

        :param file: Upload URL from the 'response' field returned by the [vk.ru/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.setChatPhoto", params)
        model = MessagesSetChatPhotoResponse
        return model(**response).response

    async def unpin(
        self,
        peer_id: int,
        group_id: typing.Optional[int] = None,
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
