# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .button_theme_response import ButtonThemeResponse
from .card_theme_response import CardThemeResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PaymentPageThemeResponse(UniversalBaseModel):
    background_color: typing.Optional[str] = None
    border_radius: typing.Optional[str] = None
    button: typing.Optional[ButtonThemeResponse] = None
    card: typing.Optional[CardThemeResponse] = None
    font_color: typing.Optional[str] = None
    font_family: typing.Optional[str] = None
    font_link_href: typing.Optional[str] = None
    logo_src: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
