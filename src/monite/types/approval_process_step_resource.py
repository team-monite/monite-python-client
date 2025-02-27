# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .approval_process_step_status import ApprovalProcessStepStatus
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ApprovalProcessStepResource(UniversalBaseModel):
    object_id: str
    required_approval_count: int
    status: ApprovalProcessStepStatus
    user_ids: typing.List[str]
    role_ids: typing.List[str]
    approved_by: typing.List[str]
    rejected_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
