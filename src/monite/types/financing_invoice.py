# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .financing_invoice_type import FinancingInvoiceType
import pydantic
from .wc_invoice_status import WcInvoiceStatus
from .currency_enum import CurrencyEnum
import typing
from .repayment_schedule import RepaymentSchedule
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FinancingInvoice(UniversalBaseModel):
    type: FinancingInvoiceType = pydantic.Field()
    """
    The type of the invoice i.e. receivable or payable.
    """

    status: WcInvoiceStatus = pydantic.Field()
    """
    Status of the invoice.
    """

    invoice_id: str = pydantic.Field()
    """
    Monite invoice ID.
    """

    document_id: str = pydantic.Field()
    """
    Monite document ID.
    """

    due_date: str = pydantic.Field()
    """
    Monite invoice due date.
    """

    issue_date: str = pydantic.Field()
    """
    Monite invoice issue date.
    """

    total_amount: int = pydantic.Field()
    """
    Total amount of the invoice in minor units.
    """

    currency: CurrencyEnum = pydantic.Field()
    """
    Currency code.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the invoice.
    """

    payer_type: str = pydantic.Field()
    """
    Payer type. BUSINESS or INDIVIDUAL
    """

    payer_business_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payer business name. Only applicable for BUSINESS payer type.
    """

    payer_first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payer first name. Only applicable for INDIVIDUAL payer type.
    """

    payer_last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payer last name. Only applicable for INDIVIDUAL payer type.
    """

    repayment_schedule: typing.Optional[RepaymentSchedule] = pydantic.Field(default=None)
    """
    Repayment schedule of the invoice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
