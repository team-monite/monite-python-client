# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_disabled_reason import AccountDisabledReason
from .payment_requirements import PaymentRequirements
from .requirements_error import RequirementsError
from .verification_error import VerificationError
from .verification_status_enum import VerificationStatusEnum


class OnboardingRequirementsResponse(UniversalBaseModel):
    disabled_reason: typing.Optional[AccountDisabledReason] = None
    requirements: PaymentRequirements
    requirements_errors: typing.List[RequirementsError]
    verification_errors: typing.List[VerificationError]
    verification_status: VerificationStatusEnum

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
