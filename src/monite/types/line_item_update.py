# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .discount import Discount
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LineItemUpdate(UniversalBaseModel):
    discount: typing.Optional[Discount] = pydantic.Field(default=None)
    """
    The discount for a product.
    """

    price: typing.Optional[int] = pydantic.Field(default=None)
    """
    The actual price of the product in [minor units](https://docs.monite.com/references/currencies#minor-units).
    """

    quantity: typing.Optional[float] = pydantic.Field(default=None)
    """
    The quantity of each of the goods, materials, or services listed in the receivable.
    """

    tax_rate_value: typing.Optional[int] = pydantic.Field(default=None)
    """
    Percent minor units. Example: 12.5% is 1250. This field is only required on invoices issued by entities in the US, Pakistan, and other unsupported countries.
    """

    vat_rate_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier of the vat rate object. This field is required for all entities in supported countries except the US and Pakistan.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
