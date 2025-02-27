# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .verification_airwallex_plaid_response import VerificationAirwallexPlaidResponse
from .bank_account_verification_type import BankAccountVerificationType
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class VerificationResponse(UniversalBaseModel):
    airwallex_plaid: VerificationAirwallexPlaidResponse
    type: BankAccountVerificationType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
