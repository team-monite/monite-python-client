# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .currency_enum import CurrencyEnum
from .ocr_counterpart_details import OcrCounterpartDetails
from .ocr_line_item import OcrLineItem


class OcrCreditNote(UniversalBaseModel):
    document_number: typing.Optional[str] = None
    original_invoice_number: typing.Optional[str] = None
    issue_date: typing.Optional[str] = None
    currency: typing.Optional[CurrencyEnum] = None
    subtotal: typing.Optional[float] = None
    tax_rate: typing.Optional[float] = None
    tax_amount: typing.Optional[float] = None
    total_amount: typing.Optional[float] = None
    sender: OcrCounterpartDetails
    recipient: OcrCounterpartDetails
    line_items: typing.List[OcrLineItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
