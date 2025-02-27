# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .item import Item
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class LabelNValue(UniversalBaseModel):
    """
    A label-value pair extracted from an uploaded document by OCR.
    For example, the label could be "Total" and the value could be a currency amount.
    """

    label: Item = pydantic.Field()
    """
    Text label.
    """

    value: Item = pydantic.Field()
    """
    The value (if any).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
