# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .payment_object_type import PaymentObjectType
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class PaymentObject(UniversalBaseModel):
    id: str
    type: PaymentObjectType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
