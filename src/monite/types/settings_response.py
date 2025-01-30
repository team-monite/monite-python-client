# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .language_code_enum import LanguageCodeEnum
from .currency_settings_output import CurrencySettingsOutput
from .reminders_settings import RemindersSettings
from .vat_mode_enum import VatModeEnum
import pydantic
from .payment_priority_enum import PaymentPriorityEnum
from .receivable_edit_flow import ReceivableEditFlow
from .document_i_ds_settings import DocumentIDsSettings
from .ocr_auto_tagging_settings_request import OcrAutoTaggingSettingsRequest
from .accounting_settings import AccountingSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SettingsResponse(UniversalBaseModel):
    language: typing.Optional[LanguageCodeEnum] = None
    currency: typing.Optional[CurrencySettingsOutput] = None
    reminder: typing.Optional[RemindersSettings] = None
    vat_mode: typing.Optional[VatModeEnum] = pydantic.Field(default=None)
    """
    Defines whether the prices of products in receivables will already include VAT or not.
    """

    payment_priority: typing.Optional[PaymentPriorityEnum] = pydantic.Field(default=None)
    """
    Payment preferences for entity to automate calculating suggested payment date based on payment terms and entity preferences.
    """

    allow_purchase_order_autolinking: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Automatically attempt to find a corresponding purchase order for all incoming payables.
    """

    receivable_edit_flow: typing.Optional[ReceivableEditFlow] = None
    document_ids: typing.Optional[DocumentIDsSettings] = None
    payables_ocr_auto_tagging: typing.Optional[typing.List[OcrAutoTaggingSettingsRequest]] = pydantic.Field(
        default=None
    )
    """
    Auto tagging settings for all incoming OCR payable documents.
    """

    quote_signature_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Sets the default behavior of whether a signature is required to accept quotes.
    """

    generate_paid_invoice_pdf: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If enabled, the paid invoice's PDF will be in a new layout set by the user.
    """

    accounting: typing.Optional[AccountingSettings] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
