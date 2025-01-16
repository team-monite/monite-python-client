# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .iteration_status import IterationStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class RecurrenceIteration(UniversalBaseModel):
    issue_at: str
    issued_invoice_id: typing.Optional[str] = None
    iteration: typing.Optional[int] = None
    status: IterationStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
