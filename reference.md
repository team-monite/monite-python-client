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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.analytics.get_analytics_credit_notes(metric="id", aggregation_function="count", )

```
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

**status_in:** `typing.Optional[typing.Union[PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status_not_in:** `typing.Optional[typing.Union[PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]]]` 
    
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.analytics.get_analytics_payables(metric="id", aggregation_function="count", )

```
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

**status_in:** `typing.Optional[typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]]` 

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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.analytics.get_analytics_receivables(metric="id", aggregation_function="count", )

```
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

**status_in:** `typing.Optional[typing.Union[GetAnalyticsReceivablesRequestStatusInItem, typing.Sequence[GetAnalyticsReceivablesRequestStatusInItem]]]` 

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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**status_in:** `typing.Optional[typing.Union[ApprovalPoliciesGetRequestStatusInItem, typing.Sequence[ApprovalPoliciesGetRequestStatusInItem]]]` 
    
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_policies.create(name='name', script=[True], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_policies.get_by_id(approval_policy_id='approval_policy_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_policies.delete_by_id(approval_policy_id='approval_policy_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_policies.update_by_id(approval_policy_id='approval_policy_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**order:** `typing.Optional[OrderEnum]` — Order by
    
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

**sort:** `typing.Optional[ApprovalRequestCursorFields]` — Allowed sort fields
    
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

**status_in:** `typing.Optional[typing.Union[ApprovalRequestStatus, typing.Sequence[ApprovalRequestStatus]]]` 
    
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
from monite import Monite
from monite import ApprovalRequestCreateByRoleRequest
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_requests.create(request=ApprovalRequestCreateByRoleRequest(object_id='object_id', object_type="account", required_approval_count=1, role_ids=['role_ids'], ), )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_requests.get_by_id(approval_request_id='approval_request_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_requests.approve_by_id(approval_request_id='approval_request_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_requests.cancel_by_id(approval_request_id='approval_request_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.approval_requests.reject_by_id(approval_request_id='approval_request_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.access_tokens.revoke(client_id='client_id', client_secret='client_secret', token='token', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**token:** `str` 
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.access_tokens.create(client_id='client_id', client_secret='client_secret', grant_type="client_credentials", )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**grant_type:** `GrantType` 
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.comments.get(object_id='object_id', )

```
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

**order:** `typing.Optional[OrderEnum]` — Order by
    
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

**sort:** `typing.Optional[CommentCursorFields]` — Allowed sort fields
    
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.comments.create(object_id='object_id', object_type='object_type', text='text', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.comments.get_by_id(comment_id='comment_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.comments.delete_by_id(comment_id='comment_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.comments.update_by_id(comment_id='comment_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.get(sort_code='123456', )

```
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
from monite import Monite
from monite import CounterpartCreatePayload_Organization
from monite import CounterpartOrganizationCreatePayload
from monite import CounterpartAddress
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.create(request=CounterpartCreatePayload_Organization(organization=CounterpartOrganizationCreatePayload(address=CounterpartAddress(city='Berlin', country="AF", line1='Flughafenstrasse 52', postal_code='10115', ), is_customer=True, is_vendor=True, legal_name='Acme Inc.', ), ), )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.get_by_id(counterpart_id='counterpart_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.delete_by_id(counterpart_id='counterpart_id', )

```
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
from monite import Monite
from monite import CounterpartIndividualRootUpdatePayload
from monite import CounterpartIndividualUpdatePayload
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.update_by_id(counterpart_id='counterpart_id', request=CounterpartIndividualRootUpdatePayload(individual=CounterpartIndividualUpdatePayload(), ), )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.get_partner_metadata_by_id(counterpart_id='counterpart_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterparts.update_partner_metadata_by_id(counterpart_id='counterpart_id', metadata={'key': 'value'
}, )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterpart_e_invoicing_credentials.get_counterparts_id_einvoicing_credentials(counterpart_id='counterpart_id', )

```
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
from monite import Monite
from monite import CreateCounterpartEinvoicingCredentialCounterpartVatId
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterpart_e_invoicing_credentials.post_counterparts_id_einvoicing_credentials(counterpart_id='counterpart_id', request=CreateCounterpartEinvoicingCredentialCounterpartVatId(counterpart_vat_id_id='counterpart_vat_id_id', ), )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterpart_e_invoicing_credentials.get_counterparts_id_einvoicing_credentials_id(credential_id='credential_id', counterpart_id='counterpart_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterpart_e_invoicing_credentials.delete_counterparts_id_einvoicing_credentials_id(credential_id='credential_id', counterpart_id='counterpart_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.counterpart_e_invoicing_credentials.patch_counterparts_id_einvoicing_credentials_id(credential_id='credential_id', counterpart_id='counterpart_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**order:** `typing.Optional[OrderEnum]` — Order by
    
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

**sort:** `typing.Optional[DataExportCursorFields]` — Allowed sort fields
    
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
from monite import Monite
from monite import ExportObjectSchema_Payable
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.data_exports.create(date_from='date_from', date_to='date_to', format="csv", objects=[ExportObjectSchema_Payable(statuses=["draft"], )], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.data_exports.get_by_id(document_export_id='document_export_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**status_in:** `typing.Optional[typing.Union[DeliveryNoteStatusEnum, typing.Sequence[DeliveryNoteStatusEnum]]]` 
    
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
from monite import Monite
from monite import DeliveryNoteCreateRequest
from monite import DeliveryNoteCreateLineItem
from monite import DeliveryNoteLineItemProduct
from monite import UnitRequest
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.delivery_notes.post_delivery_notes(request=DeliveryNoteCreateRequest(counterpart_address_id='a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6', counterpart_id='a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6', delivery_date='2025-01-01', delivery_number='102-2025-0987', display_signature_placeholder=True, line_items=[DeliveryNoteCreateLineItem(product_id='a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6', quantity=10.0, ), DeliveryNoteCreateLineItem(product=DeliveryNoteLineItemProduct(description='Description of product 2', measure_unit=UnitRequest(description='pieces', name='pcs', ), name='Product 2', ), quantity=20.0, )], memo='This is a memo', ), )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.delivery_notes.get_delivery_notes_id(delivery_note_id='delivery_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.delivery_notes.delete_delivery_notes_id(delivery_note_id='delivery_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.delivery_notes.patch_delivery_notes_id(delivery_note_id='delivery_note_id', )

```
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

**memo:** `typing.Optional[str]` — Additional information regarding the delivery note
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.delivery_notes.post_delivery_notes_id_cancel(delivery_note_id='delivery_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.delivery_notes.post_delivery_notes_id_mark_as_delivered(delivery_note_id='delivery_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.pdf_templates.get_by_id(document_template_id='document_template_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.pdf_templates.make_default_by_id(document_template_id='document_template_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
from monite import Monite
from monite import EinvoicingAddress
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.e_invoicing_connections.post_einvoicing_connections(address=EinvoicingAddress(address_line1='address_line1', city='city', country="DE", postal_code='postal_code', ), )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.e_invoicing_connections.get_einvoicing_connections_id(einvoicing_connection_id='einvoicing_connection_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.e_invoicing_connections.delete_einvoicing_connections_id(einvoicing_connection_id='einvoicing_connection_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.e_invoicing_connections.patch_einvoicing_connections_id(einvoicing_connection_id='einvoicing_connection_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.e_invoicing_connections.post_einvoicing_connections_id_network_credentials(einvoicing_connection_id='einvoicing_connection_id', network_credentials_identifier='12345678', network_credentials_schema="DE:VAT", )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
from monite import Monite
from monite import EntityAddressSchema
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.create(address=EntityAddressSchema(city='city', country="AF", line1='line1', postal_code='postal_code', ), email='email', type="individual", )

```
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

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[IndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OptionalOrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[OptionalIndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
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

Retrieve an entity by its ID.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.get_by_id(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.update_by_id(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OptionalOrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[OptionalIndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.post_entities_id_activate(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.post_entities_id_deactivate(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.upload_logo_by_id(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.delete_logo_by_id(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.get_partner_metadata_by_id(entity_id='entity_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.update_partner_metadata_by_id(entity_id='entity_id', metadata={'key': 'value'
}, )

```
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

Retrieve all settings for this entity.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.get_settings_by_id(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entities.update_settings_by_id(entity_id='ea837e28-509b-4b6a-a600-d54b6aa0b1f5', )

```
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

**language:** `typing.Optional[LanguageCodeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencySettingsInput]` 
    
</dd>
</dl>

<dl>
<dd>

**reminder:** `typing.Optional[RemindersSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**vat_mode:** `typing.Optional[VatModeEnum]` — Defines whether the prices of products in receivables will already include VAT or not.
    
</dd>
</dl>

<dl>
<dd>

**vat_inclusive_discount_mode:** `typing.Optional[VatModeEnum]` — Defines whether the amount discounts (for percentage discounts it does not matter) on VAT inclusive invoices will be applied on amounts including VAT or excluding VAT.
    
</dd>
</dl>

<dl>
<dd>

**payment_priority:** `typing.Optional[PaymentPriorityEnum]` — Payment preferences for entity to automate calculating suggested payment date based on payment terms and entity preferences.
    
</dd>
</dl>

<dl>
<dd>

**allow_purchase_order_autolinking:** `typing.Optional[bool]` — Automatically attempt to find a corresponding purchase order for all incoming payables.
    
</dd>
</dl>

<dl>
<dd>

**receivable_edit_flow:** `typing.Optional[ReceivableEditFlow]` 
    
</dd>
</dl>

<dl>
<dd>

**document_ids:** `typing.Optional[DocumentIDsSettingsRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**payables_ocr_auto_tagging:** `typing.Optional[typing.Sequence[OcrAutoTaggingSettingsRequest]]` — Auto tagging settings for all incoming OCR payable documents.
    
</dd>
</dl>

<dl>
<dd>

**quote_signature_required:** `typing.Optional[bool]` — Sets the default behavior of whether a signature is required to accept quotes.
    
</dd>
</dl>

<dl>
<dd>

**generate_paid_invoice_pdf:** `typing.Optional[bool]` 

This setting affects how PDF is generated for paid accounts receivable invoices. If set to `true`, once an invoice is fully paid its PDF version is updated to display the amount paid and the payment-related features are removed.

The PDF file gets regenerated at the moment when an invoice becomes paid. It is not issued as a separate document, and the original PDF invoice is no longer available.

This field is deprecated and will be replaced by `document_rendering.invoice.generate_paid_invoice_pdf`.
    
</dd>
</dl>

<dl>
<dd>

**accounting:** `typing.Optional[AccountingSettings]` 
    
</dd>
</dl>

<dl>
<dd>

**payables_skip_approval_flow:** `typing.Optional[bool]` — If enabled, the approval policy will be skipped and the payable will be moved to `waiting_to_be_paid` status.
    
</dd>
</dl>

<dl>
<dd>

**document_rendering:** `typing.Optional[DocumentRenderingSettings]` — Settings for rendering documents in PDF format.
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entity_users.create(first_name='Casey', login='login', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**first_name:** `str` — First name
    
</dd>
</dl>

<dl>
<dd>

**login:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — An entity user business email
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — An entity user phone number in the international format
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` — UUID of the role assigned to this entity user
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**email:** `typing.Optional[str]` — An entity user business email
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — An entity user phone number in the international format
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title
    
</dd>
</dl>

<dl>
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

Retrieves information of an entity, which this entity user belongs to.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

Update information of an entity, which this entity user belongs to.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**phone:** `typing.Optional[str]` — The contact phone number of the entity. Required for US organizations to use payments.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` — A website of the entity
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — The entity's taxpayer identification number or tax ID. This field is required for entities that are non-VAT registered.
    
</dd>
</dl>

<dl>
<dd>

**registration_number:** `typing.Optional[str]` — (Germany only) The entity's commercial register number (_Handelsregisternummer_) in the German Commercial Register, if available.
    
</dd>
</dl>

<dl>
<dd>

**registration_authority:** `typing.Optional[str]` — (Germany only) The name of the local district court (_Amtsgericht_) where the entity is registered. Required if `registration_number` is provided.
    
</dd>
</dl>

<dl>
<dd>

**organization:** `typing.Optional[OptionalOrganizationSchema]` — A set of meta data describing the organization
    
</dd>
</dl>

<dl>
<dd>

**individual:** `typing.Optional[OptionalIndividualSchema]` — A set of meta data describing the individual
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entity_users.get_by_id(entity_user_id='entity_user_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entity_users.delete_by_id(entity_user_id='entity_user_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.entity_users.update_by_id(entity_user_id='entity_user_id', )

```
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

**email:** `typing.Optional[str]` — An entity user business email
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — First name
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — Last name
    
</dd>
</dl>

<dl>
<dd>

**login:** `typing.Optional[str]` — Login
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — An entity user phone number in the international format
    
</dd>
</dl>

<dl>
<dd>

**role_id:** `typing.Optional[str]` — UUID of the role assigned to this entity user
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Title
    
</dd>
</dl>

<dl>
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.events.get_by_id(event_id='event_id', )

```
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.files.upload(file_type="ocr_results", )

```
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
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.files.get_by_id(file_id='file_id', )

```
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.files.delete(file_id='file_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**order:** `typing.Optional[OrderEnum]` — Order by
    
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

**sort:** `typing.Optional[FinancingInvoiceCursorFields]` — Allowed sort fields
    
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

**type_in:** `typing.Optional[typing.Union[FinancingInvoiceType, typing.Sequence[FinancingInvoiceType]]]` — List of invoice types. 
    
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
from monite import Monite
from monite import FinancingPushInvoicesRequestInvoice
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.financing.post_financing_invoices(invoices=[FinancingPushInvoicesRequestInvoice(id='id', type="payable", )], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**order:** `typing.Optional[OrderEnum]` — Order by
    
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

**sort:** `typing.Optional[CustomTemplatesCursorFields]` — Allowed sort fields
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[DocumentObjectTypeRequestEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**type_in:** `typing.Optional[typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]]` 
    
</dd>
</dl>

<dl>
<dd>

**type_not_in:** `typing.Optional[typing.Union[DocumentObjectTypeRequestEnum, typing.Sequence[DocumentObjectTypeRequestEnum]]]` 
    
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mail_templates.create(body_template='body_template', name='name', subject_template='subject_template', type="receivables_quote", )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mail_templates.preview(body='body', document_type="receivables_quote", language_code="ab", subject='subject', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mail_templates.get_by_id(template_id='template_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mail_templates.delete_by_id(template_id='template_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mail_templates.update_by_id(template_id='template_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mail_templates.make_default_by_id(template_id='template_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mailbox_domains.create(domain='domain', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mailbox_domains.delete_by_id(domain_id='domain_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mailbox_domains.verify_by_id(domain_id='domain_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mailboxes.create(mailbox_domain_id='mailbox_domain_id', mailbox_name='mailbox_name', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mailboxes.search(entity_ids=['entity_ids'], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.mailboxes.delete_by_id(mailbox_id='mailbox_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.measure_units.create(name='name', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.measure_units.get_by_id(unit_id='unit_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.measure_units.delete_by_id(unit_id='unit_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.measure_units.update_by_id(unit_id='unit_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.ocr.post_ocr_tasks(file_url='file_url', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.ocr.get_ocr_tasks_id(task_id='task_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.overdue_reminders.create(name='name', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.overdue_reminders.get_by_id(overdue_reminder_id='overdue_reminder_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.overdue_reminders.delete_by_id(overdue_reminder_id='overdue_reminder_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.overdue_reminders.update_by_id(overdue_reminder_id='overdue_reminder_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**status_in:** `typing.Optional[typing.Union[PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status_not_in:** `typing.Optional[typing.Union[PayableCreditNoteStateEnum, typing.Sequence[PayableCreditNoteStateEnum]]]` 
    
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes(document_id='CN-2287', issued_at='2024-01-15', )

```
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

Upload an incoming credit note (payable) in PDF, PNG, JPEG, or TIFF format and scan its contents. The maximum file size is 10MB.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.put_payable_credit_notes_validations(required_fields=["currency"], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.get_payable_credit_notes_id(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.delete_payable_credit_notes_id(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.patch_payable_credit_notes_id(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes_id_approve(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes_id_cancel(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes_id_cancel_ocr(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.get_payable_credit_notes_id_line_items(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes_id_line_items(credit_note_id='credit_note_id', )

```
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
from monite import Monite
from monite import CreditNoteLineItemCreateRequest
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.put_payable_credit_notes_id_line_items(credit_note_id='credit_note_id', data=[CreditNoteLineItemCreateRequest()], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.get_payable_credit_notes_id_line_items_id(credit_note_id='credit_note_id', line_item_id='line_item_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.delete_payable_credit_notes_id_line_items_id(credit_note_id='credit_note_id', line_item_id='line_item_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.patch_payable_credit_notes_id_line_items_id(credit_note_id='credit_note_id', line_item_id='line_item_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes_id_reject(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.post_payable_credit_notes_id_submit_for_approval(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.credit_notes.get_payable_credit_notes_id_validate(credit_note_id='credit_note_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
from monite import Monite
from monite import PurchaseOrderItem
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.purchase_orders.create(counterpart_id='counterpart_id', currency="AED", items=[PurchaseOrderItem(currency="AED", name='name', price=1, quantity=1, unit='unit', vat_rate=1, )], message='message', valid_for_days=1, )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.purchase_orders.get_by_id(purchase_order_id='purchase_order_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.purchase_orders.delete_by_id(purchase_order_id='purchase_order_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.purchase_orders.update_by_id(purchase_order_id='purchase_order_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.purchase_orders.preview_by_id(purchase_order_id='purchase_order_id', body_text='body_text', subject_text='subject_text', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.purchase_orders.send_by_id(purchase_order_id='purchase_order_id', body_text='body_text', subject_text='subject_text', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**status_in:** `typing.Optional[typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]]` 

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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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

**status_in:** `typing.Optional[typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]]` 

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

Upload an incoming invoice (payable) in PDF, PNG, JPEG, or TIFF format and scan its contents. The maximum file size is 10MB.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.update_validations(required_fields=["currency"], )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.get_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.delete_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.update_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.approve_payment_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.attach_file_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.cancel_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.post_payables_id_cancel_ocr(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.mark_as_paid_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.mark_as_partially_paid_by_id(payable_id='payable_id', amount_paid=1, )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.reject_by_id(payable_id='payable_id', )

```
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

Reset payable state from rejected to new.
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.reopen_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.submit_for_approval_by_id(payable_id='payable_id', )

```
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
client = Monite(monite_version="YOUR_MONITE_VERSION", monite_entity_id="YOUR_MONITE_ENTITY_ID", token="YOUR_TOKEN", )
client.payables.validate_by_id(payable_id='payable_id', )

```
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
