import typing

from typing_extensions import Literal
from vkbottle_types.methods.base_category import BaseCategory
from vkbottle_types.responses.lead_forms import *
from vkbottle_types.responses.base import OkResponse


class LeadFormsCategory(BaseCategory):
    async def create(
        self,
        group_id: int,
        name: str,
        title: str,
        description: str,
        questions: str,
        policy_link_url: str,
        photo: typing.Optional[str] = None,
        confirmation: typing.Optional[str] = None,
        site_link_url: typing.Optional[str] = None,
        active: typing.Optional[bool] = 0,
        once_per_user: typing.Optional[bool] = 0,
        pixel_code: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> LeadFormsCreateResponseModel:
        """leadForms.create method


        :param group_id:
        :param name:
        :param title:
        :param description:
        :param questions:
        :param policy_link_url:
        :param photo:
        :param confirmation:
        :param site_link_url:
        :param active:
        :param once_per_user:
        :param pixel_code:
        :param notify_admins:
        :param notify_emails:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsCreateResponse

        return model(**response).response

    async def delete(
        self,
        group_id: int,
        form_id: int,
        **kwargs,
    ) -> LeadFormsDeleteResponseModel:
        """leadForms.delete method


        :param group_id:
        :param form_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsDeleteResponse

        return model(**response).response

    async def get(
        self,
        group_id: int,
        form_id: int,
        **kwargs,
    ) -> LeadFormsGetResponseModel:
        """leadForms.get method


        :param group_id:
        :param form_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsGetResponse

        return model(**response).response

    async def get_leads(
        self,
        group_id: int,
        form_id: int,
        limit: typing.Optional[int] = 10,
        next_page_token: typing.Optional[str] = None,
        **kwargs,
    ) -> LeadFormsGetLeadsResponseModel:
        """leadForms.getLeads method


        :param group_id:
        :param form_id:
        :param limit:
        :param next_page_token:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsGetLeadsResponse

        return model(**response).response

    async def get_upload_u_r_l(
        self,
        **kwargs,
    ) -> LeadFormsUploadUrlResponseModel:
        """leadForms.getUploadURL method"""
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsUploadUrlResponse

        return model(**response).response

    async def list(
        self,
        group_id: int,
        **kwargs,
    ) -> LeadFormsListResponseModel:
        """leadForms.list method


        :param group_id:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsListResponse

        return model(**response).response

    async def update(
        self,
        group_id: int,
        form_id: int,
        name: str,
        title: str,
        description: str,
        questions: str,
        policy_link_url: str,
        photo: typing.Optional[str] = None,
        confirmation: typing.Optional[str] = None,
        site_link_url: typing.Optional[str] = None,
        active: typing.Optional[bool] = 0,
        once_per_user: typing.Optional[bool] = 0,
        pixel_code: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        **kwargs,
    ) -> LeadFormsCreateResponseModel:
        """leadForms.update method


        :param group_id:
        :param form_id:
        :param name:
        :param title:
        :param description:
        :param questions:
        :param policy_link_url:
        :param photo:
        :param confirmation:
        :param site_link_url:
        :param active:
        :param once_per_user:
        :param pixel_code:
        :param notify_admins:
        :param notify_emails:
        """
        params = self.get_set_params(locals())
        response = await self.api.request("account.ban", params)

        model = LeadFormsCreateResponse

        return model(**response).response


__all__ = ("LeadFormsCategory",)
