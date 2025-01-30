# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
import datetime as dt
import typing
from .currency_exchange_schema import CurrencyExchangeSchema
from .tag_read_schema import TagReadSchema
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreditNoteResponse(UniversalBaseModel):
    """
    Schema for credit note response. Includes all fields that can be returned from the API.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the credit note
    """

    created_at: dt.datetime = pydantic.Field()
    """
    Date and time when the credit note was created in the system
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    Date and time of the last update to the credit note
    """

    based_on: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the payable this credit note is based on
    """

    based_on_document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The document ID of the original payable that this credit note refers to
    """

    counterpart_address_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the counterpart's address
    """

    counterpart_bank_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the counterpart's bank account
    """

    counterpart_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the counterpart
    """

    counterpart_vat_id_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the counterpart's VAT registration
    """

    created_by_external_user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External system's user ID for the creator
    """

    created_by_external_user_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the external user who created the credit note
    """

    created_by_user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the user who created the credit note
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency code
    """

    currency_exchange: typing.Optional[CurrencyExchangeSchema] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the credit note
    """

    document_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The credit note's unique document number
    """

    entity_id: str = pydantic.Field()
    """
    The ID of the entity to which the credit note belongs
    """

    file_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the credit note file stored in the file saver.
    """

    file_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the credit note file stored in the file saver.
    """

    issued_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date when the credit note was issued
    """

    ocr_request_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the OCR processing request
    """

    ocr_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status of OCR processing
    """

    origin: str = pydantic.Field()
    """
    The origin or source system of the credit note
    """

    project_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the associated project
    """

    sender: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the sender
    """

    source_of_data: str = pydantic.Field()
    """
    How the data was input (ocr/user_specified)
    """

    status: str = pydantic.Field()
    """
    The current status of the credit note in its lifecycle
    """

    subtotal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The subtotal amount before taxes
    """

    tags: typing.Optional[typing.List[TagReadSchema]] = pydantic.Field(default=None)
    """
    List of tags associated with this credit note
    """

    tax: typing.Optional[int] = pydantic.Field(default=None)
    """
    The tax percentage
    """

    tax_amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The calculated tax amount
    """

    total_amount: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total amount including taxes
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
