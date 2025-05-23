# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CounterpartOrganizationUpdatePayload(UniversalBaseModel):
    """
    Represents counterparts that are organizations (juridical persons).
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the organization.
    """

    is_customer: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the counterpart is a customer.
    """

    is_vendor: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the counterpart is a vendor.
    """

    legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The legal name of the organization.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number of the organization.
    """

    tag_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IDs of user-defined tags (labels) assigned to this counterpart.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
