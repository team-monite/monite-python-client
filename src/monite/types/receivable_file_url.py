# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReceivableFileUrl(UniversalBaseModel):
    file_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The receivable's PDF URL in the counterpart's default language.
    """

    original_file_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The receivable's PDF URL in the entity's default language.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
