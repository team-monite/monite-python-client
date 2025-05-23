# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .receivable_entity_address_schema import ReceivableEntityAddressSchema
from .update_issued_invoice_entity import UpdateIssuedInvoiceEntity


class UpdateIssuedInvoice(UniversalBaseModel):
    contact_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of the counterpart contact.
    """

    counterpart_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id of a new or updated counterpart
    """

    counterpart_vat_id_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Counterpart VAT ID id
    """

    due_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date by which the invoice must be paid.
    """

    entity: typing.Optional[UpdateIssuedInvoiceEntity] = None
    entity_address: typing.Optional[ReceivableEntityAddressSchema] = None
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

    issue_date: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime when the invoice was issued
    """

    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note with additional information for a receivable
    """

    overdue_reminder_id: typing.Optional[str] = None
    partner_metadata: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Metadata for partner needs
    """

    payment_reminder_id: typing.Optional[str] = None
    payment_terms_id: typing.Optional[str] = None
    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A project related to current receivable
    """

    tag_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IDs of user-defined tags (labels) assigned to this receivable.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
