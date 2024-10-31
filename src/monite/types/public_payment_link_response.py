# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .currency_enum import CurrencyEnum
import datetime as dt
import typing
from .invoice import Invoice
from .account_response import AccountResponse
from .payment_intent import PaymentIntent
from .recipient_account_response import RecipientAccountResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PublicPaymentLinkResponse(UniversalBaseModel):
    id: str
    amount: int
    currency: CurrencyEnum
    expires_at: dt.datetime
    invoice: typing.Optional[Invoice] = None
    payer: typing.Optional[AccountResponse] = None
    payment_intent: typing.Optional[PaymentIntent] = None
    payment_intent_id: str
    payment_methods: typing.List[str]
    payment_page_url: str
    payment_reference: typing.Optional[str] = None
    recipient: RecipientAccountResponse
    return_url: typing.Optional[str] = None
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
