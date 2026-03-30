import typing

from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.objects import BaseUploadServer, BaseUserGroupFields
from vkbottle_types.responses.base import (
    BaseBoolResponse,
    BaseGetUploadServerResponse,
    BaseOkResponse,
    BaseOkResponseModel,
)
from vkbottle_types.responses.bugtracker import *  # noqa: F401,F403  # type: ignore


class BugtrackerCategory(BaseCategory):
    async def add_company_groups_members(
        self,
        company_group_ids: list[int],
        company_id: int,
        user_ids: list[int],
        **kwargs: typing.Any,
    ) -> BugtrackerAddCompanyGroupsMembersResponseModel:
        """Method `bugtracker.addCompanyGroupsMembers()`

        :param company_group_ids:
        :param company_id:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.addCompanyGroupsMembers", params)
        model = BugtrackerAddCompanyGroupsMembersResponse
        return model(**response).response

    async def add_company_members(
        self,
        company_id: int,
        user_ids: list[int],
        **kwargs: typing.Any,
    ) -> BugtrackerAddCompanyMembersResponseModel:
        """Method `bugtracker.addCompanyMembers()`

        :param company_id:
        :param user_ids:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.addCompanyMembers", params)
        model = BugtrackerAddCompanyMembersResponse
        return model(**response).response

    async def change_bugreport_status(
        self,
        bugreport_id: int,
        comment: str | None = None,
        from_statuses: list[int] | None = None,
        not_in_statuses: list[int] | None = None,
        status: int | None = None,
        **kwargs: typing.Any,
    ) -> bool:
        """Method `bugtracker.changeBugreportStatus()`

        :param bugreport_id:
        :param comment:
        :param from_statuses:
        :param not_in_statuses:
        :param status:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.changeBugreportStatus", params)
        model = BaseBoolResponse
        return model(**response).response

    async def create_comment(
        self,
        bugreport_id: int,
        force: bool | None = None,
        hidden: bool | None = None,
        hidden_attachments: bool | None = None,
        text: str | None = None,
        **kwargs: typing.Any,
    ) -> BugtrackerCreateCommentResponseModel:
        """Method `bugtracker.createComment()`

        :param bugreport_id:
        :param force:
        :param hidden:
        :param hidden_attachments:
        :param text:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.createComment", params)
        model = BugtrackerCreateCommentResponse
        return model(**response).response

    async def get_bugreport_by_id(
        self,
        bugreport_id: int,
        extended: bool | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        **kwargs: typing.Any,
    ) -> BugtrackerGetBugreportByIdResponseModel:
        """Method `bugtracker.getBugreportById()`

        :param bugreport_id:
        :param extended:
        :param fields:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.getBugreportById", params)
        model = BugtrackerGetBugreportByIdResponse
        return model(**response).response

    async def get_company_group_members(
        self,
        company_group_id: int,
        company_id: int,
        count: int | None = None,
        extended: bool | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        filter_name: str | None = None,
        offset: int | None = None,
        **kwargs: typing.Any,
    ) -> BugtrackerGetCompanyGroupMembersResponseModel:
        """Method `bugtracker.getCompanyGroupMembers()`

        :param company_group_id:
        :param company_id:
        :param count:
        :param extended:
        :param fields:
        :param filter_name:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.getCompanyGroupMembers", params)
        model = BugtrackerGetCompanyGroupMembersResponse
        return model(**response).response

    async def get_company_members(
        self,
        company_id: int,
        count: int | None = None,
        extended: bool | None = None,
        extra: bool | None = None,
        fields: list[BaseUserGroupFields] | None = None,
        filter_member_ids: list[int] | None = None,
        filter_name: str | None = None,
        filter_not_group: int | None = None,
        filter_role: int | None = None,
        offset: int | None = None,
        **kwargs: typing.Any,
    ) -> BugtrackerGetCompanyMembersResponseModel:
        """Method `bugtracker.getCompanyMembers()`

        :param company_id:
        :param count:
        :param extended:
        :param extra:
        :param fields:
        :param filter_member_ids:
        :param filter_name:
        :param filter_not_group:
        :param filter_role:
        :param offset:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.getCompanyMembers", params)
        model = BugtrackerGetCompanyMembersResponse
        return model(**response).response

    async def get_download_version_url(
        self,
        product_id: int,
        version_id: int,
        ttl: int | None = None,
        **kwargs: typing.Any,
    ) -> BugtrackerGetDownloadVersionUrlResponseModel:
        """Method `bugtracker.getDownloadVersionUrl()`

        :param product_id:
        :param version_id:
        :param ttl:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.getDownloadVersionUrl", params)
        model = BugtrackerGetDownloadVersionUrlResponse
        return model(**response).response

    async def get_product_build_upload_server(
        self,
        product_id: int,
        **kwargs: typing.Any,
    ) -> "BaseUploadServer":
        """Method `bugtracker.getProductBuildUploadServer()`

        :param product_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.getProductBuildUploadServer", params)
        model = BaseGetUploadServerResponse
        return model(**response).response

    async def remove_company_group_member(
        self,
        company_group_id: int,
        company_id: int,
        user_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `bugtracker.removeCompanyGroupMember()`

        :param company_group_id:
        :param company_id:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.removeCompanyGroupMember", params)
        model = BaseOkResponse
        return model(**response).response

    async def remove_company_member(
        self,
        company_id: int,
        user_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `bugtracker.removeCompanyMember()`

        :param company_id:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.removeCompanyMember", params)
        model = BaseOkResponse
        return model(**response).response

    async def save_product_version(
        self,
        title: str,
        product_id: int | None = None,
        release_notes: str | None = None,
        set_rft: bool | None = None,
        version_id: int | None = None,
        visible: bool | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `bugtracker.saveProductVersion()`

        :param title:
        :param product_id:
        :param release_notes:
        :param set_rft:
        :param version_id:
        :param visible:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.saveProductVersion", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_company_member_role(
        self,
        company_id: int,
        role: int,
        user_id: int,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `bugtracker.setCompanyMemberRole()`

        :param company_id:
        :param role:
        :param user_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.setCompanyMemberRole", params)
        model = BaseOkResponse
        return model(**response).response

    async def set_product_is_over(
        self,
        product_id: int,
        is_over: bool | None = None,
        **kwargs: typing.Any,
    ) -> BaseOkResponseModel:
        """Method `bugtracker.setProductIsOver()`

        :param product_id:
        :param is_over:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("bugtracker.setProductIsOver", params)
        model = BaseOkResponse
        return model(**response).response


__all__ = ("BugtrackerCategory",)
