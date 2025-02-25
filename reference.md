# Reference
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

**sort:** `typing.Optional[ApprovalPolicyCursorFields]` — Allowed sort fields
    
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
    description="description",
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

**description:** `str` — A brief description of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.Sequence[ApprovalPolicyCreateScriptItem]` — A list of JSON objects that represents the approval policy script. The script contains the logic that determines whether an action should be sent to approval. This field is required, and it should contain at least one script object.
    
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

**name:** `typing.Optional[str]` — The name of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of the approval policy.
    
</dd>
</dl>

<dl>
<dd>

**script:** `typing.Optional[typing.Sequence[ApprovalPolicyUpdateScriptItem]]` — A list of JSON objects that represents the approval policy script. The script contains the logic that determines whether an action should be sent to approval. This field is required, and it should contain at least one script object.
    
</dd>
</dl>

<dl>
<dd>

**trigger:** `typing.Optional[ApprovalPolicyUpdateTrigger]` — A JSON object that represents the trigger for the approval policy. The trigger specifies the event that will trigger the policy to be evaluated.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ApprovalPolicyStatus]` — A string that represents the current status of the approval policy.
    
</dd>
</dl>

<dl>
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

## Audit logs
<details><summary><code>client.audit_logs.<a href="src/monite/audit_logs/client.py">get</a>(...)</code></summary>
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
client.audit_logs.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**pagination_token:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**path_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LogTypeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[LogMethodEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_code:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**page_num:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audit_logs.<a href="src/monite/audit_logs/client.py">get_by_id</a>(...)</code></summary>
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
client.audit_logs.get_by_id(
    log_id="log_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**log_id:** `str` 
    
</dd>
</dl>

<dl>
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

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.access_tokens.create(
    client_id="client_id",
    client_secret="client_secret",
    grant_type="client_credentials",
)

```
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

## Entity bank account verifications
<details><summary><code>client.entity_bank_account_verifications.<a href="src/monite/entity_bank_account_verifications/client.py">get_bank_accounts_id_verifications</a>(...)</code></summary>
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
client.entity_bank_account_verifications.get_bank_accounts_id_verifications(
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

**sort:** `typing.Optional[CounterpartCursorFields]` — Allowed sort fields
    
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
    CounterpartCreatePayload_Individual,
    CounterpartIndividualCreatePayload,
    Monite,
)

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.counterparts.create(
    request=CounterpartCreatePayload_Individual(
        individual=CounterpartIndividualCreatePayload(
            address=CounterpartAddress(
                city="Berlin",
                country="AF",
                line1="Flughafenstrasse 52",
                postal_code="10115",
            ),
            first_name="Adnan",
            is_customer=True,
            is_vendor=True,
            last_name="Singh",
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import ExportObjectSchema_Receivable, Monite

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
        ExportObjectSchema_Receivable(
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

**sort:** `typing.Optional[EntityCursorFields]` — Allowed sort fields
    
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

**phone:** `typing.Optional[str]` — A phone number of the entity
    
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

**phone:** `typing.Optional[str]` — A phone number of the entity
    
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

**phone:** `typing.Optional[str]` — A phone number of the entity
    
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

#### 🔌 Usage

<dl>
<dd>

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

**language:** `typing.Optional[LanguageCodeEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencySettings]` 
    
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

**payment_priority:** `typing.Optional[PaymentPriorityEnum]` — Payment preferences for entity to automate calculating suggested payment date basing on payment terms and entity preferences
    
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

**quote_signature_required:** `typing.Optional[bool]` — Sets the default behavior of whether a signature is required to accept quotes
    
</dd>
</dl>

<dl>
<dd>

**generate_paid_invoice_pdf:** `typing.Optional[bool]` — If enabled, the paid invoice's PDF will be in a new layout set by the user
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[EntityUserCursorFields]` — Allowed sort fields
    
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
    first_name="Andrey",
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

**phone:** `typing.Optional[str]` — A phone number of the entity
    
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

Get events for a given entity.
</dd>
</dl>
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

**sort:** `typing.Optional[EventCursorFields]` — Allowed sort fields
    
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

Get event by ID.
</dd>
</dl>
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

**event_id:** `str` 
    
</dd>
</dl>

<dl>
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
    
</dd>
</dl>

<dl>
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
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

**domain:** `str` 
    
</dd>
</dl>

<dl>
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
)

```
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

**sort:** `typing.Optional[PurchaseOrderCursorFields]` — Allowed sort fields
    
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
https://docs.monite.com/docs/currencies#minor-units), currency, vendor information, and other details)
stored somewhere as individual attributes, you can create a payable with these attributes by calling [POST
/payables](https://docs.monite.com/reference/post_payables) and providing the [base64-encoded](
https://en.wikipedia.org/wiki/Base64) contents of the original invoice file in the field `base64_encoded_file`.

A payable is a financial document given by an entity`s supplier itemizing the purchase of a good or a service and
demanding payment.

The `file_name` field is optional. If omitted, it defaults to “default_file_name”. If the settings are configured
to automatically set `suggested_payment_term`, this object can be omitted from the request body.

The `id` generated for this payable can be used in other API calls to update the data of this payable or trigger [
status transitions](https://docs.monite.com/docs/payable-status-transitions), for example. essential data
fields to move from `draft` to `new`

Related guide: [Create a payable from data](https://docs.monite.com/docs/collect-payables#create-a-payable-from-data)

See also:


[Automatic calculation of due date](https://docs.monite.com/docs/collect-payables#automatic-calculation-of-due-date)

[Suggested payment date](https://docs.monite.com/docs/collect-payables#suggested-payment-date)

[Attach file](https://docs.monite.com/docs/collect-payables#attach-file)

[Collect payables by email](https://docs.monite.com/docs/collect-payables#send-payables-by-email)

[Manage line items](https://docs.monite.com/docs/manage-line-items)
</dd>
</dl>
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

**sort:** `typing.Optional[PayableCursorFields]` — Allowed sort fields
    
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

**status:** `typing.Optional[PayableStateEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

**amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
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

**search_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` 
    
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

**was_created_by_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_of_payable_data:** `typing.Optional[SourceOfPayableDataEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**ocr_status:** `typing.Optional[OcrStatusEnum]` 
    
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

**project_id:** `typing.Optional[str]` — Search for a payable by the identifier of the project associated with it.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Search for a payable by the identifiers of the tags associated with it.
    
</dd>
</dl>

<dl>
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

A newly created payable has the the `draft` [status](https://docs.monite.com/docs/payables-lifecycle).
</dd>
</dl>
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

**currency:** `typing.Optional[CurrencyEnum]` — The [currency code](https://docs.monite.com/docs/currencies) of the currency used in the payable.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — An arbitrary description of this payable.
    
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

**subtotal:** `typing.Optional[int]` — The subtotal amount to be paid, in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
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

**tax_amount:** `typing.Optional[int]` — Tax amount in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — The total amount to be paid, in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
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
</dd>
</dl>
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

**status:** `typing.Optional[PayableStateEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**status_in:** `typing.Optional[
    typing.Union[PayableStateEnum, typing.Sequence[PayableStateEnum]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
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

**amount:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_gt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_lt:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_gte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**amount_lte:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` 
    
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

**search_text:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**due_date:** `typing.Optional[str]` 
    
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

**was_created_by_user_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**source_of_payable_data:** `typing.Optional[SourceOfPayableDataEnum]` 
    
</dd>
</dl>

<dl>
<dd>

**ocr_status:** `typing.Optional[OcrStatusEnum]` 
    
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

**project_id:** `typing.Optional[str]` — Search for a payable by the identifier of the project associated with it.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Search for a payable by the identifiers of the tags associated with it.
    
</dd>
</dl>

<dl>
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

**currency:** `typing.Optional[CurrencyEnum]` — The [currency code](https://docs.monite.com/docs/currencies) of the currency used in the payable.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — An arbitrary description of this payable.
    
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

**subtotal:** `typing.Optional[int]` — The subtotal amount to be paid, in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
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

**tax_amount:** `typing.Optional[int]` — Tax amount in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**total_amount:** `typing.Optional[int]` — The total amount to be paid, in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
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

Related guide: [Mark a payable as paid](https://docs.monite.com/docs/payable-status-transitions#mark-as-paid)

See also:

[Payables lifecycle](https://docs.monite.com/docs/payables-lifecycle)

[Payables status transitions](https://docs.monite.com/docs/collect-payables#suggested-payment-date)
</dd>
</dl>
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

Related guide: [Mark a payable as partially paid](https://docs.monite.com/docs/payable-status-transitions#mark-as-partially-paid)

See also:

[Payables lifecycle](https://docs.monite.com/docs/payables-lifecycle)

[Payables status transitions](https://docs.monite.com/docs/collect-payables#suggested-payment-date)

[Mark a payable as paid](https://docs.monite.com/docs/payable-status-transitions#mark-as-paid)
</dd>
</dl>
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

**sort:** `typing.Optional[PaymentIntentCursorFields]` — Allowed sort fields
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` — ID of a payable or receivable invoice. If provided, returns only payment intents associated with the specified invoice.
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import Monite, PaymentAccountObject

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_links.create(
    payment_methods=["sepa_credit"],
    recipient=PaymentAccountObject(
        id="id",
        type="entity",
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

**payment_methods:** `typing.Sequence[MoniteAllPaymentMethodsTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**recipient:** `PaymentAccountObject` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `typing.Optional[int]` — The payment amount in [minor units](https://docs.monite.com/docs/currencies#minor-units). Required if `object` is not specified.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyEnum]` — The payment currency. Required if `object` is not specified.
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**invoice:** `typing.Optional[Invoice]` — An object containing information about the invoice being paid. Used only if `object` is not specified.
    
</dd>
</dl>

<dl>
<dd>

**object:** `typing.Optional[PaymentObject]` — If the invoice being paid is a payable or receivable stored in Monite, provide the `object` object containing the invoice type and ID. Otherwise, use the `amount`, `currency`, `payment_reference`, and (optionally) `invoice` fields to specify the invoice-related data.
    
</dd>
</dl>

<dl>
<dd>

**payment_reference:** `typing.Optional[str]` — A payment reference number that the recipient can use to identify the payer or purpose of the transaction. Required if `object` is not specified.
    
</dd>
</dl>

<dl>
<dd>

**return_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[PaymentRecordCursorFields]` — Allowed sort fields
    
</dd>
</dl>

<dl>
<dd>

**is_external:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**object_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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
import datetime

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
    paid_at=datetime.datetime.fromisoformat(
        "2024-01-15 09:30:00+00:00",
    ),
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

**amount:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` 
    
</dd>
</dl>

<dl>
<dd>

**object:** `PaymentRecordObjectRequest` 
    
</dd>
</dl>

<dl>
<dd>

**paid_at:** `dt.datetime` 
    
</dd>
</dl>

<dl>
<dd>

**payment_intent_id:** `str` 
    
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
from monite import Monite, PaymentTerm

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.payment_terms.create(
    name="name",
    term_final=PaymentTerm(
        number_of_days=1,
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

**term_final:** `PaymentTerm` — The final tier of the payment term. Defines the invoice due date.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**term1:** `typing.Optional[PaymentTermDiscount]` — The first tier of the payment term. Represents the terms of the first early discount.
    
</dd>
</dl>

<dl>
<dd>

**term2:** `typing.Optional[PaymentTermDiscount]` — The second tier of the payment term. Defines the terms of the second early discount.
    
</dd>
</dl>

<dl>
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

**term1:** `typing.Optional[PaymentTermDiscount]` — The first tier of the payment term. Represents the terms of the first early discount.
    
</dd>
</dl>

<dl>
<dd>

**term2:** `typing.Optional[PaymentTermDiscount]` — The second tier of the payment term. Defines the terms of the second early discount.
    
</dd>
</dl>

<dl>
<dd>

**term_final:** `typing.Optional[PaymentTerm]` — The final tier of the payment term. Defines the invoice due date.
    
</dd>
</dl>

<dl>
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

**order:** `typing.Optional[OrderEnum3]` — Order by
    
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

**sort:** `typing.Optional[ProductCursorFields]` — Allowed sort fields
    
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

**sort:** `typing.Optional[ProjectCursorFields]` — Allowed sort fields
    
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

**code:** `typing.Optional[str]` — Project code
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Project color
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of project
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Project end date
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent project ID
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Project metadata
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Project start date
    
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

**code:** `typing.Optional[str]` — Project code
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Project color
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of project
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[str]` — Project end date
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — The project name.
    
</dd>
</dl>

<dl>
<dd>

**parent_id:** `typing.Optional[str]` — Parent project ID
    
</dd>
</dl>

<dl>
<dd>

**partner_metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Project metadata
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[str]` — Project start date
    
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

**order:** `typing.Optional[OrderEnum2]` — Sort order (ascending by default). Typically used together with the `sort` parameter.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 

The number of items (0 .. 100) to return in a single page of the response. The response may contain fewer items if it is the last or only page. 

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

**status:** `typing.Optional[ReceivablesGetRequestStatus]` 
    
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

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from monite import LineItem, Monite, ReceivableFacadeCreateQuotePayload

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.receivables.create(
    request=ReceivableFacadeCreateQuotePayload(
        counterpart_billing_address_id="counterpart_billing_address_id",
        counterpart_id="counterpart_id",
        currency="AED",
        line_items=[
            LineItem(
                quantity=1.1,
            )
        ],
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

#### 🔌 Usage

<dl>
<dd>

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

#### 🔌 Usage

<dl>
<dd>

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

**signature:** `typing.Optional[Signature]` — A digital signature, if required for quote acceptance
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

<details><summary><code>client.receivables.<a href="src/monite/receivables/client.py">decline_by_id</a>(...)</code></summary>
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

#### 🔌 Usage

<dl>
<dd>

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

**receivable_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrderEnum3]` — Order by
    
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

**sort:** `typing.Optional[ReceivableHistoryCursorFields]` — Allowed sort fields
    
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
    
</dd>
</dl>

<dl>
<dd>

**entity_user_id_in:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lt:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_gte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**timestamp_lte:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

**receivable_history_id:** `str` 
    
</dd>
</dl>

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

**order:** `typing.Optional[OrderEnum3]` — Order by
    
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

**sort:** `typing.Optional[ReceivableMailCursorFields]` — Allowed sort fields
    
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

#### 🔌 Usage

<dl>
<dd>

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

#### 🔌 Usage

<dl>
<dd>

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

**language:** `typing.Optional[str]` — Lowercase ISO code of language
    
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
    day_of_month="first_day",
    end_month=1,
    end_year=1,
    invoice_id="invoice_id",
    start_month=1,
    start_year=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**day_of_month:** `DayOfMonth` 
    
</dd>
</dl>

<dl>
<dd>

**end_month:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**end_year:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_month:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**start_year:** `int` 
    
</dd>
</dl>

<dl>
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

**day_of_month:** `typing.Optional[DayOfMonth]` 
    
</dd>
</dl>

<dl>
<dd>

**end_month:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**end_year:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[RoleCursorFields]` — Allowed sort fields
    
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
from monite import BizObjectsSchema, Monite

client = Monite(
    monite_version="YOUR_MONITE_VERSION",
    monite_entity_id="YOUR_MONITE_ENTITY_ID",
    token="YOUR_TOKEN",
)
client.roles.create(
    name="name",
    permissions=BizObjectsSchema(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Role name
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `BizObjectsSchema` — Access permissions
    
</dd>
</dl>

<dl>
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

**name:** `typing.Optional[str]` — Role name
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[BizObjectsSchema]` — Access permissions
    
</dd>
</dl>

<dl>
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

Retrieve all settings for this partner.
</dd>
</dl>
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

**accounting:** `typing.Optional[AccountingSettingsPayload]` — Settings for the accounting module.
    
</dd>
</dl>

<dl>
<dd>

**api_version:** `typing.Optional[ApiVersion]` — Default API version for partner.
    
</dd>
</dl>

<dl>
<dd>

**commercial_conditions:** `typing.Optional[typing.Sequence[str]]` — Commercial conditions for receivables.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencySettings]` — Custom currency exchange rates.
    
</dd>
</dl>

<dl>
<dd>

**default_role:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — A default role to provision upon new entity creation.
    
</dd>
</dl>

<dl>
<dd>

**einvoicing:** `typing.Optional[EInvoicingSettingsPayload]` — Settings for the e-invoicing module.
    
</dd>
</dl>

<dl>
<dd>

**mail:** `typing.Optional[MailSettingsPayload]` — Settings for email and mailboxes.
    
</dd>
</dl>

<dl>
<dd>

**payable:** `typing.Optional[PayableSettingsPayload]` — Settings for the payables module.
    
</dd>
</dl>

<dl>
<dd>

**payments:** `typing.Optional[PaymentsSettingsPayload]` — Settings for the payments module.
    
</dd>
</dl>

<dl>
<dd>

**receivable:** `typing.Optional[ReceivableSettingsPayload]` — Settings for the receivables module.
    
</dd>
</dl>

<dl>
<dd>

**units:** `typing.Optional[typing.Sequence[Unit]]` — Measurement units.
    
</dd>
</dl>

<dl>
<dd>

**website:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[TagCursorFields]` — Allowed sort fields
    
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

**document_type:** `typing.Optional[DocumentTypeEnum]` 
    
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

**document_type:** `DocumentTypeEnum` 
    
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

#### 🔌 Usage

<dl>
<dd>

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

**counterpart_address_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**counterpart_vat_id_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**entity_vat_id_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**product_type:** `typing.Optional[ProductServiceTypeEnum]` 
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

**sort:** `typing.Optional[WebhookDeliveryCursorFields]` — Allowed sort fields
    
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

#### 🔌 Usage

<dl>
<dd>

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

**sort:** `typing.Optional[WebhookSubscriptionCursorFields]` — Allowed sort fields
    
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

<details><summary><code>client.webhook_subscriptions.<a href="src/monite/webhook_subscriptions/client.py">create</a>(...)</code></summary>
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
client.webhook_subscriptions.create(
    object_type="account",
    url="url",
)

```
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
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

**webhook_subscription_id:** `str` 
    
</dd>
</dl>

<dl>
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

**webhook_subscription_id:** `str` 
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

**webhook_subscription_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**object_type:** `typing.Optional[WebhookObjectType]` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
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

**webhook_subscription_id:** `str` 
    
</dd>
</dl>

<dl>
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

**webhook_subscription_id:** `str` 
    
</dd>
</dl>

<dl>
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

#### 🔌 Usage

<dl>
<dd>

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

**webhook_subscription_id:** `str` 
    
</dd>
</dl>

<dl>
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

<details><summary><code>client.accounting.connections.<a href="src/monite/accounting/connections/client.py">create</a>(...)</code></summary>
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

**platform:** `typing.Optional[Platform]` 
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[SyncRecordCursorFields]` — Allowed sort fields
    
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

**sort:** `typing.Optional[TaxRateAccountCursorFields]` — Allowed sort fields
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[LedgerAccountCursorFields]` — Allowed sort fields
    
</dd>
</dl>

<dl>
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

**sort:** `typing.Optional[ExportSettingCursorFields]` — Allowed sort fields
    
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

Add a new bank account for the specified entity.

The minimum required fields are `currency` and `country`. Other required fields depend on the currency:

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

**country:** `AllowedCountries` — The country in which the bank account is registered, repsesented as a two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    
</dd>
</dl>

<dl>
<dd>

**currency:** `CurrencyEnum` — The currency of the bank account, represented as a three-letter ISO [currency code](https://docs.monite.com/docs/currencies).
    
</dd>
</dl>

<dl>
<dd>

**account_holder_name:** `typing.Optional[str]` — The name of the person or business that owns this bank account. Required if the account currency is GBP or USD.
    
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

**bic:** `typing.Optional[str]` — The SWIFT/BIC code of the bank.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — User-defined name of this bank account, such as 'Primary account' or 'Savings account'.
    
</dd>
</dl>

<dl>
<dd>

**iban:** `typing.Optional[str]` — The IBAN of the bank account. Required if the account currency is EUR.
    
</dd>
</dl>

<dl>
<dd>

**is_default_for_currency:** `typing.Optional[bool]` — If set to `true` or if this is the first bank account added for the given currency, this account becomes the default one for its currency.
    
</dd>
</dl>

<dl>
<dd>

**routing_number:** `typing.Optional[str]` — The bank's routing transit number (RTN). Required if the account currency is USD. US routing numbers consist of 9 digits.
    
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

**business_profile:** `typing.Optional[BusinessProfile]` — Business information about the entity.
    
</dd>
</dl>

<dl>
<dd>

**ownership_declaration:** `typing.Optional[OwnershipDeclaration]` — Used to attest that the beneficial owner information provided is both current and correct.
    
</dd>
</dl>

<dl>
<dd>

**tos_acceptance:** `typing.Optional[TermsOfServiceAcceptance]` — Details on the entity's acceptance of the service agreement.
    
</dd>
</dl>

<dl>
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
)

```
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

**payment_methods:** `typing.Optional[typing.Sequence[MoniteAllPaymentMethodsTypes]]` — Deprecated. Use payment_methods_receive instead.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods_receive:** `typing.Optional[typing.Sequence[MoniteAllPaymentMethodsTypes]]` — Enable payment methods to receive money.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods_send:** `typing.Optional[typing.Sequence[MoniteAllPaymentMethodsTypes]]` — Enable payment methods to send money.
    
</dd>
</dl>

<dl>
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
    first_name="first_name",
    last_name="last_name",
    email="email",
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

**email:** `str` — The person's email address
    
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

**date_of_birth:** `typing.Optional[str]` — The person's date of birth
    
</dd>
</dl>

<dl>
<dd>

**phone:** `typing.Optional[str]` — The person's phone number
    
</dd>
</dl>

<dl>
<dd>

**id_number:** `typing.Optional[str]` — The person's ID number, as appropriate for their country
    
</dd>
</dl>

<dl>
<dd>

**ssn_last4:** `typing.Optional[str]` — The last four digits of the person's Social Security number
    
</dd>
</dl>

<dl>
<dd>

**citizenship:** `typing.Optional[AllowedCountries]` — Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.
    
</dd>
</dl>

<dl>
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

**date_of_birth:** `typing.Optional[str]` — The person's date of birth
    
</dd>
</dl>

<dl>
<dd>

**first_name:** `typing.Optional[str]` — The person's first name
    
</dd>
</dl>

<dl>
<dd>

**last_name:** `typing.Optional[str]` — The person's last name
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — The person's email address
    
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

**id_number:** `typing.Optional[str]` — The person's ID number, as appropriate for their country
    
</dd>
</dl>

<dl>
<dd>

**ssn_last4:** `typing.Optional[str]` — The last four digits of the person's Social Security number
    
</dd>
</dl>

<dl>
<dd>

**citizenship:** `typing.Optional[AllowedCountries]` — Required for persons of US entities. The country of the person's citizenship, as a two-letter country code (ISO 3166-1 alpha-2). In case of dual or multiple citizenship, specify any.
    
</dd>
</dl>

<dl>
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
Related guide: [List all payable line items](https://docs.monite.com/docs/manage-line-items#list-all-line-items-of-a-payable)

See also:

[Manage line items](https://docs.monite.com/docs/manage-line-items)

[Collect payables](https://docs.monite.com/docs/collect-payables)
</dd>
</dl>
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

**sort:** `typing.Optional[LineItemCursorFields]` — Allowed sort fields
    
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

Related guide: [Add line items to a payable](https://docs.monite.com/docs/manage-line-items#add-line-items-to-a-payable)

See also:

[Manage line items](https://docs.monite.com/docs/manage-line-items)

[Collect payables](https://docs.monite.com/docs/collect-payables)
</dd>
</dl>
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

**tax:** `typing.Optional[int]` — VAT rate in percent [minor units](https://docs.monite.com/docs/currencies#minor-units). Example: 12.5% is 1250.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` — The unit of the product
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[int]` — The unit price of the product, in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
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

Related guide: [Replace all line items](https://docs.monite.com/docs/manage-line-items#replace-all-line-items)

See also:

[Manage line items](https://docs.monite.com/docs/manage-line-items)

[Collect payables](https://docs.monite.com/docs/collect-payables)
</dd>
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

Related guide: [Retrieve a line item](https://docs.monite.com/docs/manage-line-items#retrieve-a-line-item)

See also:

[Manage line items](https://docs.monite.com/docs/manage-line-items)

[Collect payables](https://docs.monite.com/docs/collect-payables)
</dd>
</dl>
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

Related guide: [Remove a line item](https://docs.monite.com/docs/manage-line-items#remove-a-line-item)

See also:

[Manage line items](https://docs.monite.com/docs/manage-line-items)

[Collect payables](https://docs.monite.com/docs/collect-payables)
</dd>
</dl>
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

Related guide: [Update a line item](https://docs.monite.com/docs/manage-line-items#update-a-line-item)

See also:

[Manage line items](https://docs.monite.com/docs/manage-line-items)

[Collect payables](https://docs.monite.com/docs/collect-payables)
</dd>
</dl>
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

**tax:** `typing.Optional[int]` — VAT rate in percent [minor units](https://docs.monite.com/docs/currencies#minor-units). Example: 12.5% is 1250.
    
</dd>
</dl>

<dl>
<dd>

**unit:** `typing.Optional[str]` — The unit of the product
    
</dd>
</dl>

<dl>
<dd>

**unit_price:** `typing.Optional[int]` — The unit price of the product, in [minor units](https://docs.monite.com/docs/currencies#minor-units). For example, $12.50 is represented as 1250.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

