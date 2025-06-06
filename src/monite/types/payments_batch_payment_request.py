# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .single_payment_intent import SinglePaymentIntent


class PaymentsBatchPaymentRequest(UniversalBaseModel):
    payer_bank_account_id: str
    payment_intents: typing.List[SinglePaymentIntent]
    payment_method: typing.Literal["us_ach"] = "us_ach"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
