# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .airwallex_mandate_type import AirwallexMandateType
from .airwallex_mandate_version import AirwallexMandateVersion


class AirwallexMandate(UniversalBaseModel):
    email: str = pydantic.Field()
    """
    PDF copy of mandate will be sent to the email by Airwallex
    """

    signatory: str = pydantic.Field()
    """
    Name of the person signed the mandate, must be a bank account owner
    """

    type: AirwallexMandateType = "us_ach_debit"
    version: AirwallexMandateVersion = "1.0"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
