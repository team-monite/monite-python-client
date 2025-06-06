# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_enum import CurrencyEnum
from .discount import Discount
from .line_item import LineItem
from .receivable_entity_base import ReceivableEntityBase
from .vat_mode_enum import VatModeEnum


class ReceivableFacadeCreateInvoicePayload(UniversalBaseModel):
    commercial_condition_description: typing.Optional[str] = None
    counterpart_billing_address_id: str = pydantic.Field()
    """
    Address of invoicing, need to state as a separate fields for some countries if it differs from address of a company.
    """

    counterpart_business_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Different types of companies for different countries, ex. GmbH, SAS, SNC, etc.
    """

    counterpart_einvoicing_credentials_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    E-invoicing credentials ID of the counterpart
    """

    counterpart_id: str
    counterpart_shipping_address_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address where goods were shipped / where services were provided.
    """

    counterpart_vat_id_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Counterpart VAT ID id
    """

    currency: CurrencyEnum
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

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The document number of the receivable, which will appear in the PDF document. Can be set manually only in the [non-compliant mode](https://docs.monite.com/accounts-receivable/regulatory-compliance/invoice-compliance). Otherwise (or if omitted), it will be generated automatically based on the entity's [document number customization](https://docs.monite.com/advanced/document-number-customization) settings when the document is issued.
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

    footer: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional text displayed below the line items table in the PDF.
    """

    fulfillment_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date when the goods are shipped or the service is provided. Can be a current, past, or future date.
    
    Some countries require the fulfillment date in invoices for regulatory compliance. In this case, if the fulfillment date was not provided by the user, it is automatically set to the invoice issue date once the invoice gets issued.
    
    In countries where the fulfillment date is optional, Monite does not auto-assign it if it was omitted by the user.
    """

    is_einvoice: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is this Invoice will be sent through E-invoice system
    """

    line_items: typing.List[LineItem]
    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note with additional information for a receivable
    """

    network_credentials_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    E-invoicing credentials ID of the entity
    """

    overdue_reminder_id: typing.Optional[str] = None
    partner_metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Metadata for partner needs
    """

    payment_page_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the invoice's payment page. Either Monite's payment links or your custom payment links.
    """

    payment_reminder_id: typing.Optional[str] = None
    payment_terms_id: typing.Optional[str] = None
    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A project related to current receivable
    """

    purchase_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contain purchase order number.
    """

    tag_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IDs of user-defined tags (labels) assigned to this receivable.
    """

    trade_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Trade name of the entity
    """

    type: typing.Literal["invoice"] = pydantic.Field(default="invoice")
    """
    The type of the document uploaded.
    """

    vat_exempt: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the goods, materials, or services listed in the receivable are exempt from VAT or not.
    """

    vat_exemption_rationale: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for the VAT exemption, if applicable.
    """

    vat_mode: typing.Optional[VatModeEnum] = pydantic.Field(default=None)
    """
    Defines whether the prices of products in receivable will already include VAT or not.
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
