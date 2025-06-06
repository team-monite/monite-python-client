# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreviewSchema(UniversalBaseModel):
    """
    A preview image generated for a file.
    """

    height: int = pydantic.Field()
    """
    The image height in pixels.
    """

    url: str = pydantic.Field()
    """
    The image URL.
    """

    width: int = pydantic.Field()
    """
    The image width in pixels.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
