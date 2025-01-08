# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
import pydantic
import typing
from .receivables_representation_of_counterpart_address import ReceivablesRepresentationOfCounterpartAddress
from .receivable_counterpart_contact import ReceivableCounterpartContact
from .receivable_counterpart_type import ReceivableCounterpartType
from .receivable_counterpart_vat_id_response import ReceivableCounterpartVatIdResponse
from .currency_enum import CurrencyEnum
from .discount import Discount
from .invoice_response_payload_entity import InvoiceResponsePayloadEntity
from .receivable_entity_address_schema import ReceivableEntityAddressSchema
from .receivables_representation_of_entity_bank_account import ReceivablesRepresentationOfEntityBankAccount
from .receivable_entity_vat_id_response import ReceivableEntityVatIdResponse
from .receivable_file_schema import ReceivableFileSchema
from .language_code_enum import LanguageCodeEnum
from .response_item import ResponseItem
from .payment_terms import PaymentTerms
from .related_documents import RelatedDocuments
from .receivables_status_enum import ReceivablesStatusEnum
from .tag_read_schema import TagReadSchema
from .total_vat_amount_item import TotalVatAmountItem
from .vat_mode_enum import VatModeEnum
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceResponsePayload(UniversalBaseModel):
    id: str
    created_at: dt.datetime = pydantic.Field()
    """
    Time at which the receivable was created. Timestamps follow the ISO 8601 standard.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Time at which the receivable was last updated. Timestamps follow the ISO 8601 standard.
    """

    amount_due: int = pydantic.Field()
    """
    How much is left to be paid in [minor units](https://docs.monite.com/docs/currencies#minor-units). Equal 0 if the Invoice is fully paid.
    """

    amount_paid: int = pydantic.Field()
    """
    How much has been paid [minor units](https://docs.monite.com/docs/currencies#minor-units)
    """

    amount_to_pay: typing.Optional[int] = pydantic.Field(default=None)
    """
    How much is left to be paid in in [minor units](https://docs.monite.com/docs/currencies#minor-units), including payment_term discounts.
    """

    based_on: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of a previous document related to the receivable if applicable.
    """

    based_on_document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique document ID of a previous document related to the receivable if applicable.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Field with a comment for pay/partially/uncollectible info on this Invoice
    """

    commercial_condition_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The commercial terms of the receivable (e.g. The products must be delivered in X days).
    """

    counterpart_billing_address: typing.Optional[ReceivablesRepresentationOfCounterpartAddress] = pydantic.Field(
        default=None
    )
    """
    Address of invoicing, need to state as a separate fields for some countries if it differs from address of a company.
    """

    counterpart_business_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Different types of companies for different countries, ex. GmbH, SAS, SNC, etc.
    """

    counterpart_contact: typing.Optional[ReceivableCounterpartContact] = pydantic.Field(default=None)
    """
    Additional information about counterpart contacts.
    """

    counterpart_id: str = pydantic.Field()
    """
    Unique ID of the counterpart.
    """

    counterpart_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A legal name of a counterpart it is an organization or first and last name if it is an individual
    """

    counterpart_shipping_address: typing.Optional[ReceivablesRepresentationOfCounterpartAddress] = pydantic.Field(
        default=None
    )
    """
    Address where goods were shipped / where services were provided.
    """

    counterpart_tax_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The VAT/TAX ID of the counterpart.
    """

    counterpart_type: ReceivableCounterpartType = pydantic.Field()
    """
    The type of the counterpart.
    """

    counterpart_vat_id: typing.Optional[ReceivableCounterpartVatIdResponse] = None
    currency: CurrencyEnum = pydantic.Field()
    """
    The currency used in the receivable.
    """

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

    discounted_subtotal: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total price of the receivable with discounts before taxes [minor units](https://docs.monite.com/docs/currencies#minor-units).
    """

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sequential code systematically assigned to invoices.
    """

    due_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional field representing date until which invoice should be paid
    """

    entity: InvoiceResponsePayloadEntity
    entity_address: ReceivableEntityAddressSchema
    entity_bank_account: typing.Optional[ReceivablesRepresentationOfEntityBankAccount] = None
    entity_user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The entity user who created this document.
    """

    entity_vat_id: typing.Optional[ReceivableEntityVatIdResponse] = None
    file: typing.Optional[ReceivableFileSchema] = None
    file_language: LanguageCodeEnum = pydantic.Field()
    """
    The language of the customer-facing PDF file (`file_url`). The value matches the counterpart's `language` at the time when this PDF file was generated.
    """

    file_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The receivable's PDF URL in the counterpart's default language.
    """

    fulfillment_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date when the goods are shipped or the service is provided.
    
    If omitted, defaults to the invoice issue date,
    and the value is automatically set when the invoice status changes to `issued`.
    """

    issue_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Optional field for the issue of the entry.
    """

    line_items: typing.List[ResponseItem]
    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note with additional information for a receivable.
    """

    original_file_language: LanguageCodeEnum = pydantic.Field()
    """
    The language of the entity's copy of the PDF file (`original_file_url`). The value matches the entity's `language` at the time when this PDF file was generated.
    """

    original_file_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The receivable's PDF URL in the entity's default language.
    """

    overdue_reminder_id: typing.Optional[str] = None
    paid_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date and time when the invoice was paid.
    """

    partner_metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Metadata for partner needs
    """

    payment_page_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the invoice's payment page. Either Monite's payment links or your custom payment links.
    """

    payment_reminder_id: typing.Optional[str] = None
    payment_terms: typing.Optional[PaymentTerms] = None
    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A project related to current receivable
    """

    purchase_order: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contain purchase order number.
    """

    recurrence_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stores an unique ID of a recurrence if the receivable is in a recurring status
    """

    related_documents: RelatedDocuments = pydantic.Field()
    """
    Ids of documents that relate to invoice. I.e credit notes, proforma invoices, etc.
    """

    status: ReceivablesStatusEnum = pydantic.Field()
    """
    The status of the receivable inside the receivable workflow.
    """

    subtotal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The subtotal (excluding VAT), in [minor units](https://docs.monite.com/docs/currencies#minor-units).
    """

    tags: typing.Optional[typing.List[TagReadSchema]] = pydantic.Field(default=None)
    """
    The list of tags for this receivable.
    """

    total_amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total price of the receivable in [minor units](https://docs.monite.com/docs/currencies#minor-units). Calculated as a subtotal + total_vat_amount.
    """

    total_amount_with_credit_notes: int = pydantic.Field()
    """
    The total price of the receivable in [minor units](https://docs.monite.com/docs/currencies#minor-units), including VAT and excluding all issued credit notes.
    """

    total_vat_amount: int = pydantic.Field()
    """
    The total VAT of all line items, in [minor units](https://docs.monite.com/docs/currencies#minor-units).
    """

    total_vat_amounts: typing.Optional[typing.List[TotalVatAmountItem]] = pydantic.Field(default=None)
    """
    List of total vat amount for each VAT, presented in receivable
    """

    total_withholding_tax: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total price of the receivable with tax withheld in minor units
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
