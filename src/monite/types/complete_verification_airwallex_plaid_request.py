# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .airwallex_mandate import AirwallexMandate
from .airwallex_plaid_account import AirwallexPlaidAccount
from .airwallex_plaid_institution import AirwallexPlaidInstitution


class CompleteVerificationAirwallexPlaidRequest(UniversalBaseModel):
    account: AirwallexPlaidAccount = pydantic.Field()
    """
    The bank account that was selected in the Plaid Modal
    """

    institution: AirwallexPlaidInstitution = pydantic.Field()
    """
    The financial institution that was selected in the Plaid Modal
    """

    mandate: AirwallexMandate
    public_token: str = pydantic.Field()
    """
    The Plaid Public Token
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
