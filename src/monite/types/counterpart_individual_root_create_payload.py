# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .counterpart_individual_create_payload import CounterpartIndividualCreatePayload
import typing
from .language_code_enum import LanguageCodeEnum
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CounterpartIndividualRootCreatePayload(UniversalBaseModel):
    """
    This schema is used to create counterparts that are individuals (natural persons).
    """

    individual: CounterpartIndividualCreatePayload
    language: typing.Optional[LanguageCodeEnum] = pydantic.Field(default=None)
    """
    The language used to generate PDF documents for this counterpart.
    """

    reminders_enabled: typing.Optional[bool] = None
    tax_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The counterpart's taxpayer identification number or tax ID. For identification purposes, this field may be required for counterparts that are not VAT-registered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
