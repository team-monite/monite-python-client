# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_enum import CurrencyEnum
from .discount import Discount
from .line_item_update import LineItemUpdate
from .receivable_entity_base import ReceivableEntityBase


class UpdateQuote(UniversalBaseModel):
    contact_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of the counterpart contact.
    """

    counterpart_billing_address_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address of invoicing, need to state as a separate fields for some countries if it differs from address of a company.
    """

    counterpart_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of the counterpart.
    """

    counterpart_shipping_address_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address where goods were shipped / where services were provided.
    """

    counterpart_vat_id_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Counterpart VAT ID id
    """

    currency: typing.Optional[CurrencyEnum] = None
    deduction_amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of tax deducted in minor units
    """

    deduction_memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note with additional information about a tax deduction
    """

    discount: typing.Optional[Discount] = pydantic.Field(default=None)
    """
    The discount for a receivable.
    """

    entity: typing.Optional[ReceivableEntityBase] = None
    entity_bank_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity bank account ID
    """

    entity_vat_id_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Entity VAT ID id
    """

    expiry_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date (in ISO 8601 format) until which the quote is valid.
    """

    footer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional text displayed below the line items table in the PDF.
    """

    line_items: typing.Optional[typing.List[LineItemUpdate]] = None
    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note with additional information for a receivable
    """

    partner_metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Metadata for partner needs
    """

    payment_terms_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of the payment terms.
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A project related to current receivable
    """

    quote_accept_page_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link for custom quote accept page
    """

    signature_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether acceptance a quote requires a signature.
    """

    tag_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IDs of user-defined tags (labels) assigned to this receivable.
    """

    trade_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Trade name of the entity
    """

    vat_exempt: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the goods, materials, or services listed in the receivable are exempt from VAT or not.
    """

    vat_exemption_rationale: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for the VAT exemption, if applicable.
    """

    withholding_tax_rate: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of tax withheld in percent minor units
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
