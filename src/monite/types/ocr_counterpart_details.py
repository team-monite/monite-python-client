# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocr_address_details import OcrAddressDetails
from .ocr_bank_details import OcrBankDetails


class OcrCounterpartDetails(UniversalBaseModel):
    vat_number: typing.Optional[str] = None
    tax_number: typing.Optional[str] = None
    email: typing.Optional[str] = None
    name: typing.Optional[str] = None
    address: OcrAddressDetails
    bank_account: OcrBankDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
