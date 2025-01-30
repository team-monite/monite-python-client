# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class PageSchema2(UniversalBaseModel):
    """
    When a PDF document is uploaded to Monite, it extracts individual pages from the document
    and saves them as PNG images. This object contains the image and metadata of a single page.
    """

    id: str = pydantic.Field()
    """
    A unique ID of the image.
    """

    mimetype: str = pydantic.Field()
    """
    The [media type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types) of the image.
    """

    size: int = pydantic.Field()
    """
    Image file size, in bytes.
    """

    number: int = pydantic.Field()
    """
    The page number in the PDF document, from 0.
    """

    url: str = pydantic.Field()
    """
    The URL to download the image.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
