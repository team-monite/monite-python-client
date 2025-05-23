# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .accounting_line_item import AccountingLineItem
from .accounting_payable_due_date import AccountingPayableDueDate
from .accounting_purchase_order_ref import AccountingPurchaseOrderRef
from .accounting_vendor_ref_object import AccountingVendorRefObject


class AccountingPayable(UniversalBaseModel):
    """
    Details of an accounts payable invoice (bill) retrieved from an accounting system.
    """

    id: str = pydantic.Field()
    """
    An internal identifier of the payable in the accounting system.
    """

    amount_due: typing.Optional[float] = pydantic.Field(default=None)
    """
    Remaining amount to be paid.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO-4217 currency code of the payable.
    """

    currency_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Rate to convert the total amount of the transaction into the entity's base currency at the time of the transaction.
    """

    due_date: typing.Optional[AccountingPayableDueDate] = pydantic.Field(default=None)
    """
    The payable's due date.
    """

    invoice_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Invoice number of the payable.
    """

    lines: typing.Optional[typing.List[AccountingLineItem]] = None
    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Any additional information or business notes about the payable.
    """

    posted_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date when the payable was added to the accounting service. This may differ from the payable creation date.
    """

    purchase_order_refs: typing.Optional[typing.List[AccountingPurchaseOrderRef]] = pydantic.Field(default=None)
    """
    A list of purchase orders linked to the payable, if any.
    """

    status: str = pydantic.Field()
    """
    The status of the payable in the accounting system. Possible values: `open`, `draft`, `partially_paid`, `paid`, `unknown`, `void`.
    """

    subtotal: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount payable, including discounts but excluding VAT/taxes.
    """

    tax_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total VAT or tax amount.
    """

    total_amount: float = pydantic.Field()
    """
    The total amount payable, including discounts and VAT/taxes.
    """

    vendor_ref: typing.Optional[AccountingVendorRefObject] = pydantic.Field(default=None)
    """
    Information about the vendor from whom the payable was received.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
