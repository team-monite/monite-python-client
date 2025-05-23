# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaymentReceivedEventData(UniversalBaseModel):
    """
    Contains information about a payment received for an invoice.
    """

    amount_due: int = pydantic.Field()
    """
    The remainimg amount due of the invoice, in [minor units](https://docs.monite.com/references/currencies#minor-units) of the currency. For example, $12.5 is represented as 1250.
    """

    amount_paid: int = pydantic.Field()
    """
    The payment amount, in minor units of the currency.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    A user-defined comment about this payment, or `null` if no comment was provided. Comments are available only for payments recorded via `POST /receivables/{receivable_id}/mark_as_paid` and `POST /receivables/{receivable_id}/mark_as_partially_paid`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
