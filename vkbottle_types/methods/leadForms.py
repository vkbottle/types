import typing
from .base_category import BaseCategory
from vkbottle_types.responses import leadForms


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
        active: typing.Optional[bool] = None,
        once_per_user: typing.Optional[bool] = None,
        pixel_code: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> leadForms.CreateResponseModel:
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
        response = await self.api.request("leadForms.create", params)
        model = leadForms.CreateResponse
        return model(**response).response

    async def delete(
        self, group_id: int, form_id: int, **kwargs
    ) -> leadForms.DeleteResponseModel:
        """leadForms.delete method
        :param group_id:
        :param form_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.delete", params)
        model = leadForms.DeleteResponse
        return model(**response).response

    async def get(
        self, group_id: int, form_id: int, **kwargs
    ) -> leadForms.LeadFormsForm:
        """leadForms.get method
        :param group_id:
        :param form_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.get", params)
        model = leadForms.GetResponse
        return model(**response).response

    async def get_leads(
        self,
        group_id: int,
        form_id: int,
        limit: typing.Optional[int] = None,
        next_page_token: typing.Optional[str] = None,
        **kwargs
    ) -> leadForms.GetLeadsResponseModel:
        """leadForms.getLeads method
        :param group_id:
        :param form_id:
        :param limit:
        :param next_page_token:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.getLeads", params)
        model = leadForms.GetLeadsResponse
        return model(**response).response

    async def get_upload_u_r_l(
        self, **kwargs
    ) -> str:
        """leadForms.getUploadURL method"""

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.getUploadURL", params)
        model = leadForms.UploadUrlResponse
        return model(**response).response

    async def list(
        self, group_id: int, **kwargs
    ) -> typing.List[leadForms.LeadFormsForm]:
        """leadForms.list method
        :param group_id:
        """

        params = self.get_set_params(locals())
        response = await self.api.request("leadForms.list", params)
        model = leadForms.ListResponse
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
        active: typing.Optional[bool] = None,
        once_per_user: typing.Optional[bool] = None,
        pixel_code: typing.Optional[str] = None,
        notify_admins: typing.Optional[typing.List[int]] = None,
        notify_emails: typing.Optional[typing.List[str]] = None,
        **kwargs
    ) -> leadForms.CreateResponseModel:
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
        response = await self.api.request("leadForms.update", params)
        model = leadForms.CreateResponse
        return model(**response).response
