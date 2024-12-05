# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .webhook_delivery_resource import WebhookDeliveryResource
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class WebhookDeliveryPaginationResource(UniversalBaseModel):
    data: typing.List[WebhookDeliveryResource] = pydantic.Field()
    """
    A set of webhooks returned per page
    """

    next_pagination_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A token that can be sent in the `pagination_token` query parameter to get the next page of results, or `null` if there is no next page (i.e. you've reached the last page).
    """

    prev_pagination_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A token that can be sent in the `pagination_token` query parameter to get the previous page of results, or `null` if there is no previous page (i.e. you've reached the first page).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
