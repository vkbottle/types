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
        company_group_ids: typing.List[int],
        company_id: int,
        user_ids: typing.List[int],
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
        user_ids: typing.List[int],
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
        comment: typing.Optional[str] = None,
        from_statuses: typing.Optional[typing.List[int]] = None,
        not_in_statuses: typing.Optional[typing.List[int]] = None,
        status: typing.Optional[int] = None,
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
        force: typing.Optional[bool] = None,
        hidden: typing.Optional[bool] = None,
        hidden_attachments: typing.Optional[bool] = None,
        text: typing.Optional[str] = None,
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
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
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
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filter_name: typing.Optional[str] = None,
        offset: typing.Optional[int] = None,
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
        count: typing.Optional[int] = None,
        extended: typing.Optional[bool] = None,
        extra: typing.Optional[bool] = None,
        fields: typing.Optional[typing.List[BaseUserGroupFields]] = None,
        filter_member_ids: typing.Optional[typing.List[int]] = None,
        filter_name: typing.Optional[str] = None,
        filter_not_group: typing.Optional[int] = None,
        filter_role: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
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
        ttl: typing.Optional[int] = None,
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
        product_id: typing.Optional[int] = None,
        release_notes: typing.Optional[str] = None,
        set_rft: typing.Optional[bool] = None,
        version_id: typing.Optional[int] = None,
        visible: typing.Optional[bool] = None,
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
        is_over: typing.Optional[bool] = None,
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
