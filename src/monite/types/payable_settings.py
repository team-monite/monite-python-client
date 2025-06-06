# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PayableSettings(UniversalBaseModel):
    allow_cancel_duplicates_automatically: typing.Optional[bool] = None
    allow_counterpart_autocreation: typing.Optional[bool] = None
    allow_counterpart_autolinking: typing.Optional[bool] = None
    allow_credit_note_autolinking: typing.Optional[bool] = None
    approve_page_url: str
    default_state: typing.Optional[str] = pydantic.Field(default=None)
    """
    A state each new payable will have upon creation
    """

    enable_line_items: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Starting from version 2024-05-25 by default is always set to True.
    """

    skip_approval_for_paid_invoice: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
