# This file was auto-generated by Fern from our API Definition.

import typing

DocumentObjectTypeRequestEnum = typing.Union[
    typing.Literal[
        "receivables_quote",
        "receivables_invoice",
        "receivables_paid_invoice",
        "receivables_credit_note",
        "receivables_discount_reminder",
        "receivables_final_reminder",
        "payables_purchase_order",
        "payables_notify_approver",
        "payables_notify_payer",
    ],
    typing.Any,
]
