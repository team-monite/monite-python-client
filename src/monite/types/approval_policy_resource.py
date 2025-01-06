# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
import pydantic
from .approval_policy_resource_script_item import ApprovalPolicyResourceScriptItem
from .approval_policy_resource_trigger import ApprovalPolicyResourceTrigger
from .approval_policy_resource_status import ApprovalPolicyResourceStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ApprovalPolicyResource(UniversalBaseModel):
    starts_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time (in the ISO 8601 format) when the approval policy becomes active. Only payables submitted for approval during the policy's active period will trigger this policy. If omitted or `null`, the policy is effective immediately. The value will be converted to UTC.
    """

    ends_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time (in the ISO 8601 format) when the approval policy stops being active and stops triggering approval workflows.If `ends_at` is provided in the request, then `starts_at` must also be provided and `ends_at` must be later than `starts_at`. The value will be converted to UTC.
    """

    name: str = pydantic.Field()
    """
    The name of the approval policy.
    """

    description: str = pydantic.Field()
    """
    A brief description of the approval policy.
    """

    script: typing.List[ApprovalPolicyResourceScriptItem] = pydantic.Field()
    """
    A list of JSON objects that represents the approval policy script. The script contains the logic that determines whether an action should be sent to approval. This field is required, and it should contain at least one script object.
    """

    trigger: typing.Optional[ApprovalPolicyResourceTrigger] = pydantic.Field(default=None)
    """
    A JSON object that represents the trigger for the approval policy. The trigger specifies the event that will trigger the policy to be evaluated.
    """

    id: str
    status: ApprovalPolicyResourceStatus = pydantic.Field()
    """
    The current status of the approval policy.
    """

    created_at: dt.datetime
    updated_at: dt.datetime
    created_by: str
    updated_by: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
