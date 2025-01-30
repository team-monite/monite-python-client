# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .payment_page_theme import PaymentPageTheme
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PaymentsSettingsOutput(UniversalBaseModel):
    payment_page_domain: typing.Optional[str] = None
    payment_page_theme: typing.Optional[PaymentPageTheme] = None
    support_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The support email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
