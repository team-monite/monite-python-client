# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .discount import Discount
import pydantic
from .line_item_product import LineItemProduct
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ResponseItem(UniversalBaseModel):
    discount: typing.Optional[Discount] = pydantic.Field(default=None)
    """
    The discount for a product.
    """

    product: LineItemProduct
    quantity: float = pydantic.Field()
    """
    The quantity of each of the goods, materials, or services listed in the receivable.
    """

    total_before_vat: int = pydantic.Field()
    """
    Total of line_item before VAT in [minor units](https://docs.monite.com/references/currencies#minor-units).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
