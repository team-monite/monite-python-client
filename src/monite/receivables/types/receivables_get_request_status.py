# This file was auto-generated by Fern from our API Definition.

import typing

ReceivablesGetRequestStatus = typing.Union[
    typing.Literal[
        "draft",
        "issued",
        "accepted",
        "expired",
        "declined",
        "recurring",
        "partially_paid",
        "paid",
        "overdue",
        "uncollectible",
        "canceled",
    ],
    typing.Any,
]
