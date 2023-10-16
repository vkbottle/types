import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.messages import *
from vkbottle_types.responses.base import OkResponse


class MessagesCategory(BaseCategory):
    async def add_chat_user(
        self,
        chat_id: int,
        user_id: typing.Optional[int] = None,
        visible_messages_count: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.addChatUser method


        :param chat_id: Chat ID.
        :param user_id: ID of the user to be added to the chat.
        :param visible_messages_count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def add_chat_users(
        self,
        chat_id: typing.Optional[int] = None,
        visible_messages_count: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesAddChatUsersResponseModel:
        """messages.addChatUsers method


        :param chat_id:
        :param visible_messages_count:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesAddChatUsersResponse

        return model(**response).response

    async def allow_messages_from_group(
        self,
        group_id: int,
        key: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.allowMessagesFromGroup method


        :param group_id: Group ID.
        :param key:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def create_chat(
        self,
        user_ids: typing.Optional[typing.List[int]] = None,
        title: typing.Optional[str] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesCreateChatWithPeerIdsResponseModel:
        """messages.createChat method


        :param user_ids: IDs of the users to be added to the chat.
        :param title: Chat title.
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesCreateChatWithPeerIdsResponse

        return model(**response).response

    async def delete(
        self,
        message_ids: typing.Optional[typing.List[int]] = None,
        spam: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        delete_for_all: typing.Optional[bool] = 0,
        peer_id: typing.Optional[int] = None,
        cmids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> MessagesDeleteFullResponseModel:
        """messages.delete method


        :param message_ids: Message IDs.
        :param spam: '1' - to mark message as spam.
        :param group_id: Group ID (for group messages with user access token)
        :param delete_for_all: '1' - delete message for for all.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param cmids: Conversation message IDs.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesDeleteFullResponse

        return model(**response).response

    async def delete_chat_photo(
        self,
        chat_id: int,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesDeleteChatPhotoResponseModel:
        """messages.deleteChatPhoto method


        :param chat_id: Chat ID.
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesDeleteChatPhotoResponse

        return model(**response).response

    async def delete_conversation(
        self,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesDeleteConversationResponseModel:
        """messages.deleteConversation method


        :param user_id: User ID. To clear a chat history use 'chat_id'
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with user access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesDeleteConversationResponse

        return model(**response).response

    async def delete_reaction(
        self,
        peer_id: int,
        cmid: int,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """messages.deleteReaction method


        :param peer_id:
        :param cmid:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def deny_messages_from_group(
        self,
        group_id: int,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.denyMessagesFromGroup method


        :param group_id: Group ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def edit(
        self,
        peer_id: int,
        message: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
        attachment: typing.Optional[str] = None,
        keep_forward_messages: typing.Optional[bool] = None,
        keep_snippets: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        dont_parse_links: typing.Optional[bool] = 0,
        disable_mentions: typing.Optional[bool] = 0,
        message_id: typing.Optional[int] = None,
        cmid: typing.Optional[int] = None,
        template: typing.Optional[str] = None,
        keyboard: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """messages.edit method


        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'wall' - wall post, '<owner_id>' - ID of the media attachment owner. '<media_id>' - media attachment ID. Example: "photo100172_166443618"
        :param keep_forward_messages: '1' - to keep forwarded, messages.
        :param keep_snippets: '1' - to keep attached snippets.
        :param group_id: Group ID (for group messages with user access token)
        :param dont_parse_links:
        :param disable_mentions:
        :param message_id:
        :param cmid:
        :param template:
        :param keyboard:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def edit_chat(
        self,
        chat_id: int,
        title: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.editChat method


        :param chat_id: Chat ID.
        :param title: New title of the chat.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    @typing.overload
    async def get_by_conversation_message_id(
        self,
        peer_id: int,
        conversation_message_ids: typing.List[int],
        extended: typing.Literal[True] = True,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetByConversationMessageIdExtendedResponseModel:
        ...

    async def get_by_conversation_message_id(
        self,
        peer_id: int,
        conversation_message_ids: typing.List[int],
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetByConversationMessageIdResponseModel:
        """messages.getByConversationMessageId method


        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param conversation_message_ids: Conversation message IDs.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesGetByConversationMessageIdExtendedResponse),),
            default=MessagesGetByConversationMessageIdResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def get_by_id(
        self,
        extended: typing.Literal[True] = True,
        message_ids: typing.Optional[typing.List[int]] = None,
        preview_length: typing.Optional[int] = 0,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        cmids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetByIdExtendedResponseModel:
        ...

    async def get_by_id(
        self,
        message_ids: typing.Optional[typing.List[int]] = None,
        preview_length: typing.Optional[int] = 0,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        cmids: typing.Optional[typing.List[int]] = None,
        peer_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetByIdResponseModel:
        """messages.getById method


        :param message_ids: Message IDs.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        :param cmids:
        :param peer_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesGetByIdExtendedResponse),),
            default=MessagesGetByIdResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def get_chat(
        self,
        fields: typing.List[UsersFields],
        chat_id: typing.Optional[int] = None,
        chat_ids: typing.Optional[typing.List[int]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> MessagesGetChatFieldsResponseModel:
        ...

    @typing.overload
    async def get_chat(
        self,
        chat_ids: typing.List[int],
        chat_id: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> MessagesGetChatChatIdsResponseModel:
        ...

    @typing.overload
    async def get_chat(
        self,
        chat_id: typing.Optional[int] = None,
        chat_ids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> MessagesGetChatChatIdsFieldsResponseModel:
        ...

    async def get_chat(
        self,
        chat_id: typing.Optional[int] = None,
        chat_ids: typing.Optional[typing.List[int]] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        name_case: typing.Optional[str] = None,
        **kwargs,
    ) -> MessagesGetChatResponseModel:
        """messages.getChat method


        :param chat_id: Chat ID.
        :param chat_ids: Chat IDs.
        :param fields: Profile fields to return.
        :param name_case: Case for declension of user name and surname: 'nom' - nominative (default), 'gen' - genitive , 'dat' - dative, 'acc' - accusative , 'ins' - instrumental , 'abl' - prepositional
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            (
                (("fields",), MessagesGetChatFieldsResponse),
                (("chat_ids",), MessagesGetChatChatIdsResponse),
                (("chat_ids__fields_",), MessagesGetChatChatIdsFieldsResponse),
            ),
            default=MessagesGetChatResponse,
            params=params,
        )

        return model(**response).response

    async def get_chat_preview(
        self,
        peer_id: typing.Optional[int] = None,
        link: typing.Optional[str] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        **kwargs,
    ) -> MessagesGetChatPreviewResponseModel:
        """messages.getChatPreview method


        :param peer_id:
        :param link: Invitation link.
        :param fields: Profile fields to return.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetChatPreviewResponse

        return model(**response).response

    async def get_conversation_members(
        self,
        peer_id: int,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetConversationMembersResponseModel:
        """messages.getConversationMembers method


        :param peer_id: Peer ID.
        :param offset:
        :param count:
        :param extended: Extended flag
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetConversationMembersResponse

        return model(**response).response

    async def get_conversations(
        self,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        filter: typing.Optional[str] = "all",
        extended: typing.Optional[bool] = None,
        start_message_id: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetConversationsResponseModel:
        """messages.getConversations method


        :param offset: Offset needed to return a specific subset of conversations.
        :param count: Number of conversations to return.
        :param filter: Filter to apply: 'all' - all conversations, 'unread' - conversations with unread messages, 'important' - conversations, marked as important (only for community messages), 'unanswered' - conversations, marked as unanswered (only for community messages)
        :param extended: '1' - return extra information about users and communities
        :param start_message_id: ID of the message from what to return dialogs.
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetConversationsResponse

        return model(**response).response

    @typing.overload
    async def get_conversations_by_id(
        self,
        peer_ids: typing.List[int],
        extended: typing.Literal[True] = True,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetConversationsByIdExtendedResponseModel:
        ...

    async def get_conversations_by_id(
        self,
        peer_ids: typing.List[int],
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetConversationsByIdResponseModel:
        """messages.getConversationsById method


        :param peer_ids: Destination IDs. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param extended: Return extended properties
        :param fields: Profile and communities fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesGetConversationsByIdExtendedResponse),),
            default=MessagesGetConversationsByIdResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def get_history(
        self,
        extended: typing.Literal[True] = True,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        rev: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetHistoryExtendedResponseModel:
        ...

    async def get_history(
        self,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 20,
        user_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        rev: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetHistoryResponseModel:
        """messages.getHistory method


        :param offset: Offset needed to return a specific subset of messages.
        :param count: Number of messages to return.
        :param user_id: ID of the user whose message history you want to return.
        :param peer_id:
        :param start_message_id: Starting message ID from which to return history.
        :param rev: Sort order: '1' - return messages in chronological order. '0' - return messages in reverse chronological order.
        :param extended: Information whether the response should be extended
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesGetHistoryExtendedResponse),),
            default=MessagesGetHistoryResponse,
            params=params,
        )

        return model(**response).response

    async def get_history_attachments(
        self,
        attachment_types: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        cmid: typing.Optional[int] = None,
        attachment_position: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        count: typing.Optional[int] = 30,
        extended: typing.Optional[bool] = 0,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        max_forwards_level: typing.Optional[int] = 45,
        media_type: typing.Optional[str] = "photo",
        start_from: typing.Optional[str] = None,
        preserve_order: typing.Optional[bool] = None,
        photo_sizes: typing.Optional[bool] = None,
        **kwargs,
    ) -> MessagesGetHistoryAttachmentsResponseModel:
        """messages.getHistoryAttachments method


        :param attachment_types:
        :param group_id: Group ID (for group messages with group access token)
        :param peer_id: Peer ID. ", For group chat: '2000000000 + chat ID' , , For community: '-community ID'"
        :param cmid:
        :param attachment_position:
        :param offset:
        :param count: Number of objects to return.
        :param extended:
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param max_forwards_level:
        :param media_type: Type of media files to return: *'photo',, *'video',, *'audio',, *'doc',, *'link'.,*'market'.,*'wall'.,*'share'
        :param start_from: Message ID to start return results from.
        :param preserve_order:
        :param photo_sizes: '1' - to return photo sizes in a
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetHistoryAttachmentsResponse

        return model(**response).response

    @typing.overload
    async def get_important_messages(
        self,
        extended: typing.Literal[True] = True,
        count: typing.Optional[int] = 20,
        offset: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetImportantMessagesExtendedResponseModel:
        ...

    async def get_important_messages(
        self,
        count: typing.Optional[int] = 20,
        offset: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        extended: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetImportantMessagesResponseModel:
        """messages.getImportantMessages method


        :param count: Amount of needed important messages.
        :param offset:
        :param start_message_id:
        :param preview_length: Maximum length of messages body.
        :param fields: Actors fields to return.
        :param extended: Return extended properties
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesGetImportantMessagesExtendedResponse),),
            default=MessagesGetImportantMessagesResponse,
            params=params,
        )

        return model(**response).response

    async def get_intent_users(
        self,
        intent: str,
        subscribe_id: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        extended: typing.Optional[bool] = None,
        name_case: typing.Optional[typing.List[str]] = None,
        fields: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> MessagesGetIntentUsersResponseModel:
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
        response = await self.api.request("account.ban", params)

        model = MessagesGetIntentUsersResponse

        return model(**response).response

    async def get_invite_link(
        self,
        peer_id: int,
        reset: typing.Optional[bool] = 0,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetInviteLinkResponseModel:
        """messages.getInviteLink method


        :param peer_id: Destination ID.
        :param reset: 1 - to generate new link (revoke previous), 0 - to return previous link.
        :param group_id: Group ID
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetInviteLinkResponse

        return model(**response).response

    async def get_last_activity(
        self,
        user_id: int,
        **kwargs,
    ) -> MessagesGetLastActivityResponseModel:
        """messages.getLastActivity method


        :param user_id: User ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetLastActivityResponse

        return model(**response).response

    async def get_long_poll_history(
        self,
        ts: typing.Optional[int] = None,
        pts: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = None,
        onlines: typing.Optional[bool] = None,
        fields: typing.Optional[
            typing.List[UsersFields]
        ] = "photo,photo_medium_rec,sex,online,screen_name",
        events_limit: typing.Optional[int] = 1000,
        msgs_limit: typing.Optional[int] = 200,
        max_msg_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = None,
        last_n: typing.Optional[int] = 0,
        credentials: typing.Optional[bool] = None,
        extended: typing.Optional[bool] = 0,
        **kwargs,
    ) -> MessagesGetLongPollHistoryResponseModel:
        """messages.getLongPollHistory method


        :param ts: Last value of the 'ts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param pts: Last value of 'pts' parameter returned from the Long Poll server or by using [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param preview_length: Number of characters after which to truncate a previewed message. To preview the full message, specify '0'. "NOTE: Messages are not truncated by default. Messages are truncated by words."
        :param onlines: '1' - to return history with online users only.
        :param fields: Additional profile [vk.com/dev/fields|fields] to return.
        :param events_limit: Maximum number of events to return.
        :param msgs_limit: Maximum number of messages to return.
        :param max_msg_id: Maximum ID of the message among existing ones in the local copy. Both messages received with API methods (for example, , ), and data received from a Long Poll server (events with code 4) are taken into account.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version:
        :param last_n:
        :param credentials:
        :param extended:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetLongPollHistoryResponse

        return model(**response).response

    async def get_long_poll_server(
        self,
        need_pts: typing.Optional[bool] = None,
        group_id: typing.Optional[int] = None,
        lp_version: typing.Optional[int] = 0,
        **kwargs,
    ) -> MessagesGetLongPollServerResponseModel:
        """messages.getLongPollServer method


        :param need_pts: '1' - to return the 'pts' field, needed for the [vk.com/dev/messages.getLongPollHistory|messages.getLongPollHistory] method.
        :param group_id: Group ID (for group messages with user access token)
        :param lp_version: Long poll version
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetLongPollServerResponse

        return model(**response).response

    async def get_messages_reactions(
        self,
        peer_id: int,
        cmids: typing.List[int],
        **kwargs,
    ) -> MessagesGetMessagesReactionsResponseModel:
        """messages.getMessagesReactions method


        :param peer_id:
        :param cmids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetMessagesReactionsResponse

        return model(**response).response

    async def get_reacted_peers(
        self,
        peer_id: int,
        cmid: int,
        reaction_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetReactedPeersResponseModel:
        """messages.getReactedPeers method


        :param peer_id:
        :param cmid:
        :param reaction_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetReactedPeersResponse

        return model(**response).response

    async def get_reactions_assets(
        self,
        client_version: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesGetReactionsAssetsResponseModel:
        """messages.getReactionsAssets method


        :param client_version:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesGetReactionsAssetsResponse

        return model(**response).response

    async def is_messages_from_group_allowed(
        self,
        group_id: int,
        user_id: int,
        **kwargs,
    ) -> MessagesIsMessagesFromGroupAllowedResponseModel:
        """messages.isMessagesFromGroupAllowed method


        :param group_id: Group ID.
        :param user_id: User ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesIsMessagesFromGroupAllowedResponse

        return model(**response).response

    async def join_chat_by_invite_link(
        self,
        link: str,
        **kwargs,
    ) -> MessagesJoinChatByInviteLinkResponseModel:
        """messages.joinChatByInviteLink method


        :param link: Invitation link.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesJoinChatByInviteLinkResponse

        return model(**response).response

    async def mark_as_answered_conversation(
        self,
        peer_id: int,
        answered: typing.Optional[bool] = 1,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.markAsAnsweredConversation method


        :param peer_id: ID of conversation to mark as important.
        :param answered: '1' - to mark as answered, '0' - to remove the mark
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def mark_as_important(
        self,
        message_ids: typing.Optional[typing.List[int]] = None,
        important: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesMarkAsImportantDeprecatedResponseModel:
        """messages.markAsImportant method


        :param message_ids: IDs of messages to mark as important.
        :param important: '1' - to add a star (mark as important), '0' - to remove the star
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesMarkAsImportantDeprecatedResponse

        return model(**response).response

    async def mark_as_important_conversation(
        self,
        peer_id: int,
        important: typing.Optional[bool] = 1,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.markAsImportantConversation method


        :param peer_id: ID of conversation to mark as important.
        :param important: '1' - to add a star (mark as important), '0' - to remove the star
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def mark_as_read(
        self,
        message_ids: typing.Optional[typing.List[int]] = 0,
        peer_id: typing.Optional[int] = None,
        start_message_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        mark_conversation_as_read: typing.Optional[bool] = None,
        up_to_cmid: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.markAsRead method


        :param message_ids: IDs of messages to mark as read.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param start_message_id: Message ID to start from.
        :param group_id: Group ID (for group messages with user access token)
        :param mark_conversation_as_read:
        :param up_to_cmid:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def mark_reactions_as_read(
        self,
        peer_id: int,
        cmids: typing.Optional[typing.List[int]] = None,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """messages.markReactionsAsRead method


        :param peer_id:
        :param cmids:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def pin(
        self,
        peer_id: int,
        message_id: typing.Optional[int] = None,
        cmid: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesPinResponseModel:
        """messages.pin method


        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'Chat ID', e.g. '2000000001'. For community: '- Community ID', e.g. '-12345'. "
        :param message_id: Message ID
        :param cmid: Conversation message ID
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesPinResponse

        return model(**response).response

    async def remove_chat_user(
        self,
        chat_id: int,
        user_id: typing.Optional[int] = None,
        member_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.removeChatUser method


        :param chat_id: Chat ID.
        :param user_id: ID of the user to be removed from the chat.
        :param member_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def restore(
        self,
        message_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        cmid: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.restore method


        :param message_id: ID of a previously-deleted message to restore.
        :param group_id: Group ID (for group messages with user access token)
        :param cmid:
        :param peer_id: Destination ID.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    @typing.overload
    async def search(
        self,
        extended: typing.Literal[True] = True,
        q: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        date: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = 0,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSearchExtendedResponseModel:
        ...

    async def search(
        self,
        q: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        date: typing.Optional[int] = None,
        preview_length: typing.Optional[int] = 0,
        offset: typing.Optional[int] = 0,
        count: typing.Optional[int] = 20,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[str]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSearchResponseModel:
        """messages.search method


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
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesSearchExtendedResponse),),
            default=MessagesSearchResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def search_conversations(
        self,
        extended: typing.Literal[True] = True,
        q: typing.Optional[str] = None,
        count: typing.Optional[int] = 20,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSearchConversationsExtendedResponseModel:
        ...

    async def search_conversations(
        self,
        q: typing.Optional[str] = None,
        count: typing.Optional[int] = 20,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[UsersFields]] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSearchConversationsResponseModel:
        """messages.searchConversations method


        :param q: Search query string.
        :param count: Maximum number of results.
        :param extended: '1' - return extra information about users and communities
        :param fields: Profile fields to return.
        :param group_id: Group ID (for group messages with user access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            ((("extended",), MessagesSearchConversationsExtendedResponse),),
            default=MessagesSearchConversationsResponse,
            params=params,
        )

        return model(**response).response

    @typing.overload
    async def send(
        self,
        user_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        peer_ids: typing.Optional[typing.List[int]] = None,
        domain: typing.Optional[str] = None,
        chat_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
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
        dont_parse_links: typing.Optional[bool] = 0,
        disable_mentions: typing.Optional[bool] = 0,
        intent: typing.Optional[str] = "default",
        subscribe_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSendDeprecatedResponseModel:
        ...

    @typing.overload
    async def send(
        self,
        user_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        peer_ids: typing.Optional[typing.List[int]] = None,
        domain: typing.Optional[str] = None,
        chat_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
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
        dont_parse_links: typing.Optional[bool] = 0,
        disable_mentions: typing.Optional[bool] = 0,
        intent: typing.Optional[str] = "default",
        subscribe_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSendUserIdsResponseModel:
        ...

    async def send(
        self,
        user_id: typing.Optional[int] = None,
        random_id: typing.Optional[int] = None,
        peer_id: typing.Optional[int] = None,
        peer_ids: typing.Optional[typing.List[int]] = None,
        domain: typing.Optional[str] = None,
        chat_id: typing.Optional[int] = None,
        message: typing.Optional[str] = None,
        lat: typing.Optional[float] = None,
        long: typing.Optional[float] = None,
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
        dont_parse_links: typing.Optional[bool] = 0,
        disable_mentions: typing.Optional[bool] = 0,
        intent: typing.Optional[str] = "default",
        subscribe_id: typing.Optional[int] = None,
        **kwargs,
    ) -> MessagesSendDeprecatedResponseModel:
        """messages.send method


        :param user_id: User ID (by default - current user).
        :param random_id: Unique identifier to avoid resending the message.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param peer_ids: IDs of message recipients. (See peer_id)
        :param domain: User's short address (for example, 'illarionov').
        :param chat_id: ID of conversation the message will relate to.
        :param message: (Required if 'attachments' is not set.) Text of the message.
        :param lat: Geographical latitude of a check-in, in degrees (from -90 to 90).
        :param long: Geographical longitude of a check-in, in degrees (from -180 to 180).
        :param attachment: (Required if 'message' is not set.) List of objects attached to the message, separated by commas, in the following format: "<owner_id>_<media_id>", '' - Type of media attachment: 'photo' - photo, 'video' - video, 'audio' - audio, 'doc' - document, 'wall' - wall post, '<owner_id>' - ID of the media attachment owner. '<media_id>' - media attachment ID. Example: "photo100172_166443618"
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
        response = await self.api.request("account.ban", params)

        model = self.get_model(
            (
                (("deprecated",), MessagesSendDeprecatedResponse),
                (("user_ids",), MessagesSendUserIdsResponse),
            ),
            default=MessagesSendDeprecatedResponse,
            params=params,
        )

        return model(**response).response

    async def send_message_event_answer(
        self,
        event_id: str,
        user_id: int,
        peer_id: int,
        event_data: typing.Optional[str] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.sendMessageEventAnswer method


        :param event_id:
        :param user_id:
        :param peer_id:
        :param event_data:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def send_reaction(
        self,
        peer_id: int,
        cmid: int,
        reaction_id: int,
        **kwargs,
    ) -> BaseBoolResponseModel:
        """messages.sendReaction method


        :param peer_id:
        :param cmid:
        :param reaction_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseBoolResponse

        return model(**response).response

    async def set_activity(
        self,
        user_id: typing.Optional[int] = None,
        type: typing.Optional[str] = None,
        peer_id: typing.Optional[int] = None,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.setActivity method


        :param user_id: User ID.
        :param type: 'typing' - user has started to type.
        :param peer_id: Destination ID. "For user: 'User ID', e.g. '12345'. For chat: '2000000000' + 'chat_id', e.g. '2000000001'. For community: '- community ID', e.g. '-12345'. "
        :param group_id: Group ID (for group messages with group access token)
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response

    async def set_chat_photo(
        self,
        file: str,
        **kwargs,
    ) -> MessagesSetChatPhotoResponseModel:
        """messages.setChatPhoto method


        :param file: Upload URL from the 'response' field returned by the [vk.com/dev/photos.getChatUploadServer|photos.getChatUploadServer] method upon successfully uploading an image.
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = MessagesSetChatPhotoResponse

        return model(**response).response

    async def unpin(
        self,
        peer_id: int,
        group_id: typing.Optional[int] = None,
        **kwargs,
    ) -> BaseOkResponseModel:
        """messages.unpin method


        :param peer_id:
        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = BaseOkResponse

        return model(**response).response


__all__ = ("MessagesCategory",)
