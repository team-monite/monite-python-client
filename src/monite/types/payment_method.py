# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .payment_method_direction import PaymentMethodDirection
from .monite_all_payment_methods import MoniteAllPaymentMethods
from .payment_method_status import PaymentMethodStatus
from .monite_all_payment_methods_types import MoniteAllPaymentMethodsTypes
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class PaymentMethod(UniversalBaseModel):
    direction: PaymentMethodDirection
    name: MoniteAllPaymentMethods
    status: PaymentMethodStatus
    type: MoniteAllPaymentMethodsTypes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
