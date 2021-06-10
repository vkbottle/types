import typing
from .base_category import BaseCategory
from vkbottle_types.responses import base, messages


class MessagesCategory(BaseCategory):
    async def add_chat_user(
        self,
        chat_id: int,
        user_id: typing.Optional[int] = None,
        visible_messages_count: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Adds a new user to a chat.
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.addChatUser", params)
        model = base.OkResponse
        return model(**response).response

    async def allow_messages_from_group(
        self, group_id: int, key: typing.Optional[str] = None, **kwargs
    ) -> int:
        """Allows sending messages from community to the current user.
        :param group_id: Group ID.
        :param key:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.allowMessagesFromGroup", params)
        model = base.OkResponse
        return model(**response).response

    async def create_chat(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        title: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Creates a chat with several participants.
        :param user_ids: IDs of the users to be added to the chat.
        :param title: Chat title.
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.createChat", params)
        model = messages.CreateChatResponse
        return model(**response).response

    async def delete(
        self,
        message_ids: typing.Optional[typing.List[int]] = None,
        spam: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        delete_for_all: typing.Optional[bool] = None,
        peer_id: typing.Optional[int] = None,
        conversation_message_ids: typing.Optional[typing.List[int]] = None,
        **kwargs
    ) -> typing.Dict[str, int]:
        """Deletes one or more messages.
        :param message_ids: Message IDs.
        :param spam: '1' — to mark message as spam.
        :param group_id: Group ID (for group messages with user access token)
        :param delete_for_all: '1' — delete message for for all.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: Conversation message IDs.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.delete", params)
        model = messages.DeleteResponse
        return model(**response).response

    async def delete_chat_photo(
        self, chat_id: int, group_id: typing.Optional[int] = None, **kwargs
    ) -> messages.DeleteChatPhotoResponseModel:
        """Deletes a chat's cover picture.
        :param chat_id: Chat ID.
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.deleteChatPhoto", params)
        model = messages.DeleteChatPhotoResponse
        return model(**response).response

    async def delete_conversation(
        self,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.DeleteConversationResponseModel:
        """Deletes all private messages in a conversation.
        :param user_id: User ID. To clear a chat history use 'chat_id'
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with user access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.deleteConversation", params)
        model = messages.DeleteConversationResponse
        return model(**response).response

    async def deny_messages_from_group(
        self, group_id: int, **kwargs
    ) -> int:
        """Denies sending message from community to the current user.
        :param group_id: Group ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.denyMessagesFromGroup", params)
        model = base.OkResponse
        return model(**response).response

    async def edit(
        self,
        peer_id: int,
        message: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
        keep_forward_messages: typing.Optional[bool] = None,
        keep_snippets: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        dont_parse_links: typing.Optional[bool] = None,
        message_id: typing.Optional[int] = None,
        conversation_message_id: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
        **kwargs
    ) -> messages.BaseBoolInt:
        """Edits the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param keep_forward_messages: '1' — to keep forwarded, messages.
        :param keep_snippets: '1' — to keep attached snippets.
        :param group_id: Group ID (for group messages with user access token)
        :param dont_parse_links:
        :param message_id:
        :param conversation_message_id:
        :param template:
        :param keyboard:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.edit", params)
        model = messages.EditResponse
        return model(**response).response

    async def edit_chat(
        self, chat_id: int, title: typing.Optional[str] = None, **kwargs
    ) -> int:
        """Edits the title of a chat.
        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.editChat", params)
        model = base.OkResponse
        return model(**response).response

    async def get_by_conversation_message_id(
        self,
        peer_id: int,
        conversation_message_ids: typing.List[int],
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetByConversationMessageIdResponseModel:
        """Returns messages by their IDs within the conversation.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: Conversation message IDs.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getByConversationMessageId", params)
        model = messages.GetByConversationMessageIdResponse
        return model(**response).response

    async def get_by_id(
        self,
        message_ids: typing.List[int],
        preview_length: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetByIdResponseModel:
        """Returns messages by their IDs.
        :param message_ids: Message IDs.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getById", params)
        model = self.get_model(
            {("extended",): messages.GetByIdExtendedResponse},
            default=messages.GetByIdResponse,
            params=params,
        )
        return model(**response).response

    async def get_chat_preview(
        self,
        peer_id: typing.Optional[int] = None,
        link: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> messages.GetChatPreviewResponseModel:
        """messages.getChatPreview method
        :param peer_id:
        :param link: Invitation link.
        :param fields: Profile fields to return.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getChatPreview", params)
        model = messages.GetChatPreviewResponse
        return model(**response).response

    async def get_conversation_members(
        self,
        peer_id: int,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetConversationMembersResponseModel:
        """Returns a list of IDs of users participating in a chat.
        :param peer_id: Peer ID.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getConversationMembers", params)
        model = messages.GetConversationMembersResponse
        return model(**response).response

    async def get_conversations(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        filter: typing.Optional[str] = None,
        extended: typing.Optional[bool] = None,
        start_message_id: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetConversationsResponseModel:
        """Returns a list of the current user's conversations.
        :param offset: Offset needed to return a specific subset of conversations.
        :param count: Number of conversations to return.
        :param filter: Filter to apply: 'all' — all conversations, 'unread' — conversations with unread messages, 'important' — conversations, marked as important (only for community messages), 'unanswered' — conversations, marked as unanswered (only for community messages)
        :param extended: '1' — return extra information about users and communities
        :param start_message_id: ID of the message from what to return dialogs.
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getConversations", params)
        model = messages.GetConversationsResponse
        return model(**response).response

    async def get_conversations_by_id(
        self,
        peer_ids: typing.List[int],
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetConversationsByIdResponseModel:
        """Returns conversations by their IDs
        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getConversationsById", params)
        model = self.get_model(
            {("extended",): messages.GetConversationsByIdExtendedResponse},
            default=messages.GetConversationsByIdResponse,
            params=params,
        )
        return model(**response).response

    async def get_history(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        rev: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetHistoryResponseModel:
        """Returns message history for the specified user or group chat.
        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param user_id: ID of the user whose message history you want to return.
        :param peer_id:
        :param start_message_id: Starting message ID from which to return history.
        :param rev: Sort order: '1' — return messages in chronological order. '0' — return messages in reverse chronological order.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getHistory", params)
        model = self.get_model(
            {("extended",): messages.GetHistoryExtendedResponse},
            default=messages.GetHistoryResponse,
            params=params,
        )
        return model(**response).response

    async def get_history_attachments(
        self,
        peer_id: int,
        media_type: typing.Optional[str] = None,
        start_from: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        photo_sizes: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        preserve_order: typing.Optional[bool] = None,
        max_forwards_level: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetHistoryAttachmentsResponseModel:
        """Returns media files from the dialog or group chat.
        :param peer_id: Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param media_type: Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param start_from: Message ID to start return results from.
        :param count: Number of objects to return.
        :param photo_sizes: '1' — to return photo sizes in a
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param group_id: Group ID (for group messages with group access token)
        :param preserve_order:
        :param max_forwards_level:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getHistoryAttachments", params)
        model = messages.GetHistoryAttachmentsResponse
        return model(**response).response

    async def get_important_messages(
        self,
        count: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[str]] = None,
        extended: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetImportantMessagesResponseModel:
        """Returns a list of user's important messages.
        :param count: Amount of needed important messages.
        :param offset:
        :param start_message_id:
        :param preview_length: Maximum length of messages body.
        :param fields: Actors fields to return.
        :param extended: Return extended properties
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getImportantMessages", params)
        model = self.get_model(
            {("extended",): messages.GetImportantMessagesExtendedResponse},
            default=messages.GetImportantMessagesResponse,
            params=params,
        )
        return model(**response).response

    async def get_intent_users(
        self,
        intent: str,
        subscribe_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        name_case: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> messages.GetIntentUsersResponseModel:
        """messages.getIntentUsers method
        :param intent:
        :param subscribe_id:
        :param offset:
        :param count:
        :param extended:
        :param name_case:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getIntentUsers", params)
        model = messages.GetIntentUsersResponse
        return model(**response).response

    async def get_invite_link(
        self,
        peer_id: int,
        reset: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.GetInviteLinkResponseModel:
        """messages.getInviteLink method
        :param peer_id: Destination ID.
        :param reset: 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: Group ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getInviteLink", params)
        model = messages.GetInviteLinkResponse
        return model(**response).response

    async def get_last_activity(
        self, user_id: int, **kwargs
    ) -> messages.MessagesLastActivity:
        """Returns a user's current status and date of last activity.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLastActivity", params)
        model = messages.GetLastActivityResponse
        return model(**response).response

    async def get_long_poll_history(
        self,
        ts: typing.Optional[int] = None,
        pts: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        onlines: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        events_limit: typing.Optional[int] = None,
        msgs_limit: typing.Optional[int] = None,
        max_msg_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
        last_n: typing.Optional[int] = None,
        credentials: typing.Optional[bool] = None,
        **kwargs
    ) -> messages.GetLongPollHistoryResponseModel:
        """Returns updates in user's private messages.
        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param pts: Lsat value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param onlines: '1' — to return history with online users only.
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param events_limit: Maximum number of events to return.
        :param msgs_limit: Maximum number of messages to return.
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version:
        :param last_n:
        :param credentials:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLongPollHistory", params)
        model = messages.GetLongPollHistoryResponse
        return model(**response).response

    async def get_long_poll_server(
        self,
        need_pts: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
        **kwargs
    ) -> messages.MessagesLongpollParams:
        """Returns data required for connection to a Long Poll server.
        :param need_pts: '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.getLongPollServer", params)
        model = messages.GetLongPollServerResponse
        return model(**response).response

    async def is_messages_from_group_allowed(
        self, group_id: int, user_id: int, **kwargs
    ) -> messages.IsMessagesFromGroupAllowedResponseModel:
        """Returns information whether sending messages from the community to current user is allowed.
        :param group_id: Group ID.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.isMessagesFromGroupAllowed", params)
        model = messages.IsMessagesFromGroupAllowedResponse
        return model(**response).response

    async def join_chat_by_invite_link(
        self, link: str, **kwargs
    ) -> messages.JoinChatByInviteLinkResponseModel:
        """messages.joinChatByInviteLink method
        :param link: Invitation link.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.joinChatByInviteLink", params)
        model = messages.JoinChatByInviteLinkResponse
        return model(**response).response

    async def mark_as_answered_conversation(
        self,
        peer_id: int,
        answered: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Marks and unmarks conversations as unanswered.
        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' — to mark as answered, '0' — to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsAnsweredConversation", params)
        model = base.OkResponse
        return model(**response).response

    async def mark_as_important(
        self,
        message_ids: typing.Optional[typing.List[int]] = None,
        important: typing.Optional[int] = None,
        **kwargs
    ) -> typing.List[int]:
        """Marks and unmarks messages as important (starred).
        :param message_ids: IDs of messages to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsImportant", params)
        model = messages.MarkAsImportantResponse
        return model(**response).response

    async def mark_as_important_conversation(
        self,
        peer_id: int,
        important: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Marks and unmarks conversations as important.
        :param peer_id: ID of conversation to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsImportantConversation", params)
        model = base.OkResponse
        return model(**response).response

    async def mark_as_read(
        self,
        message_ids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        mark_conversation_as_read: typing.Optional[bool] = None,
        **kwargs
    ) -> int:
        """Marks messages as read.
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param group_id: Group ID (for group messages with user access token)
        :param mark_conversation_as_read:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.markAsRead", params)
        model = base.OkResponse
        return model(**response).response

    async def pin(
        self,
        peer_id: int,
        message_id: typing.Optional[int] = None,
        conversation_message_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.MessagesPinnedMessage:
        """Pin a message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id: Message ID
        :param conversation_message_id: Conversation message ID
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.pin", params)
        model = messages.PinResponse
        return model(**response).response

    async def remove_chat_user(
        self,
        chat_id: int,
        user_id: typing.Optional[int] = None,
        member_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be removed from the chat.
        :param member_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.removeChatUser", params)
        model = base.OkResponse
        return model(**response).response

    async def restore(
        self, message_id: int, group_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """Restores a deleted message.
        :param message_id: ID of a previously-deleted message to restore.
        :param group_id: Group ID (for group messages with user access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.restore", params)
        model = base.OkResponse
        return model(**response).response

    async def search(
        self,
        q: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        date: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.SearchResponseModel:
        """Returns a list of the current user's private messages that match search criteria.
        :param q: Search query string.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param date: Date to search message before in Unixtime.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param extended:
        :param fields:
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.search", params)
        model = self.get_model(
            {("extended",): messages.SearchExtendedResponse},
            default=messages.SearchResponse,
            params=params,
        )
        return model(**response).response

    async def search_conversations(
        self,
        q: typing.Optional[str] = None,
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> messages.SearchConversationsResponseModel:
        """Returns a list of the current user's conversations that match search criteria.
        :param q: Search query string.
        :param count: Maximum number of results.
        :param extended: '1' — return extra information about users and communities
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.searchConversations", params)
        model = self.get_model(
            {("extended",): messages.SearchConversationsExtendedResponse},
            default=messages.SearchConversationsResponse,
            params=params,
        )
        return model(**response).response

    async def send(
        self,
        user_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        peer_ids: typing.Optional[typing.List[int]] = None,
        domain: typing.Optional[str] = None,
        chat_id: typing.Optional[int] = None,
        user_ids: typing.Optional[typing.List[int]] = None,
        message: typing.Optional[str] = None,
        lat: typing.Optional[int] = None,
        long: typing.Optional[int] = None,
        attachment: typing.Optional[str] = None,
        reply_to: typing.Optional[int] = None,
        forward_messages: typing.Optional[typing.List[int]] = None,
        forward: typing.Optional[str] = None,
        sticker_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        keyboard: typing.Optional[str] = None,
        template: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        content_source: typing.Optional[str] = None,
        dont_parse_links: typing.Optional[bool] = None,
        disable_mentions: typing.Optional[bool] = None,
        intent: typing.Optional[str] = None,
        subscribe_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
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
            {
                ("user_ids",): messages.SendUserIdsResponse,
                ("peer_ids",): messages.SendPeerIdsResponse,
            },
            default=messages.SendResponse,
            params=params,
        )
        return model(**response).response

    async def send_message_event_answer(
        self,
        event_id: str,
        user_id: int,
        peer_id: int,
        event_data: typing.Optional[str] = None,
        **kwargs
    ) -> int:
        """messages.sendMessageEventAnswer method
        :param event_id:
        :param user_id:
        :param peer_id:
        :param event_data:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.sendMessageEventAnswer", params)
        model = base.OkResponse
        return model(**response).response

    async def set_activity(
        self,
        user_id: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs
    ) -> int:
        """Changes the status of a user as typing in a conversation.
        :param user_id: User ID.
        :param type: 'typing' — user has started to type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.setActivity", params)
        model = base.OkResponse
        return model(**response).response

    async def set_chat_photo(
        self, file: str, **kwargs
    ) -> messages.SetChatPhotoResponseModel:
        """Sets a previously-uploaded picture as the cover picture of a chat.
        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.setChatPhoto", params)
        model = messages.SetChatPhotoResponse
        return model(**response).response

    async def unpin(
        self, peer_id: int, group_id: typing.Optional[int] = None, **kwargs
    ) -> int:
        """messages.unpin method
        :param peer_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("messages.unpin", params)
        model = base.OkResponse
        return model(**response).response
