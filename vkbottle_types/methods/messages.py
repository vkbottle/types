import typing
from typing import Optional, List

from vkbottle_types.responses import messages, base
from .base_category import BaseCategory

if typing.TYPE_CHECKING:
    from vkbottle_types.objects import users as objects_users, base as objects_base


class MessagesCategory(BaseCategory):
    async def add_chat_user(
        self,
        chat_id: int,
        user_id: Optional[int] = None,
        visible_messages_count: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Adds a new user to a chat.
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.addChatUser", params)
        ).response

    async def allow_messages_from_group(
        self, group_id: int, key: Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """Allows sending messages from community to the current user.
        :param group_id: Group ID.
        :param key:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.allowMessagesFromGroup", params)
        ).response

    async def create_chat(
        self,
        user_ids: Optional[List[int]] = None,
        title: Optional[str] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> messages.CreateChatResponseModel:
        """Creates a chat with several participants.
        :param user_ids: IDs of the users to be added to the chat.
        :param title: Chat title.
        :param group_id:
        """

        params = self.get_set_params(locals())
        return messages.CreateChatResponse(
            **await self.api.request("messages.createChat", params)
        ).response

    async def delete(
        self,
        message_ids: Optional[List[int]] = None,
        spam: Optional[bool] = None,
        group_id: Optional[int] = None,
        delete_for_all: Optional[bool] = None,
        **kwargs
    ) -> messages.DeleteResponseModel:
        """Deletes one or more messages.
        :param message_ids: Message IDs.
        :param spam: '1' — to mark message as spam.
        :param group_id: Group ID (for group messages with user access token)
        :param delete_for_all: '1' — delete message for for all.
        """

        params = self.get_set_params(locals())
        return messages.DeleteResponse(
            **await self.api.request("messages.delete", params)
        ).response

    async def delete_chat_photo(
        self, chat_id: int, group_id: Optional[int] = None, **kwargs
    ) -> messages.DeleteChatPhotoResponseModel:
        """Deletes a chat's cover picture.
        :param chat_id: Chat ID.
        :param group_id:
        """

        params = self.get_set_params(locals())
        return messages.DeleteChatPhotoResponse(
            **await self.api.request("messages.deleteChatPhoto", params)
        ).response

    async def delete_conversation(
        self,
        user_id: Optional[int] = None,
        peer_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> messages.DeleteConversationResponseModel:
        """Deletes all private messages in a conversation.
        :param user_id: User ID. To clear a chat history use 'chat_id'
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with user access token)
        """

        params = self.get_set_params(locals())
        return messages.DeleteConversationResponse(
            **await self.api.request("messages.deleteConversation", params)
        ).response

    async def deny_messages_from_group(
        self, group_id: int, **kwargs
    ) -> base.OkResponseModel:
        """Denies sending message from community to the current user.
        :param group_id: Group ID.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.denyMessagesFromGroup", params)
        ).response

    async def edit(
        self,
        peer_id: int,
        message: Optional[str] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        attachment: Optional[str] = None,
        keep_forward_messages: Optional[bool] = None,
        keep_snippets: Optional[bool] = None,
        group_id: Optional[int] = None,
        dont_parse_links: Optional[bool] = None,
        message_id: Optional[int] = None,
        conversation_message_id: Optional[int] = None,
        template: Optional[str] = None,
        keyboard: Optional[str] = None,
        **kwargs
    ) -> messages.EditResponseModel:
        """Edits the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: (Required if 'attachments' is not set., **kwargs) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set., **kwargs) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
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
        return messages.EditResponse(
            **await self.api.request("messages.edit", params)
        ).response

    async def edit_chat(
        self, chat_id: int, title: Optional[str] = None, **kwargs
    ) -> base.OkResponseModel:
        """Edits the title of a chat.
        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.editChat", params)
        ).response

    async def get_by_conversation_message_id(
        self,
        peer_id: int,
        conversation_message_ids: List[int],
        extended: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        group_id: Optional[int] = None,
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
        return messages.GetByConversationMessageIdResponse(
            **await self.api.request("messages.getByConversationMessageId", params)
        ).response

    async def get_by_id(
        self,
        message_ids: List[int],
        preview_length: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> messages.GetByIdExtendedResponseModel:
        """Returns messages by their IDs.
        :param message_ids: Message IDs.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        return messages.GetByIdExtendedResponse(
            **await self.api.request("messages.getById", params)
        ).response

    async def get_chat_preview(
        self,
        peer_id: Optional[int] = None,
        link: Optional[str] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        **kwargs
    ) -> messages.GetChatPreviewResponseModel:
        """messages.getChatPreview method
        :param peer_id:
        :param link: Invitation link.
        :param fields: Profile fields to return.
        """

        params = self.get_set_params(locals())
        return messages.GetChatPreviewResponse(
            **await self.api.request("messages.getChatPreview", params)
        ).response

    async def get_conversation_members(
        self,
        peer_id: int,
        fields: Optional[List["objects_users.Fields"]] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> messages.GetConversationMembersResponseModel:
        """Returns a list of IDs of users participating in a chat.
        :param peer_id: Peer ID.
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        return messages.GetConversationMembersResponse(
            **await self.api.request("messages.getConversationMembers", params)
        ).response

    async def get_conversations(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        filter: Optional[str] = None,
        extended: Optional[bool] = None,
        start_message_id: Optional[int] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
        group_id: Optional[int] = None,
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
        return messages.GetConversationsResponse(
            **await self.api.request("messages.getConversations", params)
        ).response

    async def get_conversations_by_id(
        self,
        peer_ids: List[int],
        extended: Optional[bool] = None,
        fields: Optional[List["objects_base.UserGroupFields"]] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> messages.GetConversationsByIdExtendedResponseModel:
        """Returns conversations by their IDs
        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        return messages.GetConversationsByIdExtendedResponse(
            **await self.api.request("messages.getConversationsById", params)
        ).response

    async def get_history(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        user_id: Optional[int] = None,
        peer_id: Optional[int] = None,
        start_message_id: Optional[int] = None,
        rev: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        group_id: Optional[int] = None,
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
        return messages.GetHistoryResponse(
            **await self.api.request("messages.getHistory", params)
        ).response

    async def get_history_attachments(
        self,
        peer_id: int,
        media_type: Optional[str] = None,
        start_from: Optional[str] = None,
        count: Optional[int] = None,
        photo_sizes: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        group_id: Optional[int] = None,
        preserve_order: Optional[bool] = None,
        max_forwards_level: Optional[int] = None,
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
        return messages.GetHistoryAttachmentsResponse(
            **await self.api.request("messages.getHistoryAttachments", params)
        ).response

    async def get_invite_link(
        self,
        peer_id: int,
        reset: Optional[bool] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> messages.GetInviteLinkResponseModel:
        """messages.getInviteLink method
        :param peer_id: Destination ID.
        :param reset: 1 — to generate new link (revoke previous), 0 — to return previous link.
        :param group_id: Group ID
        """

        params = self.get_set_params(locals())
        return messages.GetInviteLinkResponse(
            **await self.api.request("messages.getInviteLink", params)
        ).response

    async def get_last_activity(
        self, user_id: int, **kwargs
    ) -> messages.GetLastActivityResponseModel:
        """Returns a user's current status and date of last activity.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        return messages.GetLastActivityResponse(
            **await self.api.request("messages.getLastActivity", params)
        ).response

    async def get_long_poll_history(
        self,
        ts: Optional[int] = None,
        pts: Optional[int] = None,
        preview_length: Optional[int] = None,
        onlines: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        events_limit: Optional[int] = None,
        msgs_limit: Optional[int] = None,
        max_msg_id: Optional[int] = None,
        group_id: Optional[int] = None,
        lp_version: Optional[int] = None,
        last_n: Optional[int] = None,
        credentials: Optional[bool] = None,
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
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4, **kwargs) are taken into account.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version:
        :param last_n:
        :param credentials:
        """

        params = self.get_set_params(locals())
        return messages.GetLongPollHistoryResponse(
            **await self.api.request("messages.getLongPollHistory", params)
        ).response

    async def get_long_poll_server(
        self,
        need_pts: Optional[bool] = None,
        group_id: Optional[int] = None,
        lp_version: Optional[int] = None,
        **kwargs
    ) -> messages.GetLongPollServerResponseModel:
        """Returns data required for connection to a Long Poll server.
        :param need_pts: '1' — to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        """

        params = self.get_set_params(locals())
        return messages.GetLongPollServerResponse(
            **await self.api.request("messages.getLongPollServer", params)
        ).response

    async def is_messages_from_group_allowed(
        self, group_id: int, user_id: int, **kwargs
    ) -> messages.IsMessagesFromGroupAllowedResponseModel:
        """Returns information whether sending messages from the community to current user is allowed.
        :param group_id: Group ID.
        :param user_id: User ID.
        """

        params = self.get_set_params(locals())
        return messages.IsMessagesFromGroupAllowedResponse(
            **await self.api.request("messages.isMessagesFromGroupAllowed", params)
        ).response

    async def join_chat_by_invite_link(
        self, link: str, **kwargs
    ) -> messages.JoinChatByInviteLinkResponseModel:
        """messages.joinChatByInviteLink method
        :param link: Invitation link.
        """

        params = self.get_set_params(locals())
        return messages.JoinChatByInviteLinkResponse(
            **await self.api.request("messages.joinChatByInviteLink", params)
        ).response

    async def mark_as_answered_conversation(
        self,
        peer_id: int,
        answered: Optional[bool] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Marks and unmarks conversations as unanswered.
        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' — to mark as answered, '0' — to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.markAsAnsweredConversation", params)
        ).response

    async def mark_as_important(
        self,
        message_ids: Optional[List[int]] = None,
        important: Optional[int] = None,
        **kwargs
    ) -> messages.MarkAsImportantResponseModel:
        """Marks and unmarks messages as important (starred).
        :param message_ids: IDs of messages to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        """

        params = self.get_set_params(locals())
        return messages.MarkAsImportantResponse(
            **await self.api.request("messages.markAsImportant", params)
        ).response

    async def mark_as_important_conversation(
        self,
        peer_id: int,
        important: Optional[bool] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Marks and unmarks conversations as important.
        :param peer_id: ID of conversation to mark as important.
        :param important: '1' — to add a star (mark as important), '0' — to remove the star
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.markAsImportantConversation", params)
        ).response

    async def mark_as_read(
        self,
        message_ids: Optional[List[int]] = None,
        peer_id: Optional[int] = None,
        start_message_id: Optional[int] = None,
        group_id: Optional[int] = None,
        mark_conversation_as_read: Optional[bool] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Marks messages as read.
        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param group_id: Group ID (for group messages with user access token)
        :param mark_conversation_as_read:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.markAsRead", params)
        ).response

    async def pin(
        self, peer_id: int, message_id: Optional[int] = None, **kwargs
    ) -> messages.PinResponseModel:
        """Pin a message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id:
        """

        params = self.get_set_params(locals())
        return messages.PinResponse(
            **await self.api.request("messages.pin", params)
        ).response

    async def remove_chat_user(
        self,
        chat_id: int,
        user_id: Optional[int] = None,
        member_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.
        :param chat_id: Chat ID.
        :param user_id: ID of the user to be removed from the chat.
        :param member_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.removeChatUser", params)
        ).response

    async def restore(
        self, message_id: int, group_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """Restores a deleted message.
        :param message_id: ID of a previously-deleted message to restore.
        :param group_id: Group ID (for group messages with user access token)
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.restore", params)
        ).response

    async def search(
        self,
        q: Optional[str] = None,
        peer_id: Optional[int] = None,
        date: Optional[int] = None,
        preview_length: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[List[str]] = None,
        group_id: Optional[int] = None,
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
        return messages.SearchResponse(
            **await self.api.request("messages.search", params)
        ).response

    async def search_conversations(
        self,
        q: Optional[str] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[List["objects_users.Fields"]] = None,
        group_id: Optional[int] = None,
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
        return messages.SearchConversationsResponse(
            **await self.api.request("messages.searchConversations", params)
        ).response

    async def send(
        self,
        user_id: Optional[int] = None,
        random_id: Optional[int] = None,
        peer_id: Optional[int] = None,
        domain: Optional[str] = None,
        chat_id: Optional[int] = None,
        user_ids: Optional[List[int]] = None,
        message: Optional[str] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        attachment: Optional[str] = None,
        reply_to: Optional[int] = None,
        forward_messages: Optional[List[int]] = None,
        sticker_id: Optional[int] = None,
        group_id: Optional[int] = None,
        keyboard: Optional[str] = None,
        payload: Optional[str] = None,
        dont_parse_links: Optional[bool] = None,
        disable_mentions: Optional[bool] = None,
        intent: Optional[str] = None,
        subscribe_id: Optional[int] = None,
        **kwargs
    ) -> messages.SendResponseModel:
        """Sends a message.
        :param user_id: User ID (by default — current user).
        :param random_id: Unique identifier to avoid resending the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param domain: User's short address (for example, 'illarionov').
        :param chat_id: ID of conversation the message will relate to.
        :param user_ids: IDs of message recipients (if new conversation shall be started).
        :param message: (Required if 'attachments' is not set., **kwargs) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set., **kwargs) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' — Type of media attachment: 'photo' — photo, 'video' — video, 'audio' — audio, 'doc' — document, 'wall' — wall post, '<owner_id>' — ID of the media attachment owner. '<media_id>' — media attachment ID. Example: "photo100172_166443618"
        :param reply_to:
        :param forward_messages: ID of forwarded messages, separated with a comma. Listed messages of the sender will be shown in the message body at the recipient's. Example: "123,431,544"
        :param sticker_id: Sticker id.
        :param group_id: Group ID (for group messages with group access token)
        :param keyboard:
        :param payload:
        :param dont_parse_links:
        :param disable_mentions:
        :param intent:
        :param subscribe_id:
        """

        params = self.get_set_params(locals())
        return messages.SendResponse(
            **await self.api.request("messages.send", params)
        ).response

    async def send_message_event_answer(
        self,
        event_id: str,
        user_id: int,
        peer_id: int,
        event_data: Optional[str] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """messages.sendMessageEventAnswer method
        :param event_id:
        :param user_id:
        :param peer_id:
        :param event_data:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.sendMessageEventAnswer", params)
        ).response

    async def set_activity(
        self,
        user_id: Optional[int] = None,
        type: Optional[str] = None,
        peer_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> base.OkResponseModel:
        """Changes the status of a user as typing in a conversation.
        :param user_id: User ID.
        :param type: 'typing' — user has started to type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with group access token)
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.setActivity", params)
        ).response

    async def set_chat_photo(
        self, file: str, **kwargs
    ) -> messages.SetChatPhotoResponseModel:
        """Sets a previously-uploaded picture as the cover picture of a chat.
        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """

        params = self.get_set_params(locals())
        return messages.SetChatPhotoResponse(
            **await self.api.request("messages.setChatPhoto", params)
        ).response

    async def unpin(
        self, peer_id: int, group_id: Optional[int] = None, **kwargs
    ) -> base.OkResponseModel:
        """messages.unpin method
        :param peer_id:
        :param group_id:
        """

        params = self.get_set_params(locals())
        return base.OkResponse(
            **await self.api.request("messages.unpin", params)
        ).response
