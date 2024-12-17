# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import datetime as dt
from .recipient import Recipient
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class OnboardingLinkResponse(UniversalBaseModel):
    id: str
    created_at: dt.datetime
    expires_at: dt.datetime
    recipient: Recipient
    refresh_url: str
    return_url: str
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
