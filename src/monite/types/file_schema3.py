# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_schema3 import PageSchema3
from .preview_schema3 import PreviewSchema3


class FileSchema3(UniversalBaseModel):
    """
    Represents a file (such as a PDF invoice) that was uploaded to Monite.
    """

    id: str = pydantic.Field()
    """
    A unique ID of this file.
    """

    created_at: dt.datetime = pydantic.Field()
    """
    UTC date and time when this file was uploaded to Monite. Timestamps follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    file_type: str = pydantic.Field()
    """
    The type of the business object associated with this file.
    """

    md5: str = pydantic.Field()
    """
    The MD5 hash of the file.
    """

    mimetype: str = pydantic.Field()
    """
    The file's [media type](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types).
    """

    name: str = pydantic.Field()
    """
    The original file name (if available).
    """

    pages: typing.Optional[typing.List[PageSchema3]] = pydantic.Field(default=None)
    """
    If the file is a PDF document, this property contains individual pages extracted from the file. Otherwise, an empty array.
    """

    previews: typing.Optional[typing.List[PreviewSchema3]] = pydantic.Field(default=None)
    """
    Preview images generated for this file. There can be multiple images with different sizes.
    """

    region: str = pydantic.Field()
    """
    Geographical region of the data center where the file is stored.
    """

    size: int = pydantic.Field()
    """
    The file size in bytes.
    """

    url: str = pydantic.Field()
    """
    The URL to download the file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
