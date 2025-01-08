# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .language_code_enum import LanguageCodeEnum
from .counterpart_organization_update_payload import CounterpartOrganizationUpdatePayload
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CounterpartOrganizationRootUpdatePayload(UniversalBaseModel):
    """
    Represents counterparts that are organizations (juridical persons).
    """

    default_billing_address_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the counterpart's billing address. If the counterpart is US-based and needs to accept ACH payments, this address must have all fields filled in. If `default_billing_address_id` is not defined, the default address is instead used as the billing address for ACH payments.
    """

    default_shipping_address_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the shipping address.
    """

    language: typing.Optional[LanguageCodeEnum] = pydantic.Field(default=None)
    """
    The language used to generate pdf documents for this counterpart.
    """

    organization: CounterpartOrganizationUpdatePayload
    reminders_enabled: typing.Optional[bool] = None
    tax_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The counterpart's taxpayer identification number or tax ID. This field is required for counterparts that are non-VAT registered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
