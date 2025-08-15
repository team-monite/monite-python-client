# Reference
## Analytics
<details><summary><code>client.analytics.<a href="src/monite/analytics/client.py">get_analytics_credit_notes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve aggregated statistics for payables with different breakdowns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.analytics.get_analytics_credit_notes(
    metric="id",
    aggregation_function="count",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**metric:** `CreditNoteMetricEnum` 
    
</dd>
</dl>

<dl>
<dd>

**aggregation_function:** `AggregationFunctionEnum` 
    
</dd>
</dl>

<dl>
<dd>

**dimension:** `typing.Optional[CreditNoteDimensionEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**date_dimension_breakdown:** `typing.Optional[DateDimensionBreakdownEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 400) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**has_file:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PayableCreditNoteStateEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**status_not_in:** `typing.Optional[
    typing.Union[
        PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[OriginEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.analytics.<a href="src/monite/analytics/client.py">get_analytics_payables</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve aggregated statistics for payables with different breakdowns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.analytics.get_analytics_payables(
    metric="id",
    aggregation_function="count",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**metric:** `PayableMetricEnum` 
    
</dd>
</dl>

<dl>
<dd>

**aggregation_function:** `AggregationFunctionEnum` 
    
</dd>
</dl>

<dl>
<dd>

**dimension:** `typing.Optional[PayableDimensionEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**date_dimension_breakdown:** `typing.Optional[DateDimensionBreakdownEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 400) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only payables created in Monite after the specified date and time. The value must be in the ISO 8601 format YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm].
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only payables created in Monite before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only payables created in Monite on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only payables created in Monite before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PayableStateEnum]` 

Return only payables that have the specified [status](https://docs.monite.com/accounts-payable/payables/index).

To query multiple statuses at once, use the `status__in` parameter instead.
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]
]` 

Return only payables that have the specified [statuses](https://docs.monite.com/accounts-payable/payables/index).

To specify multiple statuses, repeat this parameter for each value: `status__in=draft&status__in=new`
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only payables with specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value: `id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Return only payables with the exact specified total amount. The amount must be specified in the minor units of currency. For example, $12.5 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — Return only payables with the specified amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_gt:** `typing.Optional[int]` — Return only payables whose amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_lt:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_gte:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_lte:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — Return only payables that use the specified currency.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` 

Return only payables received from counterparts with the specified name (exact match, case-sensitive).

For counterparts of `type = individual`, the full name is formatted as `first_name last_name`.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` — Return only payables received from counterparts whose name contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` — Return only payables received from counterparts whose name contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Apply the `icontains` condition to search for the specified text in the `document_id` and `counterpart_name` fields in the payables.
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — Return payables that are due on the specified date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[str]` — Return payables that are due after the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[str]` — Return payables that are due before the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[str]` — Return payables that are due on or after the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[str]` — Return payables that are due before or on the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` — Return payables that are issued at the specified date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gt:** `typing.Optional[str]` — Return payables that are issued after the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lt:** `typing.Optional[str]` — Return payables that are issued before the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gte:** `typing.Optional[str]` — Return payables that are issued on or after the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lte:** `typing.Optional[str]` — Return payables that are issued before or on the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 

Return a payable with the exact specified document number (case-sensitive).

The `document_id` is the user-facing document number such as INV-00042, not to be confused with Monite resource IDs (`id`).
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` — Return only payables whose document number (`document_id`) contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` — Return only payables whose document number (`document_id`) contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**was_created_by_user_id:** `typing.Optional[str]` — Return only payables created in Monite by the entity user with the specified ID.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 

Return only payables received from the counterpart with the specified ID.

Counterparts that have been deleted but have associated payables will still return results here because the payables contain a frozen copy of the counterpart data.

If the specified counterpart ID does not exist and never existed, no results are returned.
    
</dd>
</dl>

<dl>
<dd>

**source_of_payable_data:** `typing.Optional[SourceOfPayableDataEnum]` — Return only payables coming from the specified source.
    
</dd>
</dl>

<dl>
<dd>

**ocr_status:** `typing.Optional[OcrStatusEnum]` — Return only payables with specific OCR statuses.
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `typing.Optional[str]` — Search for a payable by the identifier of the line item associated with it.
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_id:** `typing.Optional[str]` — Search for a payable by the identifier of the purchase order associated with it.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 

Return only payables assigned to the project with the specified ID.

Valid but nonexistent project IDs do not raise errors but return no results.
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `project_id` include at least one of the project_id with the specified IDs. Valid but nonexistent project IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `tags` include at least one of the tags with the specified IDs. Valid but nonexistent tag IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_not_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `tags` do not include any of the tags with the specified IDs. Valid but nonexistent tag IDs do not raise errors but produce the results.
    
</dd>
</dl>

<dl>
<dd>

**has_tags:** `typing.Optional[bool]` — Filter objects based on whether they have tags. If true, only objects with tags are returned. If false, only objects without tags are returned.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[PayableOriginEnum]` — Return only payables from a given origin ['einvoice', 'upload', 'email']
    
</dd>
</dl>

<dl>
<dd>

**has_file:** `typing.Optional[bool]` — Return only payables with or without attachments (files)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.analytics.<a href="src/monite/analytics/client.py">get_analytics_receivables</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve aggregated statistics for receivables with different breakdowns.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.analytics.get_analytics_receivables(
    metric="id",
    aggregation_function="count",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**metric:** `ReceivableMetricEnum` 
    
</dd>
</dl>

<dl>
<dd>

**aggregation_function:** `AggregationFunctionEnum` 
    
</dd>
</dl>

<dl>
<dd>

**dimension:** `typing.Optional[ReceivableDimensionEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**date_dimension_breakdown:** `typing.Optional[DateDimensionBreakdownEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 250) to return in a single page of the response. Default is 100. The response may contain fewer items if it is the last or only page. 

When using pagination with a non-default `limit`, you must provide the `limit` value alongside `pagination_token` in all subsequent pagination requests. Unlike other query parameters, `limit` is not inferred from `pagination_token`.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters except `limit` are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables with the specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value:
`id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        GetAnalyticsReceivablesRequestStatusInItem,
        typing.Sequence[GetAnalyticsReceivablesRequestStatusInItem],
    ]
]` 

Return only receivables that have the specified statuses. See the applicable [invoice statuses](https://docs.monite.com/accounts-receivable/invoices/index), [quote statuses](https://docs.monite.com/accounts-receivable/quotes/index), and [credit note statuses](https://docs.monite.com/accounts-receivable/credit-notes#credit-note-lifecycle).

To specify multiple statuses, repeat this parameter for each value:
`status__in=draft&status__in=issued`
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables created by the entity users with the specified IDs.To specify multiple user IDs, repeat this parameter for each ID:
`entity_user_id__in=<user1>&entity_user_id__in=<user2>`

If the request is authenticated using an entity user token, this user must have the `receivable.read.allowed` (rather than `allowed_for_own`) permission to be able to query receivables created by other users.

IDs of deleted users will still produce results here if those users had associated receivables. Valid but nonexistent user IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceivableCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose [tags](https://docs.monite.com/common/tags) include at least one of the tags with the specified IDs.

For example, given receivables with the following tags:
1. tagA
2. tagB
3. tagA, tagB
4. tagC
5. tagB, tagC


`tag_ids__in=<tagA>&tag_ids__in=<tagB>` will return receivables 1, 2, 3, and 5.

Valid but nonexistent tag IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose [tags](https://docs.monite.com/common/tags) include all of the tags with the specified IDs and optionally other tags that are not specified.

For example, given receivables with the following tags:
1. tagA
2. tagB
3. tagA, tagB
4. tagC
5. tagA, tagB, tagC


`tag_ids=<tagA>&tag_ids=<tagB>` will return receivables 3 and 5.
    
</dd>
</dl>

<dl>
<dd>

**product_ids_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose line items include at least one of the product IDs with the specified IDs. 

To specify multiple product IDs, repeat this parameter for each ID:
`product_ids__in=<product1>&product_ids__in=<product2>`

For example, given receivables with the following product IDs:
1. productA
2. productB
3. productA, productB
4. productC
5. productB, productC


`product_ids__in=<productA>&product_ids__in=<productB>` will return receivables 1, 2, 3, and 5.Valid but nonexistent product IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**product_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose line items include all of the product IDs with the specified IDs and optionally other products that are not specified. 

To specify multiple product IDs, repeat this parameter for each ID:
`product_ids=<product1>&product_ids=<product2>`

For example, given receivables with the following product IDs:
1. productA
2. productB
3. productA, productB
4. productC
5. productA, productB, productC


`product_ids=<productA>&product_ids=<productB>` will return receivables 3 and 5.
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only receivables whose `project_id` include at least one of the project_id with the specified IDs. Valid but nonexistent project IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ReceivableType]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetAnalyticsReceivablesRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Approval policies
<details><summary><code>client.approval_policies.<a href="src/monite/approval_policies/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all approval policies with pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**process_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ApprovalPolicyCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ApprovalPoliciesGetRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        ApprovalPoliciesGetRequestStatusInItem,
        typing.Sequence[ApprovalPoliciesGetRequestStatusInItem],
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_ncontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.<a href="src/monite/approval_policies/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new approval policy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.create(
    name="name",
    script=[True],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The name of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.Sequence[ApprovalPolicyCreateScriptItem]` — A list of JSON objects that represents the approval policy script. The script contains the logic that determines whether an action should be sent to approval. This field is required, and it should contain at least one script object.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**ends_at:** `typing.Optional[dt.datetime]` — The date and time (in the ISO 8601 format) when the approval policy stops being active and stops triggering approval workflows.If `ends_at` is provided in the request, then `starts_at` must also be provided and `ends_at` must be later than `starts_at`. The value will be converted to UTC.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` — The priority controls which approval policy takes precedence when a payable matches multiple approval policies. A higher value mean higher priority.
    
</dd>
</dl>

<dl>
<dd>

**starts_at:** `typing.Optional[dt.datetime]` — The date and time (in the ISO 8601 format) when the approval policy becomes active. Only payables submitted for approval during the policy's active period will trigger this policy. If omitted or `null`, the policy is effective immediately. The value will be converted to UTC.
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Optional[ApprovalPolicyCreateTrigger]` — A JSON object that represents the trigger for the approval policy. The trigger specifies the event that will trigger the policy to be evaluated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.<a href="src/monite/approval_policies/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific approval policy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.get_by_id(
    approval_policy_id="approval_policy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.<a href="src/monite/approval_policies/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing approval policy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.delete_by_id(
    approval_policy_id="approval_policy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.<a href="src/monite/approval_policies/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing approval policy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.update_by_id(
    approval_policy_id="approval_policy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**ends_at:** `typing.Optional[dt.datetime]` — The date and time (in the ISO 8601 format) when the approval policy stops being active and stops triggering approval workflows.If `ends_at` is provided in the request, then `starts_at` must also be provided and `ends_at` must be later than `starts_at`. The value will be converted to UTC.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The name of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` — The priority controls which approval policy takes precedence when a payable matches multiple approval policies. A higher value mean higher priority.
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.Optional[typing.Sequence[ApprovalPolicyUpdateScriptItem]]` — A list of JSON objects that represents the approval policy script. The script contains the logic that determines whether an action should be sent to approval. This field is required, and it should contain at least one script object.
    
</dd>
</dl>

<dl>
<dd>

**starts_at:** `typing.Optional[dt.datetime]` — The date and time (in the ISO 8601 format) when the approval policy becomes active. Only payables submitted for approval during the policy's active period will trigger this policy. If omitted or `null`, the policy is effective immediately. The value will be converted to UTC.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ApprovalPolicyStatus]` — A string that represents the current status of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Optional[ApprovalPolicyUpdateTrigger]` — A JSON object that represents the trigger for the approval policy. The trigger specifies the event that will trigger the policy to be evaluated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Approval requests
<details><summary><code>client.approval_requests.<a href="src/monite/approval_requests/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_requests.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ApprovalRequestCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ApprovalRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[ApprovalRequestStatus, typing.Sequence[ApprovalRequestStatus]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[ObjectType]` 
    
</dd>
</dl>

<dl>
<dd>

**object_type_in:** `typing.Optional[typing.Union[ObjectType, typing.Sequence[ObjectType]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_requests.<a href="src/monite/approval_requests/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import ApprovalRequestCreateByRoleRequest, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_requests.create(
    request=ApprovalRequestCreateByRoleRequest(
        object_id="object_id",
        object_type="account",
        required_approval_count=1,
        role_ids=["role_ids"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ApprovalRequestCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_requests.<a href="src/monite/approval_requests/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_requests.get_by_id(
    approval_request_id="approval_request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_requests.<a href="src/monite/approval_requests/client.py">approve_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_requests.approve_by_id(
    approval_request_id="approval_request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_requests.<a href="src/monite/approval_requests/client.py">cancel_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_requests.cancel_by_id(
    approval_request_id="approval_request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_requests.<a href="src/monite/approval_requests/client.py">reject_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_requests.reject_by_id(
    approval_request_id="approval_request_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Access tokens
<details><summary><code>client.access_tokens.<a href="src/monite/access_tokens/client.py">revoke</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an existing token immediately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.access_tokens.revoke(
    client_id="client_id",
    client_secret="client_secret",
    token="token",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Your partner [client ID](https://docs.monite.com/get-started/credentials#get-credentials) obtained from the "API Credentials" section of Monite Partner Portal. Note that the sandbox and production environment use different client IDs.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Your partner [client secret](https://docs.monite.com/get-started/credentials#get-credentials) obtained from the "API Credentials" section of Monite Partner Portal. Note that the sandbox and production environment use different client secrets.
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` — The token to revoke.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.access_tokens.<a href="src/monite/access_tokens/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new access token based on client ID and client secret.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.access_tokens.create(
    client_id="eb959578-a74d-4ac3-8b25-bf0910027857",
    client_secret="14c84a34-282b-4fd8-8af6-86b5b5f2c212",
    entity_user_id="7abd8744-507c-40e6-a5ca-34aa480b3991",
    grant_type="entity_user",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Your partner [client ID](https://docs.monite.com/get-started/credentials#get-credentials) obtained from the "API Credentials" section of Monite Partner Portal. Note that the sandbox and production environment use different client IDs.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Your partner [client secret](https://docs.monite.com/get-started/credentials#get-credentials) obtained from the "API Credentials" section of Monite Partner Portal. Note that the sandbox and production environment use different client secrets.
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `GrantType` 

The type of the access token to generate:

 * `client_credentials` - partner-level access token,
 * `entity_user` - entity user token.
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` — ID of the entity user to generate the access token for. Used only if `grant_type` is `entity_user`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Comments
<details><summary><code>client.comments.<a href="src/monite/comments/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get comments
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.comments.get(
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CommentCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/monite/comments/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new comment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.comments.create(
    object_id="object_id",
    object_type="object_type",
    text="text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reply_to_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/monite/comments/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get comment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.comments.get_by_id(
    comment_id="comment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/monite/comments/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete comment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.comments.delete_by_id(
    comment_id="comment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.comments.<a href="src/monite/comments/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update comment
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.comments.update_by_id(
    comment_id="comment_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**comment_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reply_to_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Counterparts
<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.get(
    sort_code="123456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**iban:** `typing.Optional[str]` — The IBAN of the counterpart's bank account.
    
</dd>
</dl>

<dl>
<dd>

**sort_code:** `typing.Optional[str]` — The bank's sort code.
    
</dd>
</dl>

<dl>
<dd>

**account_number:** `typing.Optional[str]` — The bank account number. Required for US bank accounts to accept ACH payments. US account numbers contain 9 to 12 digits. UK account numbers typically contain 8 digits.
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The tax ID of the counterpart.
    
</dd>
</dl>

<dl>
<dd>

**vat_id:** `typing.Optional[str]` — The VAT ID of the counterpart.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of counterpart IDs to search through.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CounterpartCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CounterpartType]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_vendor:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_customer:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**address_country:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_city:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_postal_code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_state:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_line1:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**address_line2:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import (
    CounterpartAddress,
    CounterpartCreatePayload_Organization,
    CounterpartOrganizationCreatePayload,
    Monite,
)

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.create(
    request=CounterpartCreatePayload_Organization(
        organization=CounterpartOrganizationCreatePayload(
            address=CounterpartAddress(
                city="Berlin",
                country="AF",
                line1="Flughafenstrasse 52",
                postal_code="10115",
            ),
            is_customer=True,
            is_vendor=True,
            legal_name="Acme Inc.",
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `CounterpartCreatePayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.get_by_id(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.delete_by_id(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import (
    CounterpartIndividualRootUpdatePayload,
    CounterpartIndividualUpdatePayload,
    Monite,
)

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.update_by_id(
    counterpart_id="counterpart_id",
    request=CounterpartIndividualRootUpdatePayload(
        individual=CounterpartIndividualUpdatePayload(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CounterpartUpdatePayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">get_partner_metadata_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.get_partner_metadata_by_id(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.<a href="src/monite/counterparts/client.py">update_partner_metadata_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.update_partner_metadata_by_id(
    counterpart_id="counterpart_id",
    metadata={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Optional[typing.Any]]` — Metadata for partner needs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Counterpart e-invoicing credentials
<details><summary><code>client.counterpart_e_invoicing_credentials.<a href="src/monite/counterpart_e_invoicing_credentials/client.py">get_counterparts_id_einvoicing_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterpart_e_invoicing_credentials.get_counterparts_id_einvoicing_credentials(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterpart_e_invoicing_credentials.<a href="src/monite/counterpart_e_invoicing_credentials/client.py">post_counterparts_id_einvoicing_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import CounterpartEinvoicingCredentialSchema, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterpart_e_invoicing_credentials.post_counterparts_id_einvoicing_credentials(
    counterpart_id="counterpart_id",
    request=CounterpartEinvoicingCredentialSchema(
        network_identifier="DE087095777",
        network_schema="DE:VAT",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateCounterpartEinvoicingCredentialPayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterpart_e_invoicing_credentials.<a href="src/monite/counterpart_e_invoicing_credentials/client.py">get_counterparts_id_einvoicing_credentials_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterpart_e_invoicing_credentials.get_counterparts_id_einvoicing_credentials_id(
    credential_id="credential_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterpart_e_invoicing_credentials.<a href="src/monite/counterpart_e_invoicing_credentials/client.py">delete_counterparts_id_einvoicing_credentials_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterpart_e_invoicing_credentials.delete_counterparts_id_einvoicing_credentials_id(
    credential_id="credential_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterpart_e_invoicing_credentials.<a href="src/monite/counterpart_e_invoicing_credentials/client.py">patch_counterparts_id_einvoicing_credentials_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterpart_e_invoicing_credentials.patch_counterparts_id_einvoicing_credentials_id(
    credential_id="credential_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**network_identifier:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**network_schema:** `typing.Optional[EinvoiceSchemaTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Custom VAT rates
<details><summary><code>client.custom_vat_rates.<a href="src/monite/custom_vat_rates/client.py">get_custom_vat_rates</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.custom_vat_rates.get_custom_vat_rates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_vat_rates.<a href="src/monite/custom_vat_rates/client.py">post_custom_vat_rates</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, VatRateComponent

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.custom_vat_rates.post_custom_vat_rates(
    components=[
        VatRateComponent(
            name="name",
            value=1.1,
        )
    ],
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**components:** `typing.Sequence[VatRateComponent]` — Sub-taxes included in the Custom VAT.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Display name of the Custom VAT.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_vat_rates.<a href="src/monite/custom_vat_rates/client.py">get_custom_vat_rates_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.custom_vat_rates.get_custom_vat_rates_id(
    custom_vat_rate_id="custom_vat_rate_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_vat_rate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_vat_rates.<a href="src/monite/custom_vat_rates/client.py">delete_custom_vat_rates_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.custom_vat_rates.delete_custom_vat_rates_id(
    custom_vat_rate_id="custom_vat_rate_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_vat_rate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_vat_rates.<a href="src/monite/custom_vat_rates/client.py">patch_custom_vat_rates_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.custom_vat_rates.patch_custom_vat_rates_id(
    custom_vat_rate_id="custom_vat_rate_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom_vat_rate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**components:** `typing.Optional[typing.Sequence[VatRateComponent]]` — Sub-taxes included in the Custom VAT.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name of the Custom VAT.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DataExports
<details><summary><code>client.data_exports.<a href="src/monite/data_exports/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[DataExportCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.<a href="src/monite/data_exports/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request the export of payable and receivable documents with the specified statuses.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import ExportObjectSchema_Payable, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.create(
    date_from="date_from",
    date_to="date_to",
    format="csv",
    objects=[
        ExportObjectSchema_Payable(
            statuses=["draft"],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**date_from:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**format:** `ExportFormat` 
    
</dd>
</dl>

<dl>
<dd>

**objects:** `typing.Sequence[ExportObjectSchema]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.<a href="src/monite/data_exports/client.py">get_supported_formats</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.get_supported_formats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.<a href="src/monite/data_exports/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.get_by_id(
    document_export_id="document_export_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_export_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Delivery notes
<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">get_delivery_notes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all delivery notes with filtering and pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.get_delivery_notes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[DeliveryNoteCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[DeliveryNoteStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        DeliveryNoteStatusEnum, typing.Sequence[DeliveryNoteStatusEnum]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on_document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on_document_id_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on_document_id_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_date_gt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_date_lt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_date_gte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**delivery_date_lte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">post_delivery_notes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import DeliveryNoteCreateBasedOnRequest, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.post_delivery_notes(
    request=DeliveryNoteCreateBasedOnRequest(
        based_on="e78de69c-c789-44ef-80bf-474b9e63b91d",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `Payload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">get_delivery_notes_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.get_delivery_notes_id(
    delivery_note_id="delivery_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delivery_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">delete_delivery_notes_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.delete_delivery_notes_id(
    delivery_note_id="delivery_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delivery_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">patch_delivery_notes_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.patch_delivery_notes_id(
    delivery_note_id="delivery_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delivery_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — ID of the counterpart address selected for the delivery note
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — ID of the counterpart
    
</dd>
</dl>

<dl>
<dd>

**delivery_date:** `typing.Optional[str]` — Date of delivery
    
</dd>
</dl>

<dl>
<dd>

**delivery_number:** `typing.Optional[str]` — Delivery number
    
</dd>
</dl>

<dl>
<dd>

**display_signature_placeholder:** `typing.Optional[bool]` — Whether to display a signature placeholder in the generated PDF
    
</dd>
</dl>

<dl>
<dd>

**line_items:** `typing.Optional[typing.Sequence[DeliveryNoteCreateLineItem]]` — List of line items in the delivery note
    
</dd>
</dl>

<dl>
<dd>

**memo:** `typing.Optional[str]` — An optional note for the customer, displayed above the line items table in the PDF.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">post_delivery_notes_id_cancel</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.post_delivery_notes_id_cancel(
    delivery_note_id="delivery_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delivery_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.delivery_notes.<a href="src/monite/delivery_notes/client.py">post_delivery_notes_id_mark_as_delivered</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.delivery_notes.post_delivery_notes_id_mark_as_delivered(
    delivery_note_id="delivery_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**delivery_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PDF templates
<details><summary><code>client.pdf_templates.<a href="src/monite/pdf_templates/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API call returns all supported templates with language codes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.pdf_templates.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pdf_templates.<a href="src/monite/pdf_templates/client.py">get_system</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This API call returns all supported system templates with language codes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.pdf_templates.get_system()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pdf_templates.<a href="src/monite/pdf_templates/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.pdf_templates.get_by_id(
    document_template_id="document_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.pdf_templates.<a href="src/monite/pdf_templates/client.py">make_default_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.pdf_templates.make_default_by_id(
    document_template_id="document_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## E-invoicing search
<details><summary><code>client.e_invoicing_search.<a href="src/monite/e_invoicing_search/client.py">get_einvoice_search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks if the specified VAT number or business number is registered on the PEPPOL network as a receiver. For example, you can use this endpoint to check if an entity's counterparts are registered in PEPPOL before creating e-invoices for those counterparts.

The lookup is powered by PEPPOL SMPs (Service Metadata Publishers) so it also includes registrations that are not visible in the public PEPPOL directory.

Both partner tokens and entity user tokens can be used for authentication.

Production and sandbox lookups are separate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_search.get_einvoice_search(
    network_identifier="DE010101010",
    network_schema="DE:VAT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**network_identifier:** `str` 

VAT number or business number, depending on the `network_schema` used. VAT numbers must include the country prefix, for example, use `DE010101010` not `10101010`.

**Note:** This endpoint does not validate the format of VAT numbers and business numbers (such as the length or characters used). Invalid values will return `{"exists": false}`.
    
</dd>
</dl>

<dl>
<dd>

**network_schema:** `EinvoiceSchemaTypeEnum` — [PEPPOL scheme](https://docs.monite.com/e-invoicing/peppol-ids#schemes) name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## E-invoicing connections
<details><summary><code>client.e_invoicing_connections.<a href="src/monite/e_invoicing_connections/client.py">get_einvoicing_connections</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_connections.get_einvoicing_connections()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_invoicing_connections.<a href="src/monite/e_invoicing_connections/client.py">post_einvoicing_connections</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import EinvoicingAddress, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_connections.post_einvoicing_connections(
    address=EinvoicingAddress(
        address_line1="address_line1",
        city="city",
        country="DE",
        postal_code="postal_code",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `EinvoicingAddress` — Integration Address
    
</dd>
</dl>

<dl>
<dd>

**entity_vat_id_id:** `typing.Optional[str]` — Entity VAT ID identifier for the integration
    
</dd>
</dl>

<dl>
<dd>

**is_receiver:** `typing.Optional[bool]` — Set to `true` if the entity needs to receive e-invoices.
    
</dd>
</dl>

<dl>
<dd>

**is_sender:** `typing.Optional[bool]` — Set to `true` if the entity needs to send e-invoices. Either `is_sender` or `is_receiver` or both must be `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_invoicing_connections.<a href="src/monite/e_invoicing_connections/client.py">get_einvoicing_connections_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_connections.get_einvoicing_connections_id(
    einvoicing_connection_id="einvoicing_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**einvoicing_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_invoicing_connections.<a href="src/monite/e_invoicing_connections/client.py">delete_einvoicing_connections_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_connections.delete_einvoicing_connections_id(
    einvoicing_connection_id="einvoicing_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**einvoicing_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_invoicing_connections.<a href="src/monite/e_invoicing_connections/client.py">patch_einvoicing_connections_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_connections.patch_einvoicing_connections_id(
    einvoicing_connection_id="einvoicing_connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**einvoicing_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[UpdateEinvoicingAddress]` — Integration Address
    
</dd>
</dl>

<dl>
<dd>

**is_receiver:** `typing.Optional[bool]` — Set to `true` if the entity needs to receive e-invoices.
    
</dd>
</dl>

<dl>
<dd>

**is_sender:** `typing.Optional[bool]` — Set to `true` if the entity needs to send e-invoices. Either `is_sender` or `is_receiver` or both must be `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.e_invoicing_connections.<a href="src/monite/e_invoicing_connections/client.py">post_einvoicing_connections_id_network_credentials</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.e_invoicing_connections.post_einvoicing_connections_id_network_credentials(
    einvoicing_connection_id="einvoicing_connection_id",
    network_credentials_identifier="12345678",
    network_credentials_schema="DE:VAT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**einvoicing_connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**network_credentials_identifier:** `str` — Network participant identifier
    
</dd>
</dl>

<dl>
<dd>

**network_credentials_schema:** `EinvoiceSchemaTypeEnum` — Network scheme identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities
<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all entities.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EntityCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[EntityTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**id_not_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**email_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**email_not_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[EntityStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new entity from the specified values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import EntityAddressSchema, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.create(
    address=EntityAddressSchema(
        city="city",
        country="AF",
        line1="line1",
        postal_code="postal_code",
    ),
    email="email",
    type="individual",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `EntityAddressSchema` — An address description of the entity
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — An official email address of the entity
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityTypeEnum` — A type for an entity
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[IndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get_entities_me</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated. Use `GET /entity_users/my_entity` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get_entities_me()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">patch_entities_me</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated. Use `PATCH /entity_users/my_entity` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.patch_entities_me()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `typing.Optional[UpdateEntityAddressSchema]` — An address description of the entity
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An official email address of the entity
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[OptionalIndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OptionalOrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns entity information for the specified entity ID.

This endpoint requires a partner access token and can be used to get any of the partner's entities.

To get entity information by using an entity user token, use [`GET /entity_users/my_entity`](https://docs.monite.com/api/entities/get-entity-users-my-entity) instead.

Related endpoints:

 * [Get entity settings](https://docs.monite.com/api/entities/get-entities-id-settings)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get_by_id(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity information for the specified entity ID.

This endpoint requires a partner access token and can be used to update any of the partner's entities.

To update an entity by using an entity user token, use [`PATCH /entity_users/my_entity`](https://docs.monite.com/api/entities/patch-entity-users-my-entity) instead.

Related endpoints:

 * [Update entity settings](https://docs.monite.com/api/entities/patch-entities-id-settings)
 * [Update entity logo](https://docs.monite.com/api/entities/put-entities-id-logo)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.update_by_id(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[UpdateEntityAddressSchema]` — An address description of the entity
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An official email address of the entity
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[OptionalIndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OptionalOrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">post_entities_id_activate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Activate an entity to allow it to perform any operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.post_entities_id_activate(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">post_entities_id_deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate an entity to stop it from performing any operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.post_entities_id_deactivate(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">upload_logo_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Entity logo can be PNG, JPG, or GIF, up to 10 MB in size. The logo is used, for example, in PDF documents created by this entity.

Both partner tokens and entity user tokens can be used for authentication. Entity users must have a role with the `entity.update` permission.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.upload_logo_by_id(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">delete_logo_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Both partner tokens and entity user tokens can be used for authentication. Entity users must have a role with the `entity.update` permission.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.delete_logo_by_id(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get_partner_metadata_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a metadata object associated with this entity, usually in a JSON format.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get_partner_metadata_by_id(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">update_partner_metadata_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fully replace the current metadata object with the specified instance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.update_partner_metadata_by_id(
    entity_id="entity_id",
    metadata={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Dict[str, typing.Optional[typing.Any]]` — Metadata for partner needs
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get_settings_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Entity settings include configuration options for accounts payable, accounts receivable, accounting integration, and other functionality.

Both partner tokens and entity user tokens can be used for authentication. Entity users must have a role with the `entity.read` permission.

Related endpoints:

 * [Get next document numbers](https://docs.monite.com/api/entities/get-entities-id-settings-next-document-numbers)
 * [Get partner settings](https://docs.monite.com/api/partner-settings/get-settings)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get_settings_by_id(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">update_settings_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Entity settings include configuration options for accounts payable, accounts receivable, accounting integration, and other functionality.

Both partner tokens and entity user tokens can be used for authentication. Entity users must have a role with the `entity.update` permission.

Related endpoints:

 * [Update an entity](https://docs.monite.com/api/entities/patch-entities-id)
 * [Update entity logo](https://docs.monite.com/api/entities/put-entities-id-logo)
 * [Update partner settings](https://docs.monite.com/api/partner-settings/patch-settings)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.update_settings_by_id(
    entity_id="ea837e28-509b-4b6a-a600-d54b6aa0b1f5",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — A unique ID to specify the entity.
    
</dd>
</dl>

<dl>
<dd>

**accounting:** `typing.Optional[AccountingSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**allow_purchase_order_autolinking:** `typing.Optional[bool]` — Automatically attempt to find a corresponding purchase order for all incoming payables.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencySettingsInput]` 
    
</dd>
</dl>

<dl>
<dd>

**document_ids:** `typing.Optional[DocumentIDsSettingsRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**document_rendering:** `typing.Optional[DocumentRenderingSettingsInput]` — Settings for rendering documents in PDF format.
    
</dd>
</dl>

<dl>
<dd>

**generate_paid_invoice_pdf:** `typing.Optional[bool]` 

This setting affects how PDF is generated for accounts receivable invoices that are paid, partially paid, or have credit notes applied.
If this setting is `true`:

 * The totals block in the PDF invoice will include a list of all payments made and credit notes issued.
 * Once an invoice becomes fully paid, the payment link and QR code are removed.

The PDF invoice gets regenerated at the moment when an invoice payment is recorded or a credit note is issued.  This PDF is not issued as a separate document, and the original PDF invoice is no longer available.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[LanguageCodeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**payables_ocr_auto_tagging:** `typing.Optional[typing.Sequence[OcrAutoTaggingSettingsRequest]]` — Auto tagging settings for all incoming OCR payable documents.
    
</dd>
</dl>

<dl>
<dd>

**payables_skip_approval_flow:** `typing.Optional[bool]` — If enabled, the approval policy will be skipped and the payable will be moved to `waiting_to_be_paid` status.
    
</dd>
</dl>

<dl>
<dd>

**payment_priority:** `typing.Optional[PaymentPriorityEnum]` — Payment preferences for entity to automate calculating suggested payment date based on payment terms and entity preferences.
    
</dd>
</dl>

<dl>
<dd>

**quote_signature_required:** `typing.Optional[bool]` — Sets the default behavior of whether a signature is required to accept quotes.
    
</dd>
</dl>

<dl>
<dd>

**receivable_edit_flow:** `typing.Optional[ReceivableEditFlow]` 

[Invoice compliance mode](https://docs.monite.com/accounts-receivable/regulatory-compliance/invoice-compliance) for accounts receivable. Possible values:

 * `compliant` - invoices cannot be edited once issued.
 * `non_compliant` - issued invoices can still be edited.
 * `partially_compliant` - deprecated mode, should not be used.
    
</dd>
</dl>

<dl>
<dd>

**reminder:** `typing.Optional[RemindersSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**vat_inclusive_discount_mode:** `typing.Optional[VatModeEnum]` — Defines whether the amount discounts (for percentage discounts it does not matter) on VAT inclusive invoices will be applied on amounts including VAT or excluding VAT.
    
</dd>
</dl>

<dl>
<dd>

**vat_mode:** `typing.Optional[VatModeEnum]` — Defines whether the prices of products in receivables will already include VAT or not.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get_entities_id_settings_next_document_numbers</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the next sequence number for various document types - invoices, quotes, credit notes, and others. For example, if the last issued invoice is `INV-00042`, the next invoice number is 43.

To set the next document numbers, use `PATCH /entities/{entity_id}/settings`.

For more information, see [Document number customization](https://docs.monite.com/advanced/document-number-customization).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get_entities_id_settings_next_document_numbers(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — Unique ID of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">upload_onboarding_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide files for entity onboarding verification
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.upload_onboarding_documents()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**additional_verification_document_back:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_verification_document_front:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**bank_account_ownership_verification:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_license:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_memorandum_of_association:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_ministerial_decree:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_registration_verification:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**company_tax_id_verification:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**proof_of_registration:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_document_back:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_document_front:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/monite/entities/client.py">get_onboarding_requirements</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get onboarding requirements for the entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.get_onboarding_requirements()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity users
<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all entity users.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EntityUserCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**id_not_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**role_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**login:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_istartswith:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new entity user from the specified values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.create(
    first_name="Casey",
    login="login",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**first_name:** `str` — The user's first name.
    
</dd>
</dl>

<dl>
<dd>

**login:** `str` 

The username assigned to this user. Usernames must be unique within the entity.

The `login` value is not used by Monite but may be used by partner applications, for example, to map the users between the partner's platform and Monite.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The user's business email address.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The user's last name.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The user's phone number.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` — ID of the role to assign to this user. The role defines the user's [access permissions](https://docs.monite.com/api/concepts/authentication#permissions) within the entity. Each user has just one role.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The user's job title.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">get_current</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The user ID is inferred fron the `Authorization` header, which must contain a user-level access token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.get_current()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">update_current</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The user ID is inferred fron the `Authorization` header, which must contain a user-level access token.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.update_current()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `typing.Optional[str]` — The user's business email address.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The user's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The user's last name.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The user's phone number.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The user's job title.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">get_current_entity</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the entity to which the authenticated user belongs. This endpoint requires an [entity user access token](https://docs.monite.com/api/concepts/authentication#entity-user-token). The user must have a role with the `entity.read` permission.

To get an entity by using a partner access token, use [`GET /entities/{entity_id}`](https://docs.monite.com/api/entities/get-entities-id) instead.

Related endpoints:

 * [Get entity settings](https://docs.monite.com/api/entities/get-entities-id-settings)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.get_current_entity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">update_current_entity</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the entity to which the authenticated user belongs.

This endpoint requires an [entity user access token](https://docs.monite.com/api/concepts/authentication#entity-user-token). The user must have a role with the `entity.update` permission.

This endpoint does not use the `X-Monite-Entity-Id` header. The entity ID is inferred from the access token.

Related endpoints:

 * [Update entity settings](https://docs.monite.com/api/entities/patch-entities-id-settings)
 * [Update entity logo](https://docs.monite.com/api/entities/put-entities-id-logo)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.update_current_entity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address:** `typing.Optional[UpdateEntityAddressSchema]` — An address description of the entity
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An official email address of the entity
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[OptionalIndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OptionalOrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">get_current_role</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information of a role assigned to this entity user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.get_current_role()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an entity user by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.get_by_id(
    entity_user_id="entity_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.delete_by_id(
    entity_user_id="entity_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_users.<a href="src/monite/entity_users/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the specified fields with provided values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entity_users.update_by_id(
    entity_user_id="entity_user_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_user_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The user's business email address.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The user's first name.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The user's last name.
    
</dd>
</dl>

<dl>
<dd>

**login:** `typing.Optional[str]` — The new username for this user. Must be unique within the entity.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The user's phone number.
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` — ID of the new role to assign to this user. The new role takes effect immediately, existing access tokens of this user are not invalidated.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The user's job title.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Events
<details><summary><code>client.events.<a href="src/monite/events/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all webhook events that were triggered for the specified entity based on your enabled webhook subscriptions. These are the same events that were sent to your configured webhook listener endpoints, aggregated into a single list. Results can be filtered by the related object type or time period.

You can use this to get the missed events for the time periods when your webhook listener was temporarily unavailable.

We guarantee access to event data only from the last three months. Earlier events may be unavailable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.events.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EventCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[WebhookObjectType]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.events.<a href="src/monite/events/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a webhook event by its ID. The data is the same as you might have previously received in a webhook sent by Monite to your server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.events.get_by_id(
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` — ID of the webhook event. This is the `id` value you might have received in a webhook or retrieved from `GET /events`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/monite/files/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The `/files` endpoint provides access to an entity's files hosted on Monite's servers. This includes both files uploaded by the entity and files that were automatically created by Monite (such as PDF versions of invoices).

`GET /files` requires at least one query parameter, either `id__in` or `file_type`. You can use this operation to:

 * Bulk fetch multiple files by IDs.
 * Get all files with the given purpose (for example, invoice attachments).

If no files matching the query parameters were found, the response contains an empty `data` array.

Both partner tokens and entity user tokens can be used for authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.files.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only files with specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value: `id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `typing.Optional[AllowedFileTypes]` 

Return only files with the given purpose. Possible values:

 * `additional_identity_documents` and `identity_documents` - [entity verification documents](https://docs.monite.com/payments/onboarding/via-api/documents) uploaded for payments onboarding.
 * `attachments` - supplementary attachments for accounts receivable invoices, quotes, and credit notes.
 * `delivery_notes` - auto-generated PDF versions of delivery notes.
 * `einvoices_xml` - e-invoice XML generated when sending e-invoices.
 * `payables` - payables (bills) received via email or uploaded via API.
 * `receivable_signatures` - images of customer signatures provided during quote acceptance.
 * `receivables` - auto-generated PDF versions of invoices, quotes, and credit notes.
 * `zip` - data export archives created by `POST /data_exports`.

Other values are unused.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/monite/files/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload files for use as:

 * supplementary attachments for invoices, quotes, and credit notes,
 * [entity verification documents](https://docs.monite.com/payments/onboarding/via-api/documents) for payments onboarding.

Maximum file size is 15 MB. Each uploaded file is assigned a unique `id` that you can use to reference this file elsewhere.

Both partner tokens and entity user tokens can be used for authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.files.upload(
    file_type="ocr_results",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `AllowedFileTypes` 

The intended purpose of the file. Possible values:

 * `attachments` - supplemental attachments for accounts receivable invoices, quotes, and credit notes.
 * `identity_documents` - company registration documents or a person's identity documents for payments onboarding.
 * `additional_identity_documents` - documents that verify a person's address.

Other enum values are not supposed to be used directly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/monite/files/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of an existing file. To bulk fetch multiple files by their IDs, use `GET /files?id__in=<ID1>&id__in=<ID2>`.

Both partner tokens and entity user tokens can be used for authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.files.get_by_id(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/monite/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a file with the specified ID.

**Note:** This endpoint does not check if the specified file is in use. Use with caution.

Both partner tokens and entity user tokens can be used for authentication.
#### Considerations for invoice attachments
Deleting a file does not delete it from the `attachments` list of accounts receivable invoices, quotes, and credit notes because these documents contain an inline copy of all referenced resources. To delete a file from attachments, call `PATCH /receivables/{receivable_id}` and update the `attachments` list to exclude the deleted file.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.files.delete(
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_id:** `str` — ID of the file you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Financing
<details><summary><code>client.financing.<a href="src/monite/financing/client.py">get_financing_invoices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of invoices requested for financing
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.financing.get_financing_invoices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[FinancingInvoiceCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[str]` — ID of a payable or receivable invoice. 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of invoice IDs. 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[WcInvoiceStatus]` — Status of the invoice. 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[typing.Union[WcInvoiceStatus, typing.Sequence[WcInvoiceStatus]]]` — List of invoice statuses. 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[FinancingInvoiceType]` — Type of the invoice. payable or receivable. 
    
</dd>
</dl>

<dl>
<dd>

**type_in:** `typing.Optional[
    typing.Union[FinancingInvoiceType, typing.Sequence[FinancingInvoiceType]]
]` — List of invoice types. 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Document ID of the invoice. 
    
</dd>
</dl>

<dl>
<dd>

**document_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of document IDs. 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gt:** `typing.Optional[dt.datetime]` — Issue date greater than. 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lt:** `typing.Optional[dt.datetime]` — Issue date less than. 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gte:** `typing.Optional[dt.datetime]` — Issue date greater than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lte:** `typing.Optional[dt.datetime]` — Issue date less than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[dt.datetime]` — Due date greater than. 
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[dt.datetime]` — Due date less than. 
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[dt.datetime]` — Due date greater than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[dt.datetime]` — Due date less than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Created date greater than. 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Created date less than. 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Created date greater than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Created date less than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Total amount of the invoice in minor units. 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` — Total amount greater than. 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` — Total amount less than. 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` — Total amount greater than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` — Total amount less than or equal. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.financing.<a href="src/monite/financing/client.py">post_financing_invoices</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a session token and a connect token to open Kanmon SDK for confirming invoice details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import FinancingPushInvoicesRequestInvoice, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.financing.post_financing_invoices(
    invoices=[
        FinancingPushInvoicesRequestInvoice(
            id="id",
            type="payable",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoices:** `typing.Sequence[FinancingPushInvoicesRequestInvoice]` — A list of invoices to request financing for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.financing.<a href="src/monite/financing/client.py">get_financing_offers</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of financing offers and the business's onboarding status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.financing.get_financing_offers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.financing.<a href="src/monite/financing/client.py">post_financing_tokens</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a token for Kanmon SDK. Creates a business and user on Kanmon if not already exist.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.financing.post_financing_tokens()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mail templates
<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all custom templates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max is 100
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` — A token, obtained from previous page. Prior over other filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CustomTemplatesCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DocumentObjectTypeRequestEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**type_in:** `typing.Optional[
    typing.Union[
        DocumentObjectTypeRequestEnum,
        typing.Sequence[DocumentObjectTypeRequestEnum],
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**type_not_in:** `typing.Optional[
    typing.Union[
        DocumentObjectTypeRequestEnum,
        typing.Sequence[DocumentObjectTypeRequestEnum],
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.create(
    body_template="body_template",
    name="name",
    subject_template="subject_template",
    type="receivables_quote",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body_template:** `str` — Jinja2 compatible string with email body
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Custom template name
    
</dd>
</dl>

<dl>
<dd>

**subject_template:** `str` — Jinja2 compatible string with email subject
    
</dd>
</dl>

<dl>
<dd>

**type:** `DocumentObjectTypeRequestEnum` — Document type of content
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` — Is default template
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[LanguageCodeEnum]` — Lowercase ISO code of language
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">preview</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Preview rendered template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.preview(
    body="body",
    document_type="receivables_quote",
    language_code="ab",
    subject="subject",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**body:** `str` — Body text of the template
    
</dd>
</dl>

<dl>
<dd>

**document_type:** `DocumentObjectTypeRequestEnum` — Document type of content
    
</dd>
</dl>

<dl>
<dd>

**language_code:** `LanguageCodeEnum` — Lowercase ISO code of language
    
</dd>
</dl>

<dl>
<dd>

**subject:** `str` — Subject text of the template
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">get_system</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all system templates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.get_system()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get custom template by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.get_by_id(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete custom template bt ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.delete_by_id(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update custom template by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.update_by_id(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body_template:** `typing.Optional[str]` — Jinja2 compatible string with email body
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[LanguageCodeEnum]` — Lowercase ISO code of language
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Custom template name
    
</dd>
</dl>

<dl>
<dd>

**subject_template:** `typing.Optional[str]` — Jinja2 compatible string with email subject
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mail_templates.<a href="src/monite/mail_templates/client.py">make_default_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make template default
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mail_templates.make_default_by_id(
    template_id="template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mailbox domains
<details><summary><code>client.mailbox_domains.<a href="src/monite/mailbox_domains/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all domains owned by partner_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailbox_domains.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mailbox_domains.<a href="src/monite/mailbox_domains/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create domain for the partner_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailbox_domains.create(
    domain="domain",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain:** `str` — The domain name, such as `mail.mycompany.com`. Can contain only alphanumeric characters (A..Z a..z 0..9), dots (.), and hyphens (-). Each segment of the domain name must start and end with either a letter or a digit.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mailbox_domains.<a href="src/monite/mailbox_domains/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete domain for the partner_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailbox_domains.delete_by_id(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mailbox_domains.<a href="src/monite/mailbox_domains/client.py">verify_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Verify domain for the partner_id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailbox_domains.verify_by_id(
    domain_id="domain_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**domain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mailboxes
<details><summary><code>client.mailboxes.<a href="src/monite/mailboxes/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all mailboxes owned by Entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailboxes.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mailboxes.<a href="src/monite/mailboxes/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new mailbox
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailboxes.create(
    mailbox_domain_id="mailbox_domain_id",
    mailbox_name="mailbox_name",
    related_object_type="payable",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mailbox_domain_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mailbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**related_object_type:** `MailboxObjectTypeEnum` — Related object type: payable and so on
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mailboxes.<a href="src/monite/mailboxes/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all mailboxes owned by Entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailboxes.search(
    entity_ids=["entity_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mailboxes.<a href="src/monite/mailboxes/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete mailbox
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.mailboxes.delete_by_id(
    mailbox_id="mailbox_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mailbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Measure units
<details><summary><code>client.measure_units.<a href="src/monite/measure_units/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.measure_units.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.measure_units.<a href="src/monite/measure_units/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.measure_units.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.measure_units.<a href="src/monite/measure_units/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.measure_units.get_by_id(
    unit_id="unit_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.measure_units.<a href="src/monite/measure_units/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.measure_units.delete_by_id(
    unit_id="unit_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.measure_units.<a href="src/monite/measure_units/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.measure_units.update_by_id(
    unit_id="unit_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**unit_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OCR
<details><summary><code>client.ocr.<a href="src/monite/ocr/client.py">get_ocr_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.ocr.get_ocr_tasks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only ocr tasks created after the specified date and time. The value must be in the ISO 8601 format YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm].
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only ocr tasks created in Monite before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only ocr tasks created on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only ocr tasks created before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[OcrTaskStatus]` — Return only ocr tasks that have the specified status.
    
</dd>
</dl>

<dl>
<dd>

**document_type:** `typing.Optional[OcrDocumentTypeEnum]` — Return only OCR tasks related to documents of a specific type.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only ocr tasks with specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value: `id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ocr.<a href="src/monite/ocr/client.py">post_ocr_tasks</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.ocr.post_ocr_tasks(
    file_url="file_url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**document_type:** `typing.Optional[OcrDocumentTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ocr.<a href="src/monite/ocr/client.py">post_ocr_tasks_upload_from_file</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.ocr.post_ocr_tasks_upload_from_file()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**document_type:** `typing.Optional[OcrDocumentTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ocr.<a href="src/monite/ocr/client.py">get_ocr_tasks_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.ocr.get_ocr_tasks_id(
    task_id="task_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**task_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Overdue reminders
<details><summary><code>client.overdue_reminders.<a href="src/monite/overdue_reminders/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.overdue_reminders.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.overdue_reminders.<a href="src/monite/overdue_reminders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.overdue_reminders.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[typing.Sequence[OverdueReminderTerm]]` — Overdue reminder terms to send for payment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.overdue_reminders.<a href="src/monite/overdue_reminders/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.overdue_reminders.get_by_id(
    overdue_reminder_id="overdue_reminder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**overdue_reminder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.overdue_reminders.<a href="src/monite/overdue_reminders/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.overdue_reminders.delete_by_id(
    overdue_reminder_id="overdue_reminder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**overdue_reminder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.overdue_reminders.<a href="src/monite/overdue_reminders/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.overdue_reminders.update_by_id(
    overdue_reminder_id="overdue_reminder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**overdue_reminder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` 
    
</dd>
</dl>

<dl>
<dd>

**terms:** `typing.Optional[typing.Sequence[OverdueReminderTerm]]` — Overdue reminder terms to send for payment
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credit notes
<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">get_payable_credit_notes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.get_payable_credit_notes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CreditNoteCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**has_file:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PayableCreditNoteStateEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**status_not_in:** `typing.Optional[
    typing.Union[
        PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[OriginEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes(
    document_id="CN-2287",
    issued_at="2024-01-15",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_id:** `str` — A unique credit note number assigned by the credit note issuer for tracking purposes
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `str` — The date when the credit note was issued, in the YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` — ID of the payable this credit note is based on. The credit note will be linked to this payable
    
</dd>
</dl>

<dl>
<dd>

**based_on_document_id:** `typing.Optional[str]` — The document ID of the original payable that this credit note refers to
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — The ID of the counterpart's address
    
</dd>
</dl>

<dl>
<dd>

**counterpart_bank_account_id:** `typing.Optional[str]` — The ID of the counterpart's bank account
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — The ID of the counterpart (vendor/supplier)
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` — The ID of the counterpart's VAT registration
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — The currency code of the credit note
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — An arbitrary description of this credit note
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The ID of the project this credit note belongs to
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — The email address from which the credit note was received
    
</dd>
</dl>

<dl>
<dd>

**subtotal:** `typing.Optional[int]` — The subtotal amount before taxes
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — List of tag IDs associated with this credit note
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — The tax percentage applied to the subtotal
    
</dd>
</dl>

<dl>
<dd>

**tax_amount:** `typing.Optional[int]` — The calculated tax amount
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — The total amount including taxes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_upload_from_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload an incoming credit note (payable) in PDF, PNG, or JPEG format and scan its contents. The maximum file size is 20MB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_upload_from_file()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">get_payable_credit_notes_validations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get credit notes validations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.get_payable_credit_notes_validations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">put_payable_credit_notes_validations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update credit notes validations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.put_payable_credit_notes_validations(
    required_fields=["currency"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**required_fields:** `typing.Sequence[CreditNoteFieldsAllowedForValidate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_validations_reset</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset credit notes validations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_validations_reset()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">get_payable_credit_notes_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.get_payable_credit_notes_id(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">delete_payable_credit_notes_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.delete_payable_credit_notes_id(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">patch_payable_credit_notes_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.patch_payable_credit_notes_id(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` — ID of the payable this credit note is based on. The credit note will be linked to this payable
    
</dd>
</dl>

<dl>
<dd>

**based_on_document_id:** `typing.Optional[str]` — The document ID of the original payable
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — ID of the counterpart's address
    
</dd>
</dl>

<dl>
<dd>

**counterpart_bank_account_id:** `typing.Optional[str]` — ID of the counterpart's bank account
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — ID of the counterpart
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` — ID of the counterpart's VAT registration
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — The currency code of the credit note
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — An arbitrary description of this credit note
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — A unique credit note number assigned by the credit note issuer for tracking purposes
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` — The date when the credit note was issued, in the YYYY-MM-DD format
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The ID of the project this credit note belongs to
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — Email address of the sender
    
</dd>
</dl>

<dl>
<dd>

**subtotal:** `typing.Optional[int]` — The subtotal amount before taxes
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — List of tag IDs associated with this credit note
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — The tax percentage applied to the subtotal
    
</dd>
</dl>

<dl>
<dd>

**tax_amount:** `typing.Optional[int]` — The calculated tax amount
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — The total amount including taxes
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_id_approve</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Approve the credit note for appliance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_id_approve(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_id_cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel the credit note that was not confirmed during the review.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_id_cancel(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_id_cancel_ocr</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request to cancel the OCR processing of the specified credit note.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_id_cancel_ocr(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">get_payable_credit_notes_id_line_items</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.get_payable_credit_notes_id_line_items(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[CreditNoteLineItemCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**total_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**subtotal_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**unit_price_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**unit_price_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**unit_price_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**unit_price_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**quantity_gt:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**quantity_lt:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**quantity_gte:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**quantity_lte:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**tax_amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**unit_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_id_line_items</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_id_line_items(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Detailed description of the line item
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name or title of the line item
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[float]` — Quantity of items
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — VAT rate in percent [minor units](https://docs.monite.com/references/currencies#minor-units). Example: 12.5% is 1250.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` — Unit of measurement
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[int]` — Price per unit in smallest currency unit (e.g. cents)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">put_payable_credit_notes_id_line_items</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import CreditNoteLineItemCreateRequest, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.put_payable_credit_notes_id_line_items(
    credit_note_id="credit_note_id",
    data=[CreditNoteLineItemCreateRequest()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[CreditNoteLineItemCreateRequest]` — List of credit note line items to replace existing ones
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">get_payable_credit_notes_id_line_items_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.get_payable_credit_notes_id_line_items_id(
    credit_note_id="credit_note_id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">delete_payable_credit_notes_id_line_items_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.delete_payable_credit_notes_id_line_items_id(
    credit_note_id="credit_note_id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">patch_payable_credit_notes_id_line_items_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.patch_payable_credit_notes_id_line_items_id(
    credit_note_id="credit_note_id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Detailed description of the line item
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name or title of the line item
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[float]` — Quantity of items
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — VAT rate in percent [minor units](https://docs.monite.com/references/currencies#minor-units). Example: 12.5% is 1250.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` — Unit of measurement
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[int]` — Price per unit in smallest currency unit
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_id_reject</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Decline the credit note when an approver finds any mismatch or discrepancies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_id_reject(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">post_payable_credit_notes_id_submit_for_approval</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start the approval process once the uploaded credit note is validated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.post_payable_credit_notes_id_submit_for_approval(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credit_notes.<a href="src/monite/credit_notes/client.py">get_payable_credit_notes_id_validate</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.credit_notes.get_payable_credit_notes_id_validate(
    credit_note_id="credit_note_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**credit_note_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Purchase orders
<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PurchaseOrderCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PurchaseOrderStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_in:** `typing.Optional[typing.Union[CurrencyEnum, typing.Sequence[CurrencyEnum]]]` 
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, PurchaseOrderItem

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.create(
    counterpart_id="counterpart_id",
    currency="AED",
    items=[
        PurchaseOrderItem(
            currency="AED",
            name="name",
            price=1,
            quantity=1,
            unit="unit",
            vat_rate=1,
        )
    ],
    message="message",
    valid_for_days=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` — Counterpart unique ID.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — The currency in which the price of the product is set. (all items need to have the same currency)
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Sequence[PurchaseOrderItem]` — List of item to purchase
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` — Msg which will be send to counterpart for who the purchase order is issued.
    
</dd>
</dl>

<dl>
<dd>

**valid_for_days:** `int` — Number of days for which purchase order is valid
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — The ID of counterpart address object stored in counterparts service. If not provided, counterpart's default address is used.
    
</dd>
</dl>

<dl>
<dd>

**entity_vat_id_id:** `typing.Optional[str]` — Entity VAT ID identifier that applied to purchase order
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Project ID of a purchase order
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">get_variables</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of placeholders allowed to insert into an email template for customization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.get_variables()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.get_by_id(
    purchase_order_id="purchase_order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**purchase_order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.delete_by_id(
    purchase_order_id="purchase_order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**purchase_order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.update_by_id(
    purchase_order_id="purchase_order_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**purchase_order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — The ID of counterpart address object stored in counterparts service. If not provided, counterpart's default address is used.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — Counterpart unique ID.
    
</dd>
</dl>

<dl>
<dd>

**entity_vat_id_id:** `typing.Optional[str]` — Entity VAT ID identifier that applied to purchase order
    
</dd>
</dl>

<dl>
<dd>

**items:** `typing.Optional[typing.Sequence[PurchaseOrderItem]]` — List of item to purchase
    
</dd>
</dl>

<dl>
<dd>

**message:** `typing.Optional[str]` — Msg which will be send to counterpart for who the purchase order is issued.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Project ID of a purchase order
    
</dd>
</dl>

<dl>
<dd>

**valid_for_days:** `typing.Optional[int]` — Number of days for which purchase order is valid
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">preview_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.preview_by_id(
    purchase_order_id="purchase_order_id",
    body_text="body_text",
    subject_text="subject_text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**purchase_order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subject_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.purchase_orders.<a href="src/monite/purchase_orders/client.py">send_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.purchase_orders.send_by_id(
    purchase_order_id="purchase_order_id",
    body_text="body_text",
    subject_text="subject_text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**purchase_order_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**subject_text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payables
<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all payables from the connected entity.

If you already have the data of the payable (amount in [minor units](
https://docs.monite.com/references/currencies#minor-units), currency, vendor information, and other details)
stored somewhere as individual attributes, you can create a payable with these attributes by calling [POST
/payables](https://docs.monite.com/api/payables/post-payables) and providing the [base64-encoded](
https://en.wikipedia.org/wiki/Base64) contents of the original invoice file in the field `base64_encoded_file`.

A payable is a financial document given by an entity`s supplier itemizing the purchase of a good or a service and
demanding payment.

The `file_name` field is optional. If omitted, it defaults to “default_file_name”. If the settings are configured
to automatically set `suggested_payment_term`, this object can be omitted from the request body.

The `id` generated for this payable can be used in other API calls to update the data of this payable or trigger [
status transitions](https://docs.monite.com/accounts-payable/approvals/manual-transition), for example. essential data
fields to move from `draft` to `new`

Related guide: [Create a payable from data](https://docs.monite.com/accounts-payable/payables/collect#create-a-payable-from-data)

See also:


[Automatic calculation of due date](https://docs.monite.com/accounts-payable/payables/collect#automatic-calculation-of-due-date)

[Suggested payment date](https://docs.monite.com/accounts-payable/payables/collect#suggested-payment-date)

[Attach file](https://docs.monite.com/accounts-payable/payables/collect#attach-file)

[Collect payables by email](https://docs.monite.com/accounts-payable/payables/collect#send-payables-by-email)

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PayableCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only payables created in Monite after the specified date and time. The value must be in the ISO 8601 format YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm].
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only payables created in Monite before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only payables created in Monite on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only payables created in Monite before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PayableStateEnum]` 

Return only payables that have the specified [status](https://docs.monite.com/accounts-payable/payables/index).

To query multiple statuses at once, use the `status__in` parameter instead.
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]
]` 

Return only payables that have the specified [statuses](https://docs.monite.com/accounts-payable/payables/index).

To specify multiple statuses, repeat this parameter for each value: `status__in=draft&status__in=new`
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only payables with specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value: `id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Return only payables with the exact specified total amount. The amount must be specified in the minor units of currency. For example, $12.5 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — Return only payables with the specified amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_gt:** `typing.Optional[int]` — Return only payables whose amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_lt:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_gte:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_lte:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — Return only payables that use the specified currency.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` 

Return only payables received from counterparts with the specified name (exact match, case-sensitive).

For counterparts of `type = individual`, the full name is formatted as `first_name last_name`.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` — Return only payables received from counterparts whose name contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` — Return only payables received from counterparts whose name contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Apply the `icontains` condition to search for the specified text in the `document_id` and `counterpart_name` fields in the payables.
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — Return payables that are due on the specified date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[str]` — Return payables that are due after the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[str]` — Return payables that are due before the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[str]` — Return payables that are due on or after the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[str]` — Return payables that are due before or on the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` — Return payables that are issued at the specified date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gt:** `typing.Optional[str]` — Return payables that are issued after the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lt:** `typing.Optional[str]` — Return payables that are issued before the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gte:** `typing.Optional[str]` — Return payables that are issued on or after the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lte:** `typing.Optional[str]` — Return payables that are issued before or on the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 

Return a payable with the exact specified document number (case-sensitive).

The `document_id` is the user-facing document number such as INV-00042, not to be confused with Monite resource IDs (`id`).
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` — Return only payables whose document number (`document_id`) contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` — Return only payables whose document number (`document_id`) contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**was_created_by_user_id:** `typing.Optional[str]` — Return only payables created in Monite by the entity user with the specified ID.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 

Return only payables received from the counterpart with the specified ID.

Counterparts that have been deleted but have associated payables will still return results here because the payables contain a frozen copy of the counterpart data.

If the specified counterpart ID does not exist and never existed, no results are returned.
    
</dd>
</dl>

<dl>
<dd>

**source_of_payable_data:** `typing.Optional[SourceOfPayableDataEnum]` — Return only payables coming from the specified source.
    
</dd>
</dl>

<dl>
<dd>

**ocr_status:** `typing.Optional[OcrStatusEnum]` — Return only payables with specific OCR statuses.
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `typing.Optional[str]` — Search for a payable by the identifier of the line item associated with it.
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_id:** `typing.Optional[str]` — Search for a payable by the identifier of the purchase order associated with it.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 

Return only payables assigned to the project with the specified ID.

Valid but nonexistent project IDs do not raise errors but return no results.
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `project_id` include at least one of the project_id with the specified IDs. Valid but nonexistent project IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `tags` include at least one of the tags with the specified IDs. Valid but nonexistent tag IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_not_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `tags` do not include any of the tags with the specified IDs. Valid but nonexistent tag IDs do not raise errors but produce the results.
    
</dd>
</dl>

<dl>
<dd>

**has_tags:** `typing.Optional[bool]` — Filter objects based on whether they have tags. If true, only objects with tags are returned. If false, only objects without tags are returned.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[PayableOriginEnum]` — Return only payables from a given origin ['einvoice', 'upload', 'email']
    
</dd>
</dl>

<dl>
<dd>

**has_file:** `typing.Optional[bool]` — Return only payables with or without attachments (files)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new payable by providing the amount, currency, vendor name, and other details.
You can provide the base64_encoded contents of the original invoice file in the field `base64_encoded_file`.

You can use this endpoint to bypass the Monite OCR service and provide the data directly
(for example, if you already have the data in place).

A newly created payable has the the `draft` [status](https://docs.monite.com/accounts-payable/payables/index).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**base64encoded_file:** `typing.Optional[str]` 

Base64-encoded contents of the original issued payable. The file is provided for reference purposes as the original source of the data.

 Any file formats are allowed. The most common formats are PDF, PNG, JPEG, TIFF.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — The ID of counterpart address object stored in counterparts service
    
</dd>
</dl>

<dl>
<dd>

**counterpart_bank_account_id:** `typing.Optional[str]` — The ID of counterpart bank account object stored in counterparts service
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — The ID of the counterpart object that represents the vendor or supplier.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` — The ID of counterpart VAT ID object stored in counterparts service
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — The [currency code](https://docs.monite.com/references/currencies) of the currency used in the payable.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — An arbitrary description of this payable.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[int]` — The value of the additional discount that will be applied to the total amount. in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — A unique invoice number assigned by the invoice issuer for payment tracking purposes.
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — The date by which the payable must be paid, in the YYYY-MM-DD format. If the payable specifies payment terms with early payment discounts, this is the final payment date.
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` — The original file name.
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` — The date when the payable was issued, in the YYYY-MM-DD format.
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata for partner needs
    
</dd>
</dl>

<dl>
<dd>

**payment_terms:** `typing.Optional[PayablePaymentTermsCreatePayload]` — The number of days to pay with potential discount for options shorter than due_date
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The ID of a project
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_id:** `typing.Optional[str]` — The identifier of the purchase order to which this payable belongs.
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — The email address from which the invoice was sent to the entity.
    
</dd>
</dl>

<dl>
<dd>

**subtotal:** `typing.Optional[int]` — The subtotal amount to be paid, in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**suggested_payment_term:** `typing.Optional[SuggestedPaymentTerm]` — The suggested date and corresponding discount in which payable could be paid. The date is in the YYYY-MM-DD format. The discount is calculated as X * (10^-4) - for example, 100 is 1%, 25 is 0,25%, 10000 is 100 %. Date varies depending on the payment terms and may even be equal to the due date with discount 0.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — A list of IDs of user-defined tags (labels) assigned to this payable. Tags can be used to trigger a specific approval policy for this payable.
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — Registered tax percentage applied for a service price in minor units, e.g. 200 means 2%. 1050 means 10.5%.
    
</dd>
</dl>

<dl>
<dd>

**tax_amount:** `typing.Optional[int]` — Tax amount in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — The total amount to be paid, in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get_analytics</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve aggregated statistics for payables, including total amount and count, both overall and by status.

For more flexible configuration and retrieval of other data types, use `GET /analytics/payables`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get_analytics()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only payables created in Monite after the specified date and time. The value must be in the ISO 8601 format YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm].
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only payables created in Monite before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only payables created in Monite on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only payables created in Monite before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PayableStateEnum]` 

Return only payables that have the specified [status](https://docs.monite.com/accounts-payable/payables/index).

To query multiple statuses at once, use the `status__in` parameter instead.
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]
]` 

Return only payables that have the specified [statuses](https://docs.monite.com/accounts-payable/payables/index).

To specify multiple statuses, repeat this parameter for each value: `status__in=draft&status__in=new`
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only payables with specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value: `id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Return only payables with the exact specified total amount. The amount must be specified in the minor units of currency. For example, $12.5 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` — Return only payables whose total amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — Return only payables with the specified amount.
    
</dd>
</dl>

<dl>
<dd>

**amount_gt:** `typing.Optional[int]` — Return only payables whose amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_lt:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_gte:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**amount_lte:** `typing.Optional[int]` — Return only payables whose amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — Return only payables that use the specified currency.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` 

Return only payables received from counterparts with the specified name (exact match, case-sensitive).

For counterparts of `type = individual`, the full name is formatted as `first_name last_name`.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` — Return only payables received from counterparts whose name contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` — Return only payables received from counterparts whose name contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**search_text:** `typing.Optional[str]` — Apply the `icontains` condition to search for the specified text in the `document_id` and `counterpart_name` fields in the payables.
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — Return payables that are due on the specified date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[str]` — Return payables that are due after the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[str]` — Return payables that are due before the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[str]` — Return payables that are due on or after the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[str]` — Return payables that are due before or on the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` — Return payables that are issued at the specified date (YYYY-MM-DD)
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gt:** `typing.Optional[str]` — Return payables that are issued after the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lt:** `typing.Optional[str]` — Return payables that are issued before the specified date (exclusive, YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_gte:** `typing.Optional[str]` — Return payables that are issued on or after the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**issued_at_lte:** `typing.Optional[str]` — Return payables that are issued before or on the specified date (YYYY-MM-DD).
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 

Return a payable with the exact specified document number (case-sensitive).

The `document_id` is the user-facing document number such as INV-00042, not to be confused with Monite resource IDs (`id`).
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` — Return only payables whose document number (`document_id`) contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` — Return only payables whose document number (`document_id`) contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**was_created_by_user_id:** `typing.Optional[str]` — Return only payables created in Monite by the entity user with the specified ID.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 

Return only payables received from the counterpart with the specified ID.

Counterparts that have been deleted but have associated payables will still return results here because the payables contain a frozen copy of the counterpart data.

If the specified counterpart ID does not exist and never existed, no results are returned.
    
</dd>
</dl>

<dl>
<dd>

**source_of_payable_data:** `typing.Optional[SourceOfPayableDataEnum]` — Return only payables coming from the specified source.
    
</dd>
</dl>

<dl>
<dd>

**ocr_status:** `typing.Optional[OcrStatusEnum]` — Return only payables with specific OCR statuses.
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `typing.Optional[str]` — Search for a payable by the identifier of the line item associated with it.
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_id:** `typing.Optional[str]` — Search for a payable by the identifier of the purchase order associated with it.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` 

Return only payables assigned to the project with the specified ID.

Valid but nonexistent project IDs do not raise errors but return no results.
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `project_id` include at least one of the project_id with the specified IDs. Valid but nonexistent project IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `tags` include at least one of the tags with the specified IDs. Valid but nonexistent tag IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_not_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only payables whose `tags` do not include any of the tags with the specified IDs. Valid but nonexistent tag IDs do not raise errors but produce the results.
    
</dd>
</dl>

<dl>
<dd>

**has_tags:** `typing.Optional[bool]` — Filter objects based on whether they have tags. If true, only objects with tags are returned. If false, only objects without tags are returned.
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[PayableOriginEnum]` — Return only payables from a given origin ['einvoice', 'upload', 'email']
    
</dd>
</dl>

<dl>
<dd>

**has_file:** `typing.Optional[bool]` — Return only payables with or without attachments (files)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">upload_from_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload an incoming invoice (payable) in PDF, PNG, or JPEG format and scan its contents. The maximum file size is 20MB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.upload_from_file()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get_validations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get payable validations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get_validations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">update_validations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update payable validations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.update_validations(
    required_fields=["currency"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**required_fields:** `typing.Sequence[PayablesFieldsAllowedForValidate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">reset_validations</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Reset payable validations to default ones.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.reset_validations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get_variables</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of placeholders that can be used to personalize email templates  related to payables. These include payables attributes such as `currency`,  `customer_name`, `document_id`, `due_date`,  `invoice_id`, `total_amount`, and `uploaded_username`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get_variables()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves information about a specific payable with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specific payable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.delete_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the information about a specific payable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.update_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount_paid:** `typing.Optional[int]` — How much was paid on the invoice (in minor units).
    
</dd>
</dl>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — The ID of counterpart address object stored in counterparts service
    
</dd>
</dl>

<dl>
<dd>

**counterpart_bank_account_id:** `typing.Optional[str]` — The ID of counterpart bank account object stored in counterparts service
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — The ID of the counterpart object that represents the vendor or supplier.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_raw_data:** `typing.Optional[CounterpartRawDataUpdateRequest]` — Allows to fix some data in counterpart recognised fields to correct them in order to make autolinking happen.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` — The ID of counterpart VAT ID object stored in counterparts service
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — The [currency code](https://docs.monite.com/references/currencies) of the currency used in the payable.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — An arbitrary description of this payable.
    
</dd>
</dl>

<dl>
<dd>

**discount:** `typing.Optional[int]` — The value of the additional discount that will be applied to the total amount. in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — A unique invoice number assigned by the invoice issuer for payment tracking purposes.
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` — The date by which the payable must be paid, in the YYYY-MM-DD format. If the payable specifies payment terms with early payment discounts, this is the final payment date.
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[str]` — The date when the payable was issued, in the YYYY-MM-DD format.
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata for partner needs
    
</dd>
</dl>

<dl>
<dd>

**payment_terms:** `typing.Optional[PayablePaymentTermsCreatePayload]` — The number of days to pay with potential discount for options shorter than due_date
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — The project ID of the payable.
    
</dd>
</dl>

<dl>
<dd>

**purchase_order_id:** `typing.Optional[str]` — The identifier of the purchase order to which this payable belongs.
    
</dd>
</dl>

<dl>
<dd>

**sender:** `typing.Optional[str]` — The email address from which the invoice was sent to the entity.
    
</dd>
</dl>

<dl>
<dd>

**subtotal:** `typing.Optional[int]` — The subtotal amount to be paid, in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**suggested_payment_term:** `typing.Optional[SuggestedPaymentTerm]` — The suggested date and corresponding discount in which payable could be paid. The date is in the YYYY-MM-DD format. The discount is calculated as X * (10^-4) - for example, 100 is 1%, 25 is 0,25%, 10000 is 100 %. Date varies depending on the payment terms and may even be equal to the due date with discount 0.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — A list of IDs of user-defined tags (labels) assigned to this payable. Tags can be used to trigger a specific approval policy for this payable.
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — Registered tax percentage applied for a service price in minor units, e.g. 200 means 2%, 1050 means 10.5%.
    
</dd>
</dl>

<dl>
<dd>

**tax_amount:** `typing.Optional[int]` — Tax amount in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — The total amount to be paid, in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">approve_payment_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirms that the payable is ready to be paid.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.approve_payment_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">attach_file_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach file to payable without existing attachment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.attach_file_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">cancel_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels the payable that was not confirmed during the review.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.cancel_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">post_payables_id_cancel_ocr</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Request to cancel the OCR processing of the specified payable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.post_payables_id_cancel_ocr(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get_payables_id_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a chronological list of events related to the specified payable.  This includes changes in status, updates to data, comments, and actions taken  by users or automation rules.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get_payables_id_history(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` — The unique identifier of the payable whose history you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PayableHistoryCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**event_type_in:** `typing.Optional[
    typing.Union[
        PayableHistoryEventTypeEnum,
        typing.Sequence[PayableHistoryEventTypeEnum],
    ]
]` — Return only the specified event types
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only events caused by the entity users with the specified IDs. To specify multiple user IDs, repeat this parameter for each ID:
`entity_user_id__in=<user1>&entity_user_id__in=<user2>`
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gt:** `typing.Optional[dt.datetime]` — Return only events that occurred after the specified date and time. The value must be in the ISO 8601 format `YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm]`.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lt:** `typing.Optional[dt.datetime]` — Return only events that occurred before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gte:** `typing.Optional[dt.datetime]` — Return only events that occurred on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lte:** `typing.Optional[dt.datetime]` — Return only events that occurred before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">mark_as_paid_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a payable as paid.

Payables can be paid using the payment channels offered by Monite or through external payment channels. In the latter
 case, the invoice is not automatically marked as paid in the system and needs to be converted to the paid status
 manually.

Optionally, it is possible to pass the `comment` field in the request body, to describe how and when the invoice was
paid.

Notes:
- To use this endpoint with an entity user token, this entity user must have a role that includes the `pay` permission
for payables.
- The `amount_to_pay` field is automatically calculated based on the `amount_due` less the percentage described
in the `payment_terms.discount` value.

Related guide: [Mark a payable as paid](https://docs.monite.com/accounts-payable/approvals/manual-transition#mark-as-paid)

See also:

[Payables lifecycle](https://docs.monite.com/accounts-payable/payables/index)

[Payables status transitions](https://docs.monite.com/accounts-payable/payables/collect#suggested-payment-date)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.mark_as_paid_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — An arbitrary comment that describes how and when this payable was paid.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">mark_as_partially_paid_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a payable as partially paid.

If the payable is partially paid, its status is moved to `partially_paid`. The value of the `amount_paid` field must be
 the sum of all payments made, not only the last one.

Notes:
- This endpoint can be used for payables in the `waiting_to_be_paid` status.
- The `amount_paid` must be greater than 0 and less than the total payable amount specified by the `amount` field.
- You can use this endpoint multiple times for the same payable to reflect multiple partial payments, always setting the
 sum of all payments made.
- To use this endpoint with an entity user token, this entity user must have a role that includes the `pay`
permission for payables.
- The `amount_to_pay` field is automatically calculated based on the `amount_due` less the percentage described
in the `payment_terms.discount` value.

Related guide: [Mark a payable as partially paid](https://docs.monite.com/accounts-payable/approvals/manual-transition#mark-as-partially-paid)

See also:

[Payables lifecycle](https://docs.monite.com/accounts-payable/payables/index)

[Payables status transitions](https://docs.monite.com/accounts-payable/payables/collect#suggested-payment-date)

[Mark a payable as paid](https://docs.monite.com/accounts-payable/approvals/manual-transition#mark-as-paid)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.mark_as_partially_paid_by_id(
    payable_id="payable_id",
    amount_paid=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount_paid:** `int` — How much was paid on the invoice (in minor units).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">reject_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Declines the payable when an approver finds any mismatch or discrepancies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.reject_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">reopen_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Moves payables in the `rejected` or `waiting_to_be_paid` statuses back to `new`, allowing further actions such as editing, approval, or payment. The 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.reopen_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` — The unique identifier of the payable you want to reopen.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">submit_for_approval_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts the approval process once the uploaded payable is validated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.submit_for_approval_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">get_payables_id_suggestions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the most likely matching counterpart for a given payable, based on an AI-powered analysis of the payable's data.

When a user uploads a payable, Monite automatically compares key fields—such as `name`, `address`, `VAT ID`, and bank `account`—against existing counterparts. If a sufficiently similar match is found, this endpoint will return a suggested counterpart.

If no suitable match is identified, the response will be empty.

**Note:** Suggestions are automatically generated during payable upload. This endpoint simply retrieves the existing suggestion for a specific payable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.get_payables_id_suggestions(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` — The unique identifier of the payable you want to find matching suggestions for.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">delete_payables_id_suggestions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the automatically generated counterpart suggestion for a specific payable.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.delete_payables_id_suggestions(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` — The unique identifier of the payable whose suggestions you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.<a href="src/monite/payables/client.py">validate_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Check the invoice for compliance with the requirements for movement from draft to new status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.validate_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payment intents
<details><summary><code>client.payment_intents.<a href="src/monite/payment_intents/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_intents.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PaymentIntentCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — ID of a payable or receivable invoice. If provided, returns only payment intents associated with the specified invoice.
    
</dd>
</dl>

<dl>
<dd>

**object_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of payable IDs and/or receivable IDs. If provided, returns only payment intents associated with the specified payable and receivable invoices. Valid but nonexistent IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_intents.<a href="src/monite/payment_intents/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_intents.get_by_id(
    payment_intent_id="payment_intent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_intent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_intents.<a href="src/monite/payment_intents/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_intents.update_by_id(
    payment_intent_id="payment_intent_id",
    amount=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_intent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_intents.<a href="src/monite/payment_intents/client.py">get_history_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_intents.get_history_by_id(
    payment_intent_id="payment_intent_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_intent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payment links
<details><summary><code>client.payment_links.<a href="src/monite/payment_links/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new [payment link](https://docs.monite.com/payments/payment-links) for an accounts payble invoice (to be paid by the entity) or an accounts receivable invoice (to be sent to the counterpart).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from monite import Invoice, InvoiceFile, Monite, PaymentAccountObject

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_links.create(
    amount=12500,
    currency="EUR",
    expires_at=datetime.datetime.fromisoformat(
        "2025-08-30 23:59:59+00:00",
    ),
    invoice=Invoice(
        due_date="2025-07-31",
        file=InvoiceFile(
            mimetype="application/pdf",
            name="invoice.pdf",
            url="https://example.com/path/to/invoice.pdf",
        ),
        issue_date="2025-07-01",
    ),
    payment_methods=["card", "eps", "ideal", "sepa_credit", "sepa_debit"],
    payment_reference="INV/2025/0042",
    recipient=PaymentAccountObject(
        id="274b995b-1906-4d8a-b7fe-e8d822d731b0",
        type="entity",
    ),
    return_url="https://example.com/where-to-redirect-after-payment",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_methods:** `typing.Sequence[MoniteAllPaymentMethodsTypes]` 

Payment methods to be displayed on the payment page. These payment methods must already be enabled for the entity.

**Note:** Available payment methods vary per country, transaction type (B2B or B2C), and the payment link type (entity pays a bill or entity generates an invoice payment link for its counterpart). For more information, see [Payment methods](https://docs.monite.com/payments/payment-methods).
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `PaymentAccountObject` — Specifies the invoice vendor - entity or counterpart. This is the payee, or the recipient of the payment.
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` 

The payment amount in [minor units](https://docs.monite.com/references/currencies#minor-units). The usage of the `amount` field depends on the type of the payment link you are creating:

 * If the `invoice` object is specified (that is, when creating a payment link for an external invoice),
  `amount` is required.
 * If `object` is specified:
   * If `object.type` is `payable`, `amount` must not be specified since it's taken from the payable.
   * If `object.type` is `receivable`, you can provide a custom `amount` value to create a partial payment link.
     In this case, the `amount` value must not exceed the invoice's `amount_to_pay` minus all active payment links.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — The payment currency. Mutually exclusive with `object`.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` 

Date and time (in the ISO 8601 format) when this payment link will expire. Can be up to 70 days from the current date and time.
If omitted:

 * Payment links for payables and receivables expire 30 days after the invoice due date.
 * Payment links for external invoices expire 30 days after the link creation time.

For more information, see [Payment link expiration](https://docs.monite.com/payments/payment-links#expiration).
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[Invoice]` — An object containing information about an external invoice to be paid. Mutually exclusive with `object`.
    
</dd>
</dl>

<dl>
<dd>

**object:** `typing.Optional[PaymentObject]` — If the invoice being paid is a payable or receivable stored in Monite, provide the `object` object containing the invoice type and ID. Otherwise, use the `amount`, `currency`, `payment_reference`, and (optionally) `invoice` fields to specify the invoice-related data.
    
</dd>
</dl>

<dl>
<dd>

**payment_reference:** `typing.Optional[str]` — A payment reference number that the recipient can use to identify the payer or purpose of the transaction. Mutually exclusive with `object`.
    
</dd>
</dl>

<dl>
<dd>

**return_url:** `typing.Optional[str]` — The URL where to redirect the payer after the payment. If `return_url` is specified, then after the payment is completed the payment page will display the "Return to platform" link that navigates to this URL.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_links.<a href="src/monite/payment_links/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_links.get_by_id(
    payment_link_id="payment_link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_links.<a href="src/monite/payment_links/client.py">expire_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_links.expire_by_id(
    payment_link_id="payment_link_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_link_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payment records
<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max is 100
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` — A token, obtained from previous page. Prior over other filters
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[PaymentRecordCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**is_external:** `typing.Optional[bool]` — Identifies whether payment is from our rails or external system
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — ID of the object, that is connected to payment
    
</dd>
</dl>

<dl>
<dd>

**object_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — List of IDs of the objects, that are connected to payments
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[ObjectTypeEnum]` — Type of an object, which is connected with payment
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Created after this datetime (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Created before this datetime (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` — Updated after this datetime (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` — Updated before this datetime (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**paid_at_gt:** `typing.Optional[dt.datetime]` — Paid after this datetime (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**paid_at_lt:** `typing.Optional[dt.datetime]` — Paid before this datetime (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date:** `typing.Optional[str]` — Optional date of the upcoming payment (equality)
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date_gt:** `typing.Optional[str]` — Planned after this date (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date_lt:** `typing.Optional[str]` — Planned before this date (exclusive)
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date_gte:** `typing.Optional[str]` — Planned at or after this date (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date_lte:** `typing.Optional[str]` — Planned at or before this date (inclusive)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PaymentRecordStatusEnum]` — One of the payment record statuses
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_status:** `typing.Optional[str]` — Payment intent status as a raw string
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[str]` — Payment method used for the transaction
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, PaymentRecordObjectRequest

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.create(
    amount=1,
    currency="AED",
    object=PaymentRecordObjectRequest(
        id="id",
        type="receivable",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**amount:** `int` — Positive amount in case of successful payment, negative amount in case of payment failure or refund, represented in minor currency units (e.g., cents).
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — Currency code (ISO 4217) indicating the currency in which the payment was made.
    
</dd>
</dl>

<dl>
<dd>

**object:** `PaymentRecordObjectRequest` — Reference object linked to this payment record, indicating the type (receivable or payable) and its identifier.
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` — ID of the user associated with the payment, if applicable.
    
</dd>
</dl>

<dl>
<dd>

**paid_at:** `typing.Optional[dt.datetime]` — Timestamp marking when the payment was executed. Null if payment hasn't occurred yet.
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_id:** `typing.Optional[str]` — Identifier for an payment intent.
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_status:** `typing.Optional[str]` — Raw status string of the external payment intent.
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[str]` — Payment method used or planned for the transaction.
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date:** `typing.Optional[str]` — Scheduled date for future payments, required when the payment is planned but not yet executed.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[PaymentRecordRequestStatus]` — Status of the payment record indicating its current stage (e.g., created, processing, succeeded).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.get_by_id(
    payment_record_id="payment_record_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">patch_payment_records_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.patch_payment_records_id(
    payment_record_id="payment_record_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — Positive amount in case of successful payment, negative amount in case of payment failure or refund, represented in minor currency units (e.g., cents).
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — Currency code (ISO 4217) indicating the currency in which the payment was made.
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` — ID of the user associated with the payment, if applicable.
    
</dd>
</dl>

<dl>
<dd>

**object:** `typing.Optional[PaymentRecordObjectRequest]` — Reference object linked to this payment record, indicating the type (receivable or payable) and its identifier.
    
</dd>
</dl>

<dl>
<dd>

**paid_at:** `typing.Optional[dt.datetime]` — Timestamp marking when the payment was executed. Null if payment hasn't occurred yet.
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_id:** `typing.Optional[str]` — Identifier for an payment intent.
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_status:** `typing.Optional[str]` — Raw status string of the external payment intent.
    
</dd>
</dl>

<dl>
<dd>

**payment_method:** `typing.Optional[str]` — Payment method used or planned for the transaction.
    
</dd>
</dl>

<dl>
<dd>

**planned_payment_date:** `typing.Optional[str]` — Scheduled date for future payments, required when the payment is planned but not yet executed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">post_payment_records_id_cancel</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.post_payment_records_id_cancel(
    payment_record_id="payment_record_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_status:** `typing.Optional[str]` — Raw status string of the external payment intent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">post_payment_records_id_mark_as_succeeded</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.post_payment_records_id_mark_as_succeeded(
    payment_record_id="payment_record_id",
    paid_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**paid_at:** `dt.datetime` — Timestamp marking when the payment was executed.
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_status:** `typing.Optional[str]` — Raw status string of the external payment intent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_records.<a href="src/monite/payment_records/client.py">post_payment_records_id_start_processing</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_records.post_payment_records_id_start_processing(
    payment_record_id="payment_record_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_status:** `typing.Optional[str]` — Raw status string of the external payment intent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payment reminders
<details><summary><code>client.payment_reminders.<a href="src/monite/payment_reminders/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_reminders.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_reminders.<a href="src/monite/payment_reminders/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_reminders.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` 
    
</dd>
</dl>

<dl>
<dd>

**term1reminder:** `typing.Optional[Reminder]` — Reminder to send for first payment term
    
</dd>
</dl>

<dl>
<dd>

**term2reminder:** `typing.Optional[Reminder]` — Reminder to send for second payment term
    
</dd>
</dl>

<dl>
<dd>

**term_final_reminder:** `typing.Optional[Reminder]` — Reminder to send for final payment term
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_reminders.<a href="src/monite/payment_reminders/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_reminders.get_by_id(
    payment_reminder_id="payment_reminder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_reminder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_reminders.<a href="src/monite/payment_reminders/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_reminders.delete_by_id(
    payment_reminder_id="payment_reminder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_reminder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_reminders.<a href="src/monite/payment_reminders/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_reminders.update_by_id(
    payment_reminder_id="payment_reminder_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_reminder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` 
    
</dd>
</dl>

<dl>
<dd>

**term1reminder:** `typing.Optional[Reminder]` — Reminder to send for first payment term
    
</dd>
</dl>

<dl>
<dd>

**term2reminder:** `typing.Optional[Reminder]` — Reminder to send for second payment term
    
</dd>
</dl>

<dl>
<dd>

**term_final_reminder:** `typing.Optional[Reminder]` — Reminder to send for final payment term
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payment terms
<details><summary><code>client.payment_terms.<a href="src/monite/payment_terms/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_terms.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_terms.<a href="src/monite/payment_terms/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, TermDiscountDays, TermFinalDays

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_terms.create(
    description="The invoice must be paid within 30 days. 2% discount if paid within the first 10 days, 1% discount if paid within 20 days.",
    name="2/10, 1/20, Net 30",
    term1=TermDiscountDays(
        discount=200,
        number_of_days=10,
    ),
    term2=TermDiscountDays(
        discount=100,
        number_of_days=20,
    ),
    term_final=TermFinalDays(
        number_of_days=30,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**term_final:** `TermFinalDays` — The final tier of the payment term. Defines the invoice due date.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**term1:** `typing.Optional[TermDiscountDays]` — The first tier of the payment term. Represents the terms of the first early discount.
    
</dd>
</dl>

<dl>
<dd>

**term2:** `typing.Optional[TermDiscountDays]` — The second tier of the payment term. Defines the terms of the second early discount.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_terms.<a href="src/monite/payment_terms/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_terms.get_by_id(
    payment_terms_id="payment_terms_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_terms_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_terms.<a href="src/monite/payment_terms/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_terms.delete_by_id(
    payment_terms_id="payment_terms_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_terms_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payment_terms.<a href="src/monite/payment_terms/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_terms.update_by_id(
    payment_terms_id="payment_terms_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_terms_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**term1:** `typing.Optional[TermDiscountDays]` — The first tier of the payment term. Represents the terms of the first early discount.
    
</dd>
</dl>

<dl>
<dd>

**term2:** `typing.Optional[TermDiscountDays]` — The second tier of the payment term. Defines the terms of the second early discount.
    
</dd>
</dl>

<dl>
<dd>

**term_final:** `typing.Optional[TermFinalDays]` — The final tier of the payment term. Defines the invoice due date.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Products
<details><summary><code>client.products.<a href="src/monite/products/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.products.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ProductCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ProductServiceTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**price_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**price_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**price_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**price_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**currency_in:** `typing.Optional[typing.Union[CurrencyEnum, typing.Sequence[CurrencyEnum]]]` 
    
</dd>
</dl>

<dl>
<dd>

**measure_unit_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/monite/products/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.products.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the product.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the product.
    
</dd>
</dl>

<dl>
<dd>

**external_reference:** `typing.Optional[str]` — A user-defined identifier of the product. For example, an internal product code or SKU (stock keeping unit). Client applications can use this field to map the products in Monite to an external product catalog.
    
</dd>
</dl>

<dl>
<dd>

**ledger_account_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**measure_unit_id:** `typing.Optional[str]` — The unique ID reference of the unit used to measure the quantity of this product (e.g. items, meters, kilograms).
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[Price]` 
    
</dd>
</dl>

<dl>
<dd>

**smallest_amount:** `typing.Optional[float]` — The smallest amount allowed for this product.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ProductServiceTypeEnum]` — Specifies whether this offering is a product or service. This may affect the applicable tax rates.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/monite/products/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.products.get_by_id(
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/monite/products/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.products.delete_by_id(
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.products.<a href="src/monite/products/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.products.update_by_id(
    product_id="product_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**product_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the product.
    
</dd>
</dl>

<dl>
<dd>

**external_reference:** `typing.Optional[str]` — A user-defined identifier of the product. For example, an internal product code or SKU (stock keeping unit). Client applications can use this field to map the products in Monite to an external product catalog.
    
</dd>
</dl>

<dl>
<dd>

**ledger_account_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**measure_unit_id:** `typing.Optional[str]` — The unique ID reference of the unit used to measure the quantity of this product (e.g. items, meters, kilograms).
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the product.
    
</dd>
</dl>

<dl>
<dd>

**price:** `typing.Optional[Price]` 
    
</dd>
</dl>

<dl>
<dd>

**smallest_amount:** `typing.Optional[float]` — The smallest amount allowed for this product.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ProductServiceTypeEnum]` — Specifies whether this offering is a product or service. This may affect the applicable tax rates.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Projects
<details><summary><code>client.projects.<a href="src/monite/projects/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all projects for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.projects.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ProjectCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date_gt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date_lt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date_gte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**start_date_lte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date_gt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date_lt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date_gte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date_lte:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/monite/projects/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.projects.create(
    name="Marketing",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The project name.
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — A user-defined identifier of this project.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Project color as a [CSS-compatible](https://developer.mozilla.org/en-US/docs/Web/CSS/color) value. Client applications can use this to color-code the projects or project-related data.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A user-defined description of the project.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Project end date. If specified, must be later than or equal to the start date.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Unused. Reserved for future use.
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — [Metadata](https://docs.monite.com/common/metadata) for partner needs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Project start date.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — A list of IDs of user-defined tags (labels) assigned to this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/monite/projects/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a project with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.projects.get_by_id(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/monite/projects/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.projects.delete_by_id(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.projects.<a href="src/monite/projects/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a project.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.projects.update_by_id(
    project_id="project_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**code:** `typing.Optional[str]` — A user-defined identifier of this project.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Project color as a [CSS-compatible](https://developer.mozilla.org/en-US/docs/Web/CSS/color) value. Client applications can use this to color-code the projects or project-related data.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A user-defined description of the project.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Project end date. If specified, must be later than or equal to the start date.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The project name.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Unused. Reserved for future use.
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — [Metadata](https://docs.monite.com/common/metadata) for partner needs.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Project start date.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` — A list of IDs of user-defined tags (labels) assigned to this project.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Receipts
<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">get_receipts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.get_receipts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceiptCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**has_file:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**has_transaction:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">post_receipts</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.post_receipts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**base64encoded_file:** `typing.Optional[str]` — Base64-encoded contents of the original receipt file.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — Currency code used in the receipt.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Unique receipt number assigned by the issuer.
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[dt.datetime]` — Receipt issued date and time.
    
</dd>
</dl>

<dl>
<dd>

**merchant_location:** `typing.Optional[str]` — Location of the merchant.
    
</dd>
</dl>

<dl>
<dd>

**merchant_name:** `typing.Optional[str]` — Name of the merchant.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Total amount for the receipt in minor units (e.g. cents).
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Transaction ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">post_receipts_upload_from_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload an incoming receipt in PDF, PNG, or JPEG format and scan its contents. The maximum file size is 20MB.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.post_receipts_upload_from_file()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">get_receipts_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.get_receipts_id(
    receipt_id="receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">delete_receipts_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.delete_receipts_id(
    receipt_id="receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">patch_receipts_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.patch_receipts_id(
    receipt_id="receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**base64encoded_file:** `typing.Optional[str]` — Base64-encoded file contents.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — Currency code.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Receipt number.
    
</dd>
</dl>

<dl>
<dd>

**issued_at:** `typing.Optional[dt.datetime]` — Date when the receipt was issued.
    
</dd>
</dl>

<dl>
<dd>

**merchant_location:** `typing.Optional[str]` — Merchant location.
    
</dd>
</dl>

<dl>
<dd>

**merchant_name:** `typing.Optional[str]` — Merchant name.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Total amount.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Transaction ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">post_receipts_id_attach_file</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach file to receipt without existing attachment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.post_receipts_id_attach_file(
    receipt_id="receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">get_receipts_id_line_items</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.get_receipts_id_line_items(
    receipt_id="receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceiptLineItemCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_iexact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_icontains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**total_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**total_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">post_receipts_id_line_items</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.post_receipts_id_line_items(
    receipt_id="receipt_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accounting_tax_rate_id:** `typing.Optional[str]` — Accounting tax rate ID.
    
</dd>
</dl>

<dl>
<dd>

**cost_center_id:** `typing.Optional[str]` — Cost center ID.
    
</dd>
</dl>

<dl>
<dd>

**general_ledger_id:** `typing.Optional[str]` — General ledger ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Line item name/description.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[int]` — Line item total in minor units.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">delete_receipts_id_line_items_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.delete_receipts_id_line_items_id(
    receipt_id="receipt_id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receipts.<a href="src/monite/receipts/client.py">patch_receipts_id_line_items_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receipts.patch_receipts_id_line_items_id(
    receipt_id="receipt_id",
    line_item_id="line_item_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receipt_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accounting_tax_rate_id:** `typing.Optional[str]` — Accounting tax rate ID.
    
</dd>
</dl>

<dl>
<dd>

**cost_center_id:** `typing.Optional[str]` — Cost center ID.
    
</dd>
</dl>

<dl>
<dd>

**general_ledger_id:** `typing.Optional[str]` — General ledger ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Line item name/description.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[int]` — Line item total in minor units.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Receivables
<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of [accounts receivable](https://docs.monite.com/accounts-receivable/index) documents - invoices, quotes, and credit notes - of the specified entity.

Results can be filtered by amount, counterpart, due date, and other criteria. Multiple filters are combined using logical AND unless specified otherwise. If no documents matching the search criteria are found, the endpoint returns a successful response with an empty `data` array.

This endpoint supports [pagination](https://docs.monite.com/api/concepts/pagination-sorting-filtering) and sorting. By default, results are sorted by the creation date in ascending order (from oldest to newest).

#### Examples

##### Invoices

* Get all overdue invoices:
    ```
    GET /receivables?type=invoice&status=overdue
    ```

* Get all invoices created for the counterpart named "Solarwind" (case-insensitive):

    ```
    GET /receivables?type=invoice?counterpart_name__icontains=Solarwind
    ```

* Get invoices whose total amount starts from 500 EUR:

    ```
    GET /receivables?type=invoice&total_amount__gte=50000
    ```

* Get invoices that are due for payment in September 2024:

    ```
    GET /receivables?type=invoice&due_date__gte=2024-09-01T00:00:00Z&due_date__lt=2024-10-01T00:00:00Z
    ```

* Get invoices created on or after September 1, 2024:

    ```
    GET /receivables?type=invoice&created_at__gte=2024-09-01T00:00:00Z
    ```

* Find an invoice created from a specific quote:

    ```
    GET /receivables?type=invoice?based_on=QUOTE_ID
    ```

##### Quotes

* Get the latest created quote:

    ```
    GET /receivables?type=quote&sort=created_at&order=desc&limit=1
    ```

* Get the latest issued quote:

    ```
    GET /receivables?type=quote&sort=issue_date&order=desc&limit=1
    ```

##### Credit notes

* Find all credit notes created for a specific invoice:

    ```
    GET /receivables?type=credit_note?based_on=INVOICE_ID
    ```
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 250) to return in a single page of the response. Default is 100. The response may contain fewer items if it is the last or only page. 

When using pagination with a non-default `limit`, you must provide the `limit` value alongside `pagination_token` in all subsequent pagination requests. Unlike other query parameters, `limit` is not inferred from `pagination_token`.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters except `limit` are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables with the specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.

To specify multiple IDs, repeat this parameter for each value:
`id__in=<id1>&id__in=<id2>`
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        ReceivablesGetRequestStatusInItem,
        typing.Sequence[ReceivablesGetRequestStatusInItem],
    ]
]` 

Return only receivables that have the specified statuses. See the applicable [invoice statuses](https://docs.monite.com/accounts-receivable/invoices/index), [quote statuses](https://docs.monite.com/accounts-receivable/quotes/index), and [credit note statuses](https://docs.monite.com/accounts-receivable/credit-notes#credit-note-lifecycle).

To specify multiple statuses, repeat this parameter for each value:
`status__in=draft&status__in=issued`
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables created by the entity users with the specified IDs.To specify multiple user IDs, repeat this parameter for each ID:
`entity_user_id__in=<user1>&entity_user_id__in=<user2>`

If the request is authenticated using an entity user token, this user must have the `receivable.read.allowed` (rather than `allowed_for_own`) permission to be able to query receivables created by other users.

IDs of deleted users will still produce results here if those users had associated receivables. Valid but nonexistent user IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceivableCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose [tags](https://docs.monite.com/common/tags) include at least one of the tags with the specified IDs.

For example, given receivables with the following tags:
1. tagA
2. tagB
3. tagA, tagB
4. tagC
5. tagB, tagC


`tag_ids__in=<tagA>&tag_ids__in=<tagB>` will return receivables 1, 2, 3, and 5.

Valid but nonexistent tag IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose [tags](https://docs.monite.com/common/tags) include all of the tags with the specified IDs and optionally other tags that are not specified.

For example, given receivables with the following tags:
1. tagA
2. tagB
3. tagA, tagB
4. tagC
5. tagA, tagB, tagC


`tag_ids=<tagA>&tag_ids=<tagB>` will return receivables 3 and 5.
    
</dd>
</dl>

<dl>
<dd>

**product_ids_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose line items include at least one of the product IDs with the specified IDs. 

To specify multiple product IDs, repeat this parameter for each ID:
`product_ids__in=<product1>&product_ids__in=<product2>`

For example, given receivables with the following product IDs:
1. productA
2. productB
3. productA, productB
4. productC
5. productB, productC


`product_ids__in=<productA>&product_ids__in=<productB>` will return receivables 1, 2, 3, and 5.Valid but nonexistent product IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**product_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only receivables whose line items include all of the product IDs with the specified IDs and optionally other products that are not specified. 

To specify multiple product IDs, repeat this parameter for each ID:
`product_ids=<product1>&product_ids=<product2>`

For example, given receivables with the following product IDs:
1. productA
2. productB
3. productA, productB
4. productC
5. productA, productB, productC


`product_ids=<productA>&product_ids=<productB>` will return receivables 3 and 5.
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return only receivables whose `project_id` include at least one of the project_id with the specified IDs. Valid but nonexistent project IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ReceivableType]` — Return only receivables of the specified type. Use this parameter to get only invoices, or only quotes, or only credit notes.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Return a receivable with the exact specified document number (case-sensitive). The `document_id` is the user-facing document number such as INV-00042, not to be confused with Monite resource IDs (`id`).
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` — Return only receivables whose document number (`document_id`) contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` — Return only receivables whose document number (`document_id`) contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gt:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued after the specified date and time. The value must be in the ISO 8601 format `YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm]`.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lt:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gte:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lte:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only receivables created after the specified date and time. The value must be in the ISO 8601 format `YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm]`.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only receivables created before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only receivables created on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only receivables created before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 

Return only receivables created for the counterpart with the specified ID.

Counterparts that have been deleted but have associated receivables will still return results here because the receivables contain a frozen copy of the counterpart data.

If the specified counterpart ID does not exist and never existed, no results are returned.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` — Return only receivables created for counterparts with the specified name (exact match, case-sensitive). For counterparts of `type` = `individual`, the full name is formatted as `first_name last_name`.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` — Return only receivables created for counterparts whose name contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` — Return only receivables created for counterparts whose name contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Return only receivables with the exact specified total amount. The amount must be specified in the [minor units](https://docs.monite.com/references/currencies#minor-units) of currency. For example, $12.5 is represented as 1250."
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal:** `typing.Optional[int]` — Return only receivables with the exact specified discounted subtotal. The amount must be specified in the [minor units](https://docs.monite.com/references/currencies#minor-units) of currency. For example, $12.5 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_gt:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_lt:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_gte:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_lte:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ReceivablesGetRequestStatus]` 

Return only receivables that have the specified status. See the applicable [invoice statuses](https://docs.monite.com/accounts-receivable/invoices/index), [quote statuses](https://docs.monite.com/accounts-receivable/quotes/index), and [credit note statuses](https://docs.monite.com/accounts-receivable/credit-notes#credit-note-lifecycle).

To query multiple statuses at once, use the `status__in` parameter instead.
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` 

Return only receivables created by the entity users with the specified IDs. To specify multiple user IDs, repeat this parameter for each ID:
`entity_user_id__in=<user1>&entity_user_id__in=<user2>`

If the request is authenticated using an entity user token, this user must have the `receivable.read.allowed` (rather than `allowed_for_own`) permission to be able to query receivables created by other users.

IDs of deleted users will still produce results here if those users had associated receivables. Valid but nonexistent user IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**based_on:** `typing.Optional[str]` 

This parameter accepts a quote ID or an invoice ID.

 * Specify a quote ID to find invoices created from this quote.
 * Specify an invoice ID to find credit notes created for this invoice or find recurring invoices created from a base invoice.

Valid but nonexistent IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[str]` 

Return invoices that are due after the specified date (exclusive, `YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[str]` 

Return invoices that are due before the specified date (exclusive, `YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[str]` 

Return invoices that are due on or after the specified date (`YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[str]` 

Return invoices that are due before or on the specified date (`YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Return only receivables assigned to the project with the specified ID. Valid but nonexistent project IDs do not raise errors but return no results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, ReceivableCreateBasedOnPayload

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.create(
    request=ReceivableCreateBasedOnPayload(
        based_on="e977db242-e7d5-4d2e-83cf-a1f5051ed40a",
        type="credit_note",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ReceivableFacadeCreatePayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_receivables_required_fields</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get field requirements for invoice creation given the entity and counterpart details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_receivables_required_fields()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_billing_address_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_country:** `typing.Optional[AllowedCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_type:** `typing.Optional[CounterpartType]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_vat_id_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">post_receivables_search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This is a POST version of the `GET /receivables` endpoint. Use it to send search and filter parameters in the request body instead of the URL query string in case the query is too long and exceeds the URL length limit of your HTTP client.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.post_receivables_search(
    status="draft",
    type="invoice",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**based_on:** `typing.Optional[str]` 

This parameter accepts a quote ID or an invoice ID.

* Specify a quote ID to find invoices created from this quote.
* Specify an invoice ID to find credit notes created for this invoice.

Valid but nonexistent IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 

Return only receivables created for the counterpart with the specified ID.

Counterparts that have been deleted but have associated receivables will still return results here because the receivables contain a frozen copy of the counterpart data.

If the specified counterpart ID does not exist and never existed, no results are returned.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name:** `typing.Optional[str]` — Return only receivables created for counterparts with the specified name (exact match, case-sensitive). For counterparts of `type` = `individual`, the full name is formatted as `first_name last_name`.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_contains:** `typing.Optional[str]` — Return only receivables created for counterparts whose name contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**counterpart_name_icontains:** `typing.Optional[str]` — Return only receivables created for counterparts whose name contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only receivables created after the specified date and time. The value must be in the ISO 8601 format `YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm]`.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only receivables created on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only receivables created before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only receivables created before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal:** `typing.Optional[int]` — Return only receivables with the exact specified discounted subtotal. The amount must be specified in the [minor units](https://docs.monite.com/references/currencies#minor-units) of currency. For example, $12.5 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_gt:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is greater than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_gte:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_lt:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**discounted_subtotal_lte:** `typing.Optional[int]` — Return only receivables whose discounted subtotal (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `typing.Optional[str]` — Return a receivable with the exact specified document number (case-sensitive). The `document_id` is the user-facing document number such as INV-00042, not to be confused with Monite resource IDs (`id`).
    
</dd>
</dl>

<dl>
<dd>

**document_id_contains:** `typing.Optional[str]` — Return only receivables whose document number (`document_id`) contains the specified string (case-sensitive).
    
</dd>
</dl>

<dl>
<dd>

**document_id_icontains:** `typing.Optional[str]` — Return only receivables whose document number (`document_id`) contains the specified string (case-insensitive).
    
</dd>
</dl>

<dl>
<dd>

**due_date_gt:** `typing.Optional[str]` 

Return invoices that are due after the specified date (exclusive, `YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**due_date_gte:** `typing.Optional[str]` 

Return invoices that are due on or after the specified date (`YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**due_date_lt:** `typing.Optional[str]` 

Return invoices that are due before the specified date (exclusive, `YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**due_date_lte:** `typing.Optional[str]` 

Return invoices that are due before or on the specified date (`YYYY-MM-DD`).

This filter excludes quotes, credit notes, and draft invoices.
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` 

Return only receivables created by the entity user with the specified ID. To query receivables by multiple user IDs at once, use the `entity_user_id__in` parameter instead.

If the request is authenticated using an entity user token, this user must have the `receivable.read.allowed` (rather than `allowed_for_own`) permission to be able to query receivables created by other users.

IDs of deleted users will still produce results here if those users had associated receivables. Valid but nonexistent user IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id_in:** `typing.Optional[typing.Sequence[str]]` 

Return only receivables created by the entity users with the specified IDs.

If the request is authenticated using an entity user token, this user must have the `receivable.read.allowed` (rather than `allowed_for_own`) permission to be able to query receivables created by other users.

IDs of deleted users will still produce results here if those users had associated receivables. Valid but nonexistent user IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Sequence[str]]` — Return only receivables with the specified IDs. Valid but nonexistent IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gt:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued after the specified date and time. The value must be in the ISO 8601 format `YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm]`.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_gte:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lt:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**issue_date_lte:** `typing.Optional[dt.datetime]` — Return only non-draft receivables that were issued before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 250) to return in a single page of the response. Default is 100. The response may contain fewer items if it is the last or only page.

When using pagination with a non-default limit, you must provide the `limit` value alongside `pagination_token` in all subsequent pagination requests. Unlike other pagination parameters, `limit` is not inferred from `pagination_token`.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to `GET /receivables` or `POST /receivables/search`. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other parameters except `limit` are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**product_ids:** `typing.Optional[typing.Sequence[str]]` 

Return only receivables with line items containing all of the products with the specified IDs and optionally other products that are not specified.

For example, given receivables that contain the following products:

 1. productA
 2. productB
 3. productA, productB
 4. productC
 5. productA, productB, productC

`product_ids` = `[productA, productB]` will return receivables 3 and 5.

Valid but nonexistent product IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**product_ids_in:** `typing.Optional[typing.Sequence[str]]` 

Return only receivables with line items containing at least one of the products with the specified IDs.

For example, given receivables that contain the following products:

 1. productA
 2. productB
 3. productA, productB
 4. productC
 5. productB, productC

`product_ids__in` = `[productA, productB]` will return receivables 1, 2, 3, and 5.

Valid but nonexistent product IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[str]` — Return only receivables assigned to the project with the specified ID. Valid but nonexistent project IDs do not raise errors but return no results.
    
</dd>
</dl>

<dl>
<dd>

**project_id_in:** `typing.Optional[typing.Sequence[str]]` — Return only receivables that belong to one of the projects with the specified IDs. Valid but nonexistent project IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceivableCursorFields2]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ReceivablesSearchRequestStatus]` 

Return only receivables that have the specified status. See the applicable [invoice statuses](https://docs.monite.com/accounts-receivable/invoices/index), [quote statuses](https://docs.monite.com/accounts-receivable/quotes/index), and [credit note statuses](https://docs.monite.com/accounts-receivable/credit-notes#credit-note-lifecycle).

To query multiple statuses at once, use the `status__in` parameter instead.
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[typing.Sequence[str]]` — Return only receivables that have the specified statuses. See the applicable [invoice statuses](https://docs.monite.com/accounts-receivable/invoices/index), [quote statuses](https://docs.monite.com/accounts-receivable/quotes/index), and [credit note statuses](https://docs.monite.com/accounts-receivable/credit-notes#credit-note-lifecycle).
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Sequence[str]]` 

Return only receivables whose [tags](https://docs.monite.com/common/tags) include all of the tags with the specified IDs and optionally other tags that are not specified.

For example, given receivables with the following tags:

 1. tagA
 2. tagB
 3. tagA, tagB
 4. tagC
 5. tagA, tagB, tagC

`tag_ids` = `[tagA, tagB]` will return receivables 3 and 5.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids_in:** `typing.Optional[typing.Sequence[str]]` 

Return only receivables whose [tags](https://docs.monite.com/common/tags) include at least one of the tags with the specified IDs.

For example, given receivables with the following tags:

 1. tagA
 2. tagB
 3. tagA, tagB
 4. tagC
 5. tagB, tagC

`tag_ids__in` = `[tagA, tagB]` will return receivables 1, 2, 3, and 5.

Valid but nonexistent tag IDs do not raise errors but produce no results.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — Return only receivables with the exact specified total amount. The amount must be specified in the [minor units](https://docs.monite.com/references/currencies#minor-units) of currency. For example, $12.5 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gt:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) exceeds the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_gte:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) is greater than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lt:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) is less than the specified value.
    
</dd>
</dl>

<dl>
<dd>

**total_amount_lte:** `typing.Optional[int]` — Return only receivables whose total amount (in minor units) is less than or equal to the specified value.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ReceivableType]` — Return only receivables of the specified type. Use this parameter to get only invoices, or only quotes, or only credit notes.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_variables</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of placeholders that can be used in email templates for customization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_variables()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of an existing accounts receivable invoice, quote, or credit note with the specified ID.

The response fields vary depending on the document type. Use the `type` field to distinguish between different document types.

Entity users with the `receivable.read.allowed_for_own` permission (rather than `allowed`) can access only documents that they created themselves.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` — ID of an existing invoice, quote, or credit note that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.delete_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, UpdateQuote, UpdateQuotePayload

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.update_by_id(
    receivable_id="receivable_id",
    request=UpdateQuotePayload(
        quote=UpdateQuote(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReceivableUpdatePayload` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">accept_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only quotes in the `issued` status can be accepted.

When a quote is accepted, Monite automatically creates a draft invoice based on this quote. To find the newly created invoice, use `GET /receivables?based_on=QUOTE_ID`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.accept_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**signature:** `typing.Optional[Signature]` — The counterpart's signature. Required if the quote field `signature_required` is `true`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">cancel_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.cancel_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">clone_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a copy of an existing accounts receivable invoice or quote. The original document can be in any status. The cloned document will have the `draft` status.

Cloning a document requires that all of the referenced resource IDs (counterpart ID, product IDs, and others) still exist.

Most of the original document's data is copied as is, with a few exceptions:

 * Some fields are not copied: `attachments`, `document_id`, `issue_date`, quote `expiry_date`.
 * Counterpart details, entity bank account details, and entity VAT number are fetched anew from their corresponding IDs.
   This means, for example, that if the counterpart details have been changed since the original invoice or quote was created,
   the cloned document will use the current counterpart details rather than the old details from the original document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.clone_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` — ID of an existing invoice or quote that you want to clone.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">decline_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only quotes in the `issued` status can be declined.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.decline_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Field with a comment on why the client declined this Quote
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the history of the specified accounts receivable document. The history contains all revisions of the document, status updates, and other events that occurred during the document's lifecycle. For more information, see [Document history](https://docs.monite.com/accounts-receivable/document-history).

You can filter the history by the date range and event type. Events are sorted from oldest to newest by default.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_history(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` — ID of the accounts receivable document whose history you want to get.
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceivableHistoryCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**event_type_in:** `typing.Optional[
    typing.Union[
        ReceivableHistoryEventTypeEnum,
        typing.Sequence[ReceivableHistoryEventTypeEnum],
    ]
]` 

Return only the specified [event types](https://docs.monite.com/accounts-receivable/document-history#event-types). To include multiple types, repeat this parameter for each value:
`event_type__in=receivable_updated&event_type__in=status_changed`
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Return only events caused by the entity users with the specified IDs. To specify multiple user IDs, repeat this parameter for each ID:
`entity_user_id__in=<user1>&entity_user_id__in=<user2>`
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gt:** `typing.Optional[dt.datetime]` — Return only events that occurred after the specified date and time. The value must be in the ISO 8601 format `YYYY-MM-DDThh:mm[:ss[.ffffff]][Z|±hh:mm]`.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lt:** `typing.Optional[dt.datetime]` — Return only events that occurred before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gte:** `typing.Optional[dt.datetime]` — Return only events that occurred on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lte:** `typing.Optional[dt.datetime]` — Return only events that occurred before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_history_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a single record from the change history of the specified accounts receivable document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_history_by_id(
    receivable_history_id="receivable_history_id",
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_history_id:** `str` — ID of the history record to return. You can get these IDs from `GET /receivables/{receivable_id}/history`.
    
</dd>
</dl>

<dl>
<dd>

**receivable_id:** `str` — ID of the accounts receivable document whose history you want to get.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">issue_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.issue_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">update_line_items_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace all line items of an existing invoice or quote with a new list of line items.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import LineItem, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.update_line_items_by_id(
    receivable_id="receivable_id",
    data=[
        LineItem(
            quantity=1.1,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[LineItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_mails</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_mails(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ReceivableMailCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ReceivableMailStatusEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[
        ReceivableMailStatusEnum, typing.Sequence[ReceivableMailStatusEnum]
    ]
]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_mail_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_mail_by_id(
    receivable_id="receivable_id",
    mail_id="mail_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**mail_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">mark_as_paid_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.mark_as_paid_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Optional comment explaining how the payment was made.
    
</dd>
</dl>

<dl>
<dd>

**paid_at:** `typing.Optional[dt.datetime]` — Date and time when the invoice was paid.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">mark_as_partially_paid_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated. Use `POST /payment_records` to record an invoice payment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.mark_as_partially_paid_by_id(
    receivable_id="receivable_id",
    amount_paid=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount_paid:** `int` — How much has been paid on the invoice (in minor units).
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Optional comment explaining how the payment was made.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">mark_as_uncollectible_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.mark_as_uncollectible_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**comment:** `typing.Optional[str]` — Optional comment explains why the Invoice goes uncollectible.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">get_pdf_link_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.get_pdf_link_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">preview_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can preview emails only for documents in the following statuses:

 * Invoices: `draft`, `issued`, `overdue`, `partially_paid`, `paid`.
   In the [non-compliant mode](https://docs.monite.com/accounts-receivable/regulatory-compliance/invoice-compliance): also `canceled`.
 * Quotes: `draft`, `issued`.
 * Credit notes: `draft`, `issued`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.preview_by_id(
    receivable_id="receivable_id",
    body_text="body_text",
    subject_text="subject_text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body_text:** `str` — Body text of the content
    
</dd>
</dl>

<dl>
<dd>

**subject_text:** `str` — Subject text of the content
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[LanguageCodeEnum]` — Language code for localization purposes
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ReceivablesPreviewTypeEnum]` — The type of the preview document.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">send_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only documents in the following statuses can be sent via email:

 * Invoices: `draft`, `issued`, `overdue`, `partially_paid`, `paid`.
   In the [non-compliant mode](https://docs.monite.com/accounts-receivable/regulatory-compliance/invoice-compliance): also `canceled`.
 * Quotes: `draft`, `issued`.
 * Credit notes: `draft`, `issued`.

Draft documents are automatically moved to the `issued` status before sending.

For more information, see [Send an invoice via email](https://docs.monite.com/accounts-receivable/invoices/create#send-via-email).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.send_by_id(
    receivable_id="receivable_id",
    body_text="body_text",
    subject_text="subject_text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**body_text:** `str` — Body text of the content
    
</dd>
</dl>

<dl>
<dd>

**subject_text:** `str` — Subject text of the content
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">send_test_reminder_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.send_test_reminder_by_id(
    receivable_id="receivable_id",
    reminder_type="term_1",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reminder_type:** `ReminderTypeEnum` — The type of the reminder to be sent.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">verify_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.verify_by_id(
    receivable_id="receivable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Recurrences
<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.create(
    invoice_id="invoice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — ID of the base invoice that will be used as a template for creating recurring invoices.
    
</dd>
</dl>

<dl>
<dd>

**automation_level:** `typing.Optional[AutomationLevel]` 

Controls how invoices are processed when generated:
- "draft": Creates invoices in draft status, requiring manual review, issuing, and sending
- "issue": Automatically issues invoices but requires manual sending
- "issue_and_send": Fully automates the process (creates, issues, and sends invoices)

Default: "issue" (or "issue_and_send" if subject_text and body_text are provided)

Note: When using "issue_and_send", both subject_text and body_text must be provided.
    
</dd>
</dl>

<dl>
<dd>

**body_text:** `typing.Optional[str]` — The body text for the email that will be sent with the recurring invoice.
    
</dd>
</dl>

<dl>
<dd>

**day_of_month:** `typing.Optional[DayOfMonth]` — Deprecated, use `start_date` instead
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — The end date of the recurring invoice, in the `yyyy-mm-dd` format. The end date is inclusive, that is, the last invoice will be created on this date if the last occurrence falls on this date. `end_date` is mutually exclusive with `max_occurrences`. Either `end_date` or `max_occurrences` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**end_month:** `typing.Optional[int]` — Deprecated, use `end_date` instead
    
</dd>
</dl>

<dl>
<dd>

**end_year:** `typing.Optional[int]` — Deprecated, use `end_date` instead
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[RecurrenceFrequency]` — How often the invoice will be created.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[int]` — The interval between each occurrence of the invoice. For example, when using monthly frequency, an interval of 1 means invoices will be created every month, an interval of 2 means invoices will be created every 2 months.
    
</dd>
</dl>

<dl>
<dd>

**max_occurrences:** `typing.Optional[int]` — How many times the recurring invoice will be created. The recurrence will stop after this number is reached. `max_occurrences` is mutually exclusive with `end_date`. Either `max_occurrences` or `end_date` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` — An object containing the recipients (To, CC, BCC) of the recurring invoices. Can be omitted if the base invoice has the counterpart contact email specified in the `counterpart_contact.email` field.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — The date when the first invoice will be created, in the `yyyy-mm-dd` format. Cannot be a past date. Subsequent invoice dates will be calculated based on `start_date`, `frequency`, and `interval`.
    
</dd>
</dl>

<dl>
<dd>

**start_month:** `typing.Optional[int]` — Deprecated, use `start_date` instead
    
</dd>
</dl>

<dl>
<dd>

**start_year:** `typing.Optional[int]` — Deprecated, use `start_date` instead
    
</dd>
</dl>

<dl>
<dd>

**subject_text:** `typing.Optional[str]` — The subject for the email that will be sent with the recurring invoice.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.get_by_id(
    recurrence_id="recurrence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurrence_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.update_by_id(
    recurrence_id="recurrence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurrence_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**automation_level:** `typing.Optional[AutomationLevel]` 

Controls how invoices are processed when generated:
- "draft": Creates invoices in draft status, requiring manual review, issuing, and sending
- "issue": Automatically issues invoices but requires manual sending
- "issue_and_send": Fully automates the process (creates, issues, and sends invoices)

Default: "issue" (or "issue_and_send" if subject_text and body_text are provided)

Note: When using "issue_and_send", both subject_text and body_text must be provided.
    
</dd>
</dl>

<dl>
<dd>

**body_text:** `typing.Optional[str]` — The body text for the email that will be sent with the recurring invoice.
    
</dd>
</dl>

<dl>
<dd>

**day_of_month:** `typing.Optional[DayOfMonth]` — Deprecated, use `start_date` instead
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — The end date of the recurring invoice, in the `yyyy-mm-dd` format. The end date is inclusive, that is, the last invoice will be created on this date if the last occurrence falls on this date. `end_date` is mutually exclusive with `max_occurrences`. Either `end_date` or `max_occurrences` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**end_month:** `typing.Optional[int]` — Deprecated, use `end_date` instead
    
</dd>
</dl>

<dl>
<dd>

**end_year:** `typing.Optional[int]` — Deprecated, use `end_date` instead
    
</dd>
</dl>

<dl>
<dd>

**frequency:** `typing.Optional[RecurrenceFrequency]` — How often the invoice will be created.
    
</dd>
</dl>

<dl>
<dd>

**interval:** `typing.Optional[int]` — The interval between each occurrence of the invoice. For example, when using monthly frequency, an interval of 1 means invoices will be created every month, an interval of 2 means invoices will be created every 2 months.
    
</dd>
</dl>

<dl>
<dd>

**max_occurrences:** `typing.Optional[int]` — How many times the recurring invoice will be created. The recurrence will stop after this number is reached. `max_occurrences` is mutually exclusive with `end_date`. Either `max_occurrences` or `end_date` must be specified.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Optional[Recipients]` — An object containing the recipients (To, CC, BCC) of the recurring invoices. Can be omitted if the base invoice has the counterpart contact email specified in the `counterpart_contact.email` field.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — The date when the first invoice will be created, in the `yyyy-mm-dd` format. Cannot be a past date. Subsequent invoice dates will be calculated based on `start_date`, `frequency`, and `interval`.
    
</dd>
</dl>

<dl>
<dd>

**subject_text:** `typing.Optional[str]` — The subject for the email that will be sent with the recurring invoice.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">cancel_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.cancel_by_id(
    recurrence_id="recurrence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurrence_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">post_recurrences_id_pause</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.post_recurrences_id_pause(
    recurrence_id="recurrence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurrence_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recurrences.<a href="src/monite/recurrences/client.py">post_recurrences_id_resume</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.recurrences.post_recurrences_id_resume(
    recurrence_id="recurrence_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**recurrence_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/monite/roles/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find all roles that match the search criteria.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.roles.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[RoleCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/monite/roles/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new role from the specified values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import BizObjectsSchemaInput, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.roles.create(
    name="name",
    permissions=BizObjectsSchemaInput(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The role name is case-sensitive and must be unique.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `BizObjectsSchemaInput` — Access permissions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/monite/roles/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.roles.get_by_id(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/monite/roles/client.py">delete_roles_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a role with the specified ID. The role being deleted must not be in use by any entity users, otherwise a 409 error is returned. To check if there are entity users that have this role, call `GET /entity_users?role_id=ROLE_ID`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.roles.delete_roles_id(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.roles.<a href="src/monite/roles/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the specified fields with the provided values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.roles.update_by_id(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The new name for this role. Case-sensitive and must be unique.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[BizObjectsSchemaInput]` — Access permissions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Partner settings
<details><summary><code>client.partner_settings.<a href="src/monite/partner_settings/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partner-level settings apply to all entities of that partner.

See also:

 * [Get entity settings](https://docs.monite.com/api/entities/get-entities-id-settings)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.partner_settings.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_settings.<a href="src/monite/partner_settings/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partner-level settings apply to all entities of that partner.

See also:

 * [Update entity settings](https://docs.monite.com/api/entities/patch-entities-id-settings)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.partner_settings.update()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**api_version:** `typing.Optional[ApiVersion]` — Default API version for partner.
    
</dd>
</dl>

<dl>
<dd>

**commercial_conditions:** `typing.Optional[typing.Sequence[str]]` — Unused. To specify commercial conditions for invoices and quotes, use the `commercial_condition_description` field in those documents.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencySettingsInput]` — Custom currency exchange rates.
    
</dd>
</dl>

<dl>
<dd>

**default_role:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — A default role to provision upon new entity creation.
    
</dd>
</dl>

<dl>
<dd>

**mail:** `typing.Optional[MailSettings]` 

Settings for outgoing email. Used by:

 * accounts receivable emails, for example, emails sent by `POST /recevables/{receivable_id}/send`,
 * accounts payable approval notifications.
    
</dd>
</dl>

<dl>
<dd>

**payable:** `typing.Optional[PayableSettings]` — Settings for accounts payable.
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Optional[PaymentsSettingsInput]` — Settings for the payments module.
    
</dd>
</dl>

<dl>
<dd>

**receivable:** `typing.Optional[ReceivableSettings]` — Settings for accounts receivable.
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[typing.Sequence[Unit]]` — Unused. To manage the [measure units](https://docs.monite.com/accounts-receivable/products#manage-measure-units) for your entities, use the `/measure_units` endpoints.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — The URL of the partner's website. Must be an HTTPS URL. Required if the partner's entities use [payment links](https://docs.monite.com/payments/payment-links). The "Powered by" badge in the payment page footer will link to this website.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tags
<details><summary><code>client.tags.<a href="src/monite/tags/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all tags. Tags can be assigned to resources to assist with searching and filtering.
    Tags can also be used as trigger conditions in payable approval policies.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.tags.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[TagCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_by_entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/monite/tags/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new tag. The tag name must be unique.
    Tag names are case-sensitive, that is `Marketing` and `marketing` are two different tags.


The response returns an auto-generated ID assigned to this tag.
To assign this tag to a resource, send the tag ID in the `tag_ids` list when creating or updating a resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.tags.create(
    name="Marketing",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — The tag name. Must be unique.
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[TagCategory]` — The tag category.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The tag description.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/monite/tags/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a tag with the given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.tags.get_by_id(
    tag_id="tag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/monite/tags/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tag with the given ID. This tag will be automatically deleted from all resources where it was used.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.tags.delete_by_id(
    tag_id="tag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tags.<a href="src/monite/tags/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the tag name. The new name must be unique among existing tags.
    Tag names are case-sensitive, that is `Marketing` and `marketing` are two different tags.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.tags.update_by_id(
    tag_id="tag_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[TagCategory]` — The tag category.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — The tag description.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The tag name. Must be unique.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Text templates
<details><summary><code>client.text_templates.<a href="src/monite/text_templates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get text templates
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.text_templates.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[TextTemplateType]` 
    
</dd>
</dl>

<dl>
<dd>

**document_type:** `typing.Optional[TextTemplateDocumentTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_templates.<a href="src/monite/text_templates/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a text template
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.text_templates.create(
    document_type="quote",
    name="name",
    template="template",
    type="email_header",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_type:** `TextTemplateDocumentTypeEnum` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `TextTemplateType` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_templates.<a href="src/monite/text_templates/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all custom contents
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.text_templates.get_by_id(
    text_template_id="text_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_template_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_templates.<a href="src/monite/text_templates/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete custom content by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.text_templates.delete_by_id(
    text_template_id="text_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_template_id:** `str` — UUID text_template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_templates.<a href="src/monite/text_templates/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update custom content by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.text_templates.update_by_id(
    text_template_id="text_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_template_id:** `str` — UUID text_template ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.text_templates.<a href="src/monite/text_templates/client.py">make_default_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Make text template default
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.text_templates.make_default_by_id(
    text_template_id="text_template_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text_template_id:** `str` — UUID text_template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## VAT rates
<details><summary><code>client.vat_rates.<a href="src/monite/vat_rates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Monite maintains a catalog of VAT and sales tax rates for [select countries](https://docs.monite.com/accounts-receivable/vat-rates#supported-countries).

To query the applicable VAT/tax rates for an invoice or quote, use:

`GET /vat_rates?counterpart_id=<...>&entity_vat_id_id=<...>`

Or if the entity does not have a VAT ID:

`GET /vat_rates?counterpart_id=<...>`

**Note:** Entities from countries [not on the list](https://docs.monite.com/accounts-receivable/vat-rates#supported-countries) should not use this endpoint. Instead, those entities can either create custom VAT/tax rates or use the invoice field `line_items[].tax_rate_value` to specify the VAT/tax rates directly.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.vat_rates.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_address_id:** `typing.Optional[str]` — Unused. Reserved for future use.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` — ID of the counterpart that will be invoiced.
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` — Unused. Reserved for future use.
    
</dd>
</dl>

<dl>
<dd>

**entity_vat_id_id:** `typing.Optional[str]` — ID of the entity's VAT number (if any) used for the sales transaction.
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[ProductServiceTypeEnum]` — Unused. Reserved for future use.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhook deliveries
<details><summary><code>client.webhook_deliveries.<a href="src/monite/webhook_deliveries/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns an aggregated log of webhook delivery attempts. The data contains a list of triggered webhook events, how many times Monite tried to send each event to your server, the last HTTP status code returned by your webhook listener endpoint, and whether the final attempt to deliver that event was successful.

We guarantee access to webhook delivery data only from the last three months. Earlier data may be unavailable.

Note that if the same event type is included in multiple webhook subscriptions, the results will include several entries for each occurrence of this event - one entry per subscription.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_deliveries.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[WebhookDeliveryCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[WebhookObjectType]` 
    
</dd>
</dl>

<dl>
<dd>

**event_action:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Webhook subscriptions
<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of all [webhook](https://docs.monite.com/references/webhooks/index) subscriptions (both active and disabled).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[WebhookSubscriptionCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[WebhookObjectType]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` — Return only subscriptions created after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` — Return only subscriptions created before the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` — Return only subscriptions created on or after the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` — Return only subscriptions created before or on the specified date and time.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Related guide: [Webhooks](https://docs.monite.com/references/webhooks/index).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.create(
    event_types=[
        "created",
        "onboarding_requirements.updated",
        "onboarding_requirements.status_updated",
    ],
    object_type="entity",
    url="https://example.com/your-webhook-listener",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `WebhookObjectType` 

The [object type](https://docs.monite.com/references/webhooks/index#events) to whose events you want to subscribe.

To subscribe to events from multiple object types, create a separate subscription for each object type.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 

An HTTPS URL to which Monite will send webhooks. This URL must be accessible over the public Internet, accept POST requests, and respond with status code 200. It must be a direct URL (no redirects).

The same URL can be used by multiple webhook subscriptions.
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[str]]` — A list of [events](https://docs.monite.com/references/webhooks/index#events) to subscribe to. If set to an empty array, the subscription includes all events triggered by the specified `object_type`. 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the details of the webhook subscription with the specified ID.

The response does not include the [webhook signing secret](https://docs.monite.com/references/webhooks/signatures). If you lost the secret, you can [regenerate it](https://docs.monite.com/api/webhook-subscriptions/post-webhook-subscriptions-id-regenerate-secret).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.get_by_id(
    webhook_subscription_id="webhook_subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_subscription_id:** `str` — ID of the webhook subscription. This is the same value as the `webhook_subscription_id` you receive in webhooks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.delete_by_id(
    webhook_subscription_id="webhook_subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_subscription_id:** `str` — ID of the webhook subscription. This is the same value as the `webhook_subscription_id` you receive in webhooks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

You can update the webhook listener URL or the event list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.update_by_id(
    webhook_subscription_id="webhook_subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_subscription_id:** `str` — ID of the webhook subscription. This is the same value as the `webhook_subscription_id` you receive in webhooks.
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[str]]` — A list of [events](https://docs.monite.com/references/webhooks/index#events) to subscribe to. If set to an empty array, the subscription includes all events triggered by the specified `object_type`. 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[WebhookObjectType]` 

The [object type](https://docs.monite.com/references/webhooks/index#events) to whose events you want to subscribe.

To subscribe to events from multiple object types, create a separate subscription for each object type.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 

An HTTPS URL to which Monite will send webhooks. This URL must be accessible over the public Internet, accept POST requests, and respond with status code 200. It must be a direct URL (no redirects).

The same URL can be used by multiple webhook subscriptions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">disable_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.disable_by_id(
    webhook_subscription_id="webhook_subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_subscription_id:** `str` — ID of the webhook subscription. This is the same value as the `webhook_subscription_id` you receive in webhooks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">enable_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.enable_by_id(
    webhook_subscription_id="webhook_subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_subscription_id:** `str` — ID of the webhook subscription. This is the same value as the `webhook_subscription_id` you receive in webhooks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">regenerate_secret_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The webhook signing secret lets you [verify webhook signatures](https://docs.monite.com/references/webhooks/signatures). If you lost the original secret generated for any of your webhook subscriptions, you can regenerate it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.webhook_subscriptions.regenerate_secret_by_id(
    webhook_subscription_id="webhook_subscription_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_subscription_id:** `str` — ID of the webhook subscription. This is the same value as the `webhook_subscription_id` you receive in webhooks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounting Payables
<details><summary><code>client.accounting.payables.<a href="src/monite/accounting/payables/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of accounts payable invoices (bills) that exist in the entity's accounting system. This requires that an accounting connection has been previously established. Refer to the [Accounting integration guide](https://docs.monite.com/accounting/integration/index) for details.

This endpoint only provides read-only access to the accounting system's data but does not pull those payables into Monite. You can use it to review the data in the accounting system and find out which of those payables already exist or do not exist in Monite.

Data is actual as of the date and time of the last accounting synchronization, which is specified by the `last_pull` value in the response from `GET /accounting_connections/{connection_id}`. To make sure you are accessing the most up-to-date accounting data, you can use `POST /accounting_connections/{connection_id}/sync` to trigger on-demand synchronization before getting the list of payables.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.payables.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before selecting items to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.payables.<a href="src/monite/accounting/payables/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about an individual payable invoice (bill) that exists in the entity's accounting system. This payable may or may not also exist in Monite.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.payables.get_by_id(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` — An internal ID of the payable invoice (bill) in the accounting system. You can get these IDs from `GET /accounting/payables`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounting Receivables
<details><summary><code>client.accounting.receivables.<a href="src/monite/accounting/receivables/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of invoices that exist in the entity's accounting system. This requires that an accounting connection has been previously established. Refer to the [Accounting integration guide](https://docs.monite.com/accounting/integration/index) for details.

This endpoint only provides read-only access to the accounting system's data but does not pull those invoices into Monite. You can use it to review the data in the accounting system and find out which of those invoices already exist or do not exist in Monite.

Data is actual as of the date and time of the last accounting synchronization, which is specified by the `last_pull` value in the response from `GET /accounting_connections/{connection_id}`. To make sure you are accessing the most up-to-date accounting data, you can use `POST /accounting_connections/{connection_id}/sync` to trigger on-demand synchronization before getting the invoice list.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.receivables.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of results per page.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip before selecting items to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.receivables.<a href="src/monite/accounting/receivables/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns information about an individual invoice that exists in the entity's accounting system. This invoice may or may not also exist in Monite.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.receivables.get_by_id(
    invoice_id="invoice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_id:** `str` — An internal ID of the invoice in the accounting system. You can get these IDs from `GET /accounting/receivables`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounting Connections
<details><summary><code>client.accounting.connections.<a href="src/monite/accounting/connections/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all connections
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.connections.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.connections.<a href="src/monite/accounting/connections/client.py">create</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create new connection
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.connections.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.connections.<a href="src/monite/accounting/connections/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get connection by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.connections.get_by_id(
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.connections.<a href="src/monite/accounting/connections/client.py">disconnect_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.connections.disconnect_by_id(
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.connections.<a href="src/monite/accounting/connections/client.py">sync_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.connections.sync_by_id(
    connection_id="connection_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**connection_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounting SyncedRecords
<details><summary><code>client.accounting.synced_records.<a href="src/monite/accounting/synced_records/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get synchronized records
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.synced_records.get(
    object_type="product",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**object_type:** `ObjectMatchTypes` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 250) to return in a single page of the response. Default is 100. The response may contain fewer items if it is the last or only page. 

When using pagination with a non-default `limit`, you must provide the `limit` value alongside `pagination_token` in all subsequent pagination requests. Unlike other query parameters, `limit` is not inferred from `pagination_token`.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters except `limit` are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[SyncRecordCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.synced_records.<a href="src/monite/accounting/synced_records/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get synchronized record by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.synced_records.get_by_id(
    synced_record_id="synced_record_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**synced_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.synced_records.<a href="src/monite/accounting/synced_records/client.py">push_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Push object to the accounting system manually
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.synced_records.push_by_id(
    synced_record_id="synced_record_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**synced_record_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounting TaxRates
<details><summary><code>client.accounting.tax_rates.<a href="src/monite/accounting/tax_rates/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all tax rate accounts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.tax_rates.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 250) to return in a single page of the response. Default is 100. The response may contain fewer items if it is the last or only page. 

When using pagination with a non-default `limit`, you must provide the `limit` value alongside `pagination_token` in all subsequent pagination requests. Unlike other query parameters, `limit` is not inferred from `pagination_token`.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters except `limit` are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[TaxRateAccountCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.tax_rates.<a href="src/monite/accounting/tax_rates/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get tax rate account by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.tax_rates.get_by_id(
    tax_rate_id="tax_rate_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tax_rate_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Accounting LedgerAccounts
<details><summary><code>client.accounting.ledger_accounts.<a href="src/monite/accounting/ledger_accounts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all ledger accounts
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.ledger_accounts.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 250) to return in a single page of the response. Default is 100. The response may contain fewer items if it is the last or only page. 

When using pagination with a non-default `limit`, you must provide the `limit` value alongside `pagination_token` in all subsequent pagination requests. Unlike other query parameters, `limit` is not inferred from `pagination_token`.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters except `limit` are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[LedgerAccountCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.accounting.ledger_accounts.<a href="src/monite/accounting/ledger_accounts/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get ledger account by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.accounting.ledger_accounts.get_by_id(
    ledger_account_id="ledger_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**ledger_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ApprovalPolicies Processes
<details><summary><code>client.approval_policies.processes.<a href="src/monite/approval_policies/processes/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of all approval policy processes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.processes.get(
    approval_policy_id="approval_policy_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.processes.<a href="src/monite/approval_policies/processes/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific approval policy process.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.processes.get_by_id(
    approval_policy_id="approval_policy_id",
    process_id="process_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.processes.<a href="src/monite/approval_policies/processes/client.py">cancel_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel an ongoing approval process for a specific approval policy.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.processes.cancel_by_id(
    approval_policy_id="approval_policy_id",
    process_id="process_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.approval_policies.processes.<a href="src/monite/approval_policies/processes/client.py">get_steps</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of approval policy process steps.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.approval_policies.processes.get_steps(
    approval_policy_id="approval_policy_id",
    process_id="process_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**approval_policy_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**process_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Counterparts Addresses
<details><summary><code>client.counterparts.addresses.<a href="src/monite/counterparts/addresses/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.addresses.get(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.addresses.<a href="src/monite/counterparts/addresses/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.addresses.create(
    counterpart_id="counterpart_id",
    city="Berlin",
    country="AF",
    line1="Flughafenstrasse 52",
    postal_code="10115",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `str` — City name.
    
</dd>
</dl>

<dl>
<dd>

**country:** `AllowedCountries` — Two-letter ISO country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    
</dd>
</dl>

<dl>
<dd>

**line1:** `str` — Street address.
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `str` — ZIP or postal code.
    
</dd>
</dl>

<dl>
<dd>

**line2:** `typing.Optional[str]` — Additional address information (if any).
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — State, county, province, prefecture, region, or similar component of the counterpart's address. For US counterparts, `state` is required and must be a two-letter [USPS state abbreviation](https://pe.usps.com/text/pub28/28apb.htm), for example, NY or CA.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.addresses.<a href="src/monite/counterparts/addresses/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.addresses.get_by_id(
    address_id="address_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.addresses.<a href="src/monite/counterparts/addresses/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.addresses.delete_by_id(
    address_id="address_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.addresses.<a href="src/monite/counterparts/addresses/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.addresses.update_by_id(
    address_id="address_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**address_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**city:** `typing.Optional[str]` — City name.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[AllowedCountries]` — Two-letter ISO country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    
</dd>
</dl>

<dl>
<dd>

**line1:** `typing.Optional[str]` — Street address.
    
</dd>
</dl>

<dl>
<dd>

**line2:** `typing.Optional[str]` — Additional address information (if any).
    
</dd>
</dl>

<dl>
<dd>

**postal_code:** `typing.Optional[str]` — ZIP or postal code.
    
</dd>
</dl>

<dl>
<dd>

**state:** `typing.Optional[str]` — State, region, province, or county.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Counterparts BankAccounts
<details><summary><code>client.counterparts.bank_accounts.<a href="src/monite/counterparts/bank_accounts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.bank_accounts.get(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.bank_accounts.<a href="src/monite/counterparts/bank_accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.bank_accounts.create(
    counterpart_id="counterpart_id",
    country="AF",
    currency="AED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `AllowedCountries` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` 
    
</dd>
</dl>

<dl>
<dd>

**account_holder_name:** `typing.Optional[str]` — The name of the person or business that owns this bank account. Required for US bank accounts to accept ACH payments.
    
</dd>
</dl>

<dl>
<dd>

**account_number:** `typing.Optional[str]` — The bank account number. Required for US bank accounts to accept ACH payments. US account numbers contain 9 to 12 digits. UK account numbers typically contain 8 digits.
    
</dd>
</dl>

<dl>
<dd>

**bic:** `typing.Optional[str]` — The BIC/SWIFT code of the bank.
    
</dd>
</dl>

<dl>
<dd>

**iban:** `typing.Optional[str]` — The IBAN of the bank account.
    
</dd>
</dl>

<dl>
<dd>

**is_default_for_currency:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata for partner needs.
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `typing.Optional[str]` — The bank's routing transit number (RTN). Required for US bank accounts to accept ACH payments. US routing numbers consist of 9 digits.
    
</dd>
</dl>

<dl>
<dd>

**sort_code:** `typing.Optional[str]` — The bank's sort code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.bank_accounts.<a href="src/monite/counterparts/bank_accounts/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.bank_accounts.get_by_id(
    bank_account_id="bank_account_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.bank_accounts.<a href="src/monite/counterparts/bank_accounts/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.bank_accounts.delete_by_id(
    bank_account_id="bank_account_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.bank_accounts.<a href="src/monite/counterparts/bank_accounts/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.bank_accounts.update_by_id(
    bank_account_id="bank_account_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_holder_name:** `typing.Optional[str]` — The name of the person or business that owns this bank account. Required for US bank accounts to accept ACH payments.
    
</dd>
</dl>

<dl>
<dd>

**account_number:** `typing.Optional[str]` — The bank account number. Required for US bank accounts to accept ACH payments. US account numbers contain 9 to 12 digits. UK account numbers typically contain 8 digits.
    
</dd>
</dl>

<dl>
<dd>

**bic:** `typing.Optional[str]` — The BIC/SWIFT code of the bank.
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[AllowedCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**iban:** `typing.Optional[str]` — The IBAN of the bank account.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Metadata for partner needs.
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `typing.Optional[str]` — The bank's routing transit number (RTN). Required for US bank accounts to accept ACH payments. US routing numbers consist of 9 digits.
    
</dd>
</dl>

<dl>
<dd>

**sort_code:** `typing.Optional[str]` — The bank's sort code.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.bank_accounts.<a href="src/monite/counterparts/bank_accounts/client.py">make_default_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.bank_accounts.make_default_by_id(
    bank_account_id="bank_account_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Counterparts Contacts
<details><summary><code>client.counterparts.contacts.<a href="src/monite/counterparts/contacts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.contacts.get(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.contacts.<a href="src/monite/counterparts/contacts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import CounterpartAddress, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.contacts.create(
    counterpart_id="counterpart_id",
    address=CounterpartAddress(
        city="Berlin",
        country="AF",
        line1="Flughafenstrasse 52",
        postal_code="10115",
    ),
    first_name="Mary",
    last_name="O'Brien",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `CounterpartAddress` — The address of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `str` — The first name of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — The last name of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The phone number of a contact person
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title or honorific of a contact person. Examples: Mr., Ms., Dr., Prof.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.contacts.<a href="src/monite/counterparts/contacts/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.contacts.get_by_id(
    contact_id="contact_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.contacts.<a href="src/monite/counterparts/contacts/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.contacts.delete_by_id(
    contact_id="contact_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.contacts.<a href="src/monite/counterparts/contacts/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.contacts.update_by_id(
    contact_id="contact_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[CounterpartAddress]` — The address of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The email address of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The first name of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The last name of a contact person.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The phone number of a contact person
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — The title or honorific of a contact person. Examples: Mr., Ms., Dr., Prof.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.contacts.<a href="src/monite/counterparts/contacts/client.py">make_default_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.contacts.make_default_by_id(
    contact_id="contact_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contact_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Counterparts VatIds
<details><summary><code>client.counterparts.vat_ids.<a href="src/monite/counterparts/vat_ids/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.vat_ids.get(
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.vat_ids.<a href="src/monite/counterparts/vat_ids/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.vat_ids.create(
    counterpart_id="counterpart_id",
    value="123456789",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[AllowedCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[VatIdTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.vat_ids.<a href="src/monite/counterparts/vat_ids/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.vat_ids.get_by_id(
    vat_id="vat_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.vat_ids.<a href="src/monite/counterparts/vat_ids/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.vat_ids.delete_by_id(
    vat_id="vat_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.counterparts.vat_ids.<a href="src/monite/counterparts/vat_ids/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.vat_ids.update_by_id(
    vat_id="vat_id",
    counterpart_id="counterpart_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**vat_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[AllowedCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[VatIdTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DataExports ExtraData
<details><summary><code>client.data_exports.extra_data.<a href="src/monite/data_exports/extra_data/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.extra_data.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ExportSettingCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**created_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**updated_at_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**field_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**field_value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.extra_data.<a href="src/monite/data_exports/extra_data/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.extra_data.create(
    field_name="default_account_code",
    field_value="field_value",
    object_id="object_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**field_name:** `SupportedFieldNames` 
    
</dd>
</dl>

<dl>
<dd>

**field_value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.extra_data.<a href="src/monite/data_exports/extra_data/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.extra_data.get_by_id(
    extra_data_id="extra_data_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_data_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.extra_data.<a href="src/monite/data_exports/extra_data/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.extra_data.delete_by_id(
    extra_data_id="extra_data_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_data_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.data_exports.extra_data.<a href="src/monite/data_exports/extra_data/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.data_exports.extra_data.update_by_id(
    extra_data_id="extra_data_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**extra_data_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**field_name:** `typing.Optional[SupportedFieldNames]` 
    
</dd>
</dl>

<dl>
<dd>

**field_value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[typing.Literal["counterpart"]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities BankAccounts
<details><summary><code>client.entities.bank_accounts.<a href="src/monite/entities/bank_accounts/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all bank accounts of this entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.bank_accounts.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.bank_accounts.<a href="src/monite/entities/bank_accounts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new bank account for the specified entity.

The minimum required fields are `currency` and `country`. Other required fields depend on the currency and country.

Bank accounts in African countries can use any fields or combinations of fields.

For other countries:
* EUR accounts require `iban`.
* GBP accounts require `account_holder_name`, `account_number`, and `sort_code`.
* USD accounts require `account_holder_name`, `account_number`, and `routing_number`.
* Accounts in other currencies require one of:
  * `iban`
  * `account_number` and `sort_code`
  * `account_number` and `routing_number`
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.bank_accounts.create(
    account_holder_name="Bob Jones",
    account_number="2571714302",
    bank_name="WELLS FARGO",
    country="US",
    currency="USD",
    display_name="Primary account",
    is_default_for_currency=True,
    routing_number="061000227",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country:** `AllowedCountries` — The country in which the bank account is registered, repsesented as a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — The currency of the bank account, represented as a three-letter ISO [currency code](https://docs.monite.com/references/currencies).
    
</dd>
</dl>

<dl>
<dd>

**account_holder_name:** `typing.Optional[str]` 

The name of the person or business that owns this bank account. Required in the following cases:
* the account currency is GBP or USD,
* the account currency is EUR and the entity wishes to receive SEPA Credit transfers to this account.
    
</dd>
</dl>

<dl>
<dd>

**account_number:** `typing.Optional[str]` — The bank account number. Required if the account currency is GBP or USD. UK account numbers typically contain 8 digits. US bank account numbers contain 9 to 12 digits.
    
</dd>
</dl>

<dl>
<dd>

**bank_name:** `typing.Optional[str]` — The bank name.
    
</dd>
</dl>

<dl>
<dd>

**bic:** `typing.Optional[str]` 

The SWIFT/BIC code of the bank. Can be either 8 or 11 characters long. Monite verifies the BIC length, country code, and whether the structure conforms to ISO 9362.

If `bic` is specified, `iban` must also be specified.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — User-defined name of this bank account, such as 'Primary account' or 'Savings account'.
    
</dd>
</dl>

<dl>
<dd>

**iban:** `typing.Optional[str]` — The IBAN of the bank account, up to 34 characters. Required if the account currency is EUR. Monite verifies the IBAN length, checksum digits, and country-specific format according to ISO 13616.
    
</dd>
</dl>

<dl>
<dd>

**is_default_for_currency:** `typing.Optional[bool]` — If set to `true` or if this is the first bank account added for the given currency, this account becomes the default one for its currency.
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `typing.Optional[str]` — The bank's routing transit number (RTN) or branch code. Required if the account currency is USD. US routing numbers consist of 9 digits.
    
</dd>
</dl>

<dl>
<dd>

**sort_code:** `typing.Optional[str]` — The bank's sort code. Required if the account currency is GBP.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.bank_accounts.<a href="src/monite/entities/bank_accounts/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a bank account by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.bank_accounts.get_by_id(
    bank_account_id="bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.bank_accounts.<a href="src/monite/entities/bank_accounts/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the bank account specified by its ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.bank_accounts.delete_by_id(
    bank_account_id="bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.bank_accounts.<a href="src/monite/entities/bank_accounts/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change the specified fields with the provided values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.bank_accounts.update_by_id(
    bank_account_id="bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**account_holder_name:** `typing.Optional[str]` — The name of the person or business that owns this bank account. If the account currency is GBP or USD, the holder name cannot be changed to an empty string.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — User-defined name of this bank account, such as 'Primary account' or 'Savings account'.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.bank_accounts.<a href="src/monite/entities/bank_accounts/client.py">make_default_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set a bank account as the default for this entity per currency.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.bank_accounts.make_default_by_id(
    bank_account_id="bank_account_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bank_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities OnboardingData
<details><summary><code>client.entities.onboarding_data.<a href="src/monite/entities/onboarding_data/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.onboarding_data.get(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.onboarding_data.<a href="src/monite/entities/onboarding_data/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.onboarding_data.update(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**business_profile:** `typing.Optional[BusinessProfileInput]` — Business information about the entity.
    
</dd>
</dl>

<dl>
<dd>

**ownership_declaration:** `typing.Optional[OwnershipDeclarationInput]` — Used to attest that the beneficial owner information provided is both current and correct.
    
</dd>
</dl>

<dl>
<dd>

**tos_acceptance:** `typing.Optional[TermsOfServiceAcceptanceInput]` — Details on the entity's acceptance of the service agreement.
    
</dd>
</dl>

<dl>
<dd>

**treasury_tos_acceptance:** `typing.Optional[TermsOfServiceAcceptanceInput]` — Details on the entity's acceptance of the Stripe Treasury service agreement.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities PaymentMethods
<details><summary><code>client.entities.payment_methods.<a href="src/monite/entities/payment_methods/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all enabled payment methods.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.payment_methods.get(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.payment_methods.<a href="src/monite/entities/payment_methods/client.py">set</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Set which payment methods should be enabled.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.payment_methods.set(
    entity_id="entity_id",
    payment_methods_receive=["card", "us_ach", "affirm", "klarna"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.Optional[typing.Sequence[MoniteAllPaymentMethodsTypes]]` — Deprecated. Replaced by `payment_methods_receive`.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods_receive:** `typing.Optional[typing.Sequence[MoniteAllPaymentMethodsTypes]]` 

Payment methods to receive money from customers. Supported payment methods [vary per country](https://docs.monite.com/payments/payment-methods).

`card` includes card payments, Apple Pay, and Google Pay. The values `applepay` and `googlepay` are deprecated and unused.

`sofort` is deprecated and replaced by `klarna`.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods_send:** `typing.Optional[typing.Sequence[MoniteAllPaymentMethodsTypes]]` 

Only for entities in the EU and UK. Payment methods used to make payments to vendors.

Currently only `sepa_credit` is supported for making payments.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities VatIds
<details><summary><code>client.entities.vat_ids.<a href="src/monite/entities/vat_ids/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.vat_ids.get(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.vat_ids.<a href="src/monite/entities/vat_ids/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.vat_ids.create(
    entity_id="entity_id",
    country="AF",
    value="123456789",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `AllowedCountries` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[VatIdTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.vat_ids.<a href="src/monite/entities/vat_ids/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.vat_ids.get_by_id(
    id="id",
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.vat_ids.<a href="src/monite/entities/vat_ids/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.vat_ids.delete_by_id(
    id="id",
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.vat_ids.<a href="src/monite/entities/vat_ids/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.vat_ids.update_by_id(
    id="id",
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entity_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[AllowedCountries]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[VatIdTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**value:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities Persons
<details><summary><code>client.entities.persons.<a href="src/monite/entities/persons/client.py">get</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.persons.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.persons.<a href="src/monite/entities/persons/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, PersonRelationshipRequest

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.persons.create(
    email="email",
    first_name="first_name",
    last_name="last_name",
    relationship=PersonRelationshipRequest(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — The person's email address
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `str` — The person's first name
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `str` — The person's last name
    
</dd>
</dl>

<dl>
<dd>

**relationship:** `PersonRelationshipRequest` — Describes the person's relationship to the entity
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[PersonAddressRequest]` — The person's address
    
</dd>
</dl>

<dl>
<dd>

**citizenship:** `typing.Optional[AllowedCountries]` — Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.
    
</dd>
</dl>

<dl>
<dd>

**date_of_birth:** `typing.Optional[str]` — The person's date of birth
    
</dd>
</dl>

<dl>
<dd>

**id_number:** `typing.Optional[str]` — The person's ID number, as appropriate for their country
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The person's phone number
    
</dd>
</dl>

<dl>
<dd>

**ssn_last4:** `typing.Optional[str]` — The last four digits of the person's Social Security number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.persons.<a href="src/monite/entities/persons/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.persons.get_by_id(
    person_id="person_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**person_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.persons.<a href="src/monite/entities/persons/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.persons.delete_by_id(
    person_id="person_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**person_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.persons.<a href="src/monite/entities/persons/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.persons.update_by_id(
    person_id="person_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**person_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[OptionalPersonAddressRequest]` — The person's address
    
</dd>
</dl>

<dl>
<dd>

**citizenship:** `typing.Optional[AllowedCountries]` — Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.
    
</dd>
</dl>

<dl>
<dd>

**date_of_birth:** `typing.Optional[str]` — The person's date of birth
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The person's email address
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The person's first name
    
</dd>
</dl>

<dl>
<dd>

**id_number:** `typing.Optional[str]` — The person's ID number, as appropriate for their country
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The person's last name
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The person's phone number
    
</dd>
</dl>

<dl>
<dd>

**relationship:** `typing.Optional[OptionalPersonRelationship]` — Describes the person's relationship to the entity
    
</dd>
</dl>

<dl>
<dd>

**ssn_last4:** `typing.Optional[str]` — The last four digits of the person's Social Security number
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.persons.<a href="src/monite/entities/persons/client.py">upload_onboarding_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Provide files for person onboarding verification
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.entities.persons.upload_onboarding_documents(
    person_id="person_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**person_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**additional_verification_document_back:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**additional_verification_document_front:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_document_back:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**verification_document_front:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Payables LineItems
<details><summary><code>client.payables.line_items.<a href="src/monite/payables/line_items/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of all line items related to a specific payable.
Related guide: [List all payable line items](https://docs.monite.com/accounts-payable/payables/line-items#list-all-line-items-of-a-payable)

See also:

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)

[Collect payables](https://docs.monite.com/accounts-payable/payables/collect)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.line_items.get(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page.
    
</dd>
</dl>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 

A pagination token obtained from a previous call to this endpoint. Use it to get the next or previous page of results for your initial query. If `pagination_token` is specified, all other query parameters are ignored and inferred from the initial query.

If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[LineItemCursorFields]` — The field to sort the results by. Typically used together with the `order` parameter.
    
</dd>
</dl>

<dl>
<dd>

**was_created_by_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.line_items.<a href="src/monite/payables/line_items/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new line item to a specific payable.

The `subtotal` and `total` fields of line items are automatically calculated based on the `unit_price`,
 `quantity`, and `tax` fields, therefore, are read-only and appear only in the response schema. The field
  `ledger_account_id` is required **only** for account integration, otherwise, it is optional.

Related guide: [Add line items to a payable](https://docs.monite.com/accounts-payable/payables/line-items#add-line-items-to-a-payable)

See also:

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)

[Collect payables](https://docs.monite.com/accounts-payable/payables/collect)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.line_items.create(
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accounting_tax_rate_id:** `typing.Optional[str]` — ID of the tax rate reference used for accounting integration. May be used to override auto-picked tax rate reference in accounting platform in case of any platform-specific constraints.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the product.
    
</dd>
</dl>

<dl>
<dd>

**ledger_account_id:** `typing.Optional[str]` — ID of the account record used to store bookkeeping entries for balance-sheet and income-statement transactions.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the product.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[float]` — The quantity of each of the goods, materials, or services listed in the payable.
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — VAT rate in percent [minor units](https://docs.monite.com/references/currencies#minor-units). Example: 12.5% is 1250.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` — The unit of the product
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[int]` — The unit price of the product, in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.line_items.<a href="src/monite/payables/line_items/client.py">replace</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the information of all line items of a specific payable.

Related guide: [Replace all line items](https://docs.monite.com/accounts-payable/payables/line-items#replace-all-line-items)

See also:

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)

[Collect payables](https://docs.monite.com/accounts-payable/payables/collect)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import LineItemInternalRequest, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.line_items.replace(
    payable_id="payable_id",
    data=[LineItemInternalRequest()],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Sequence[LineItemInternalRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.line_items.<a href="src/monite/payables/line_items/client.py">get_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a specific line item with a given ID.

Related guide: [Retrieve a line item](https://docs.monite.com/accounts-payable/payables/line-items#retrieve-a-line-item)

See also:

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)

[Collect payables](https://docs.monite.com/accounts-payable/payables/collect)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.line_items.get_by_id(
    line_item_id="line_item_id",
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.line_items.<a href="src/monite/payables/line_items/client.py">delete_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the line item with the given ID.

Related guide: [Remove a line item](https://docs.monite.com/accounts-payable/payables/line-items#remove-a-line-item)

See also:

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)

[Collect payables](https://docs.monite.com/accounts-payable/payables/collect)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.line_items.delete_by_id(
    line_item_id="line_item_id",
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.payables.line_items.<a href="src/monite/payables/line_items/client.py">update_by_id</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Edits the information of a specific line item.

Related guide: [Update a line item](https://docs.monite.com/accounts-payable/payables/line-items#update-a-line-item)

See also:

[Manage line items](https://docs.monite.com/accounts-payable/payables/line-items)

[Collect payables](https://docs.monite.com/accounts-payable/payables/collect)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payables.line_items.update_by_id(
    line_item_id="line_item_id",
    payable_id="payable_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**line_item_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**payable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**accounting_tax_rate_id:** `typing.Optional[str]` — ID of the tax rate reference used for accounting integration. May be used to override auto-picked tax rate reference in accounting platform in case of any platform-specific constraints.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the product.
    
</dd>
</dl>

<dl>
<dd>

**ledger_account_id:** `typing.Optional[str]` — ID of the account record used to store bookkeeping entries for balance-sheet and income-statement transactions.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name of the product.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `typing.Optional[float]` — The quantity of each of the goods, materials, or services listed in the payable.
    
</dd>
</dl>

<dl>
<dd>

**tax:** `typing.Optional[int]` — VAT rate in percent [minor units](https://docs.monite.com/references/currencies#minor-units). Example: 12.5% is 1250.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` — The unit of the product
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[int]` — The unit price of the product, in [minor units](https://docs.monite.com/references/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

