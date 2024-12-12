# This file was auto-generated by Fern from our API Definition.

import typing
from .environment import MoniteEnvironment
import httpx
from .core.client_wrapper import SyncClientWrapper
from .analytics.client import AnalyticsClient
from .approval_policies.client import ApprovalPoliciesClient
from .approval_requests.client import ApprovalRequestsClient
from .audit_logs.client import AuditLogsClient
from .access_tokens.client import AccessTokensClient
from .batch_payments.client import BatchPaymentsClient
from .comments.client import CommentsClient
from .counterparts.client import CounterpartsClient
from .data_exports.client import DataExportsClient
from .pdf_templates.client import PdfTemplatesClient
from .entities.client import EntitiesClient
from .entity_users.client import EntityUsersClient
from .events.client import EventsClient
from .files.client import FilesClient
from .financing.client import FinancingClient
from .mail_templates.client import MailTemplatesClient
from .mailbox_domains.client import MailboxDomainsClient
from .mailboxes.client import MailboxesClient
from .measure_units.client import MeasureUnitsClient
from .onboarding_links.client import OnboardingLinksClient
from .overdue_reminders.client import OverdueRemindersClient
from .credit_notes.client import CreditNotesClient
from .purchase_orders.client import PurchaseOrdersClient
from .payables.client import PayablesClient
from .payment_intents.client import PaymentIntentsClient
from .payment_links.client import PaymentLinksClient
from .payment_records.client import PaymentRecordsClient
from .payment_reminders.client import PaymentRemindersClient
from .payment_terms.client import PaymentTermsClient
from .products.client import ProductsClient
from .projects.client import ProjectsClient
from .receivables.client import ReceivablesClient
from .recurrences.client import RecurrencesClient
from .roles.client import RolesClient
from .partner_settings.client import PartnerSettingsClient
from .tags.client import TagsClient
from .text_templates.client import TextTemplatesClient
from .vat_rates.client import VatRatesClient
from .webhook_deliveries.client import WebhookDeliveriesClient
from .webhook_subscriptions.client import WebhookSubscriptionsClient
from .accounting.client import AccountingClient
from .core.client_wrapper import AsyncClientWrapper
from .analytics.client import AsyncAnalyticsClient
from .approval_policies.client import AsyncApprovalPoliciesClient
from .approval_requests.client import AsyncApprovalRequestsClient
from .audit_logs.client import AsyncAuditLogsClient
from .access_tokens.client import AsyncAccessTokensClient
from .batch_payments.client import AsyncBatchPaymentsClient
from .comments.client import AsyncCommentsClient
from .counterparts.client import AsyncCounterpartsClient
from .data_exports.client import AsyncDataExportsClient
from .pdf_templates.client import AsyncPdfTemplatesClient
from .entities.client import AsyncEntitiesClient
from .entity_users.client import AsyncEntityUsersClient
from .events.client import AsyncEventsClient
from .files.client import AsyncFilesClient
from .financing.client import AsyncFinancingClient
from .mail_templates.client import AsyncMailTemplatesClient
from .mailbox_domains.client import AsyncMailboxDomainsClient
from .mailboxes.client import AsyncMailboxesClient
from .measure_units.client import AsyncMeasureUnitsClient
from .onboarding_links.client import AsyncOnboardingLinksClient
from .overdue_reminders.client import AsyncOverdueRemindersClient
from .credit_notes.client import AsyncCreditNotesClient
from .purchase_orders.client import AsyncPurchaseOrdersClient
from .payables.client import AsyncPayablesClient
from .payment_intents.client import AsyncPaymentIntentsClient
from .payment_links.client import AsyncPaymentLinksClient
from .payment_records.client import AsyncPaymentRecordsClient
from .payment_reminders.client import AsyncPaymentRemindersClient
from .payment_terms.client import AsyncPaymentTermsClient
from .products.client import AsyncProductsClient
from .projects.client import AsyncProjectsClient
from .receivables.client import AsyncReceivablesClient
from .recurrences.client import AsyncRecurrencesClient
from .roles.client import AsyncRolesClient
from .partner_settings.client import AsyncPartnerSettingsClient
from .tags.client import AsyncTagsClient
from .text_templates.client import AsyncTextTemplatesClient
from .vat_rates.client import AsyncVatRatesClient
from .webhook_deliveries.client import AsyncWebhookDeliveriesClient
from .webhook_subscriptions.client import AsyncWebhookSubscriptionsClient
from .accounting.client import AsyncAccountingClient


class Monite:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MoniteEnvironment
        The environment to use for requests from the client. from .environment import MoniteEnvironment



        Defaults to MoniteEnvironment.SANDBOX



    monite_version : str
    monite_entity_id : typing.Optional[str]
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from monite import Monite

    client = Monite(
        monite_version="YOUR_MONITE_VERSION",
        monite_entity_id="YOUR_MONITE_ENTITY_ID",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MoniteEnvironment = MoniteEnvironment.SANDBOX,
        monite_version: str,
        monite_entity_id: typing.Optional[str] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            monite_version=monite_version,
            monite_entity_id=monite_entity_id,
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.analytics = AnalyticsClient(client_wrapper=self._client_wrapper)
        self.approval_policies = ApprovalPoliciesClient(client_wrapper=self._client_wrapper)
        self.approval_requests = ApprovalRequestsClient(client_wrapper=self._client_wrapper)
        self.audit_logs = AuditLogsClient(client_wrapper=self._client_wrapper)
        self.access_tokens = AccessTokensClient(client_wrapper=self._client_wrapper)
        self.batch_payments = BatchPaymentsClient(client_wrapper=self._client_wrapper)
        self.comments = CommentsClient(client_wrapper=self._client_wrapper)
        self.counterparts = CounterpartsClient(client_wrapper=self._client_wrapper)
        self.data_exports = DataExportsClient(client_wrapper=self._client_wrapper)
        self.pdf_templates = PdfTemplatesClient(client_wrapper=self._client_wrapper)
        self.entities = EntitiesClient(client_wrapper=self._client_wrapper)
        self.entity_users = EntityUsersClient(client_wrapper=self._client_wrapper)
        self.events = EventsClient(client_wrapper=self._client_wrapper)
        self.files = FilesClient(client_wrapper=self._client_wrapper)
        self.financing = FinancingClient(client_wrapper=self._client_wrapper)
        self.mail_templates = MailTemplatesClient(client_wrapper=self._client_wrapper)
        self.mailbox_domains = MailboxDomainsClient(client_wrapper=self._client_wrapper)
        self.mailboxes = MailboxesClient(client_wrapper=self._client_wrapper)
        self.measure_units = MeasureUnitsClient(client_wrapper=self._client_wrapper)
        self.onboarding_links = OnboardingLinksClient(client_wrapper=self._client_wrapper)
        self.overdue_reminders = OverdueRemindersClient(client_wrapper=self._client_wrapper)
        self.credit_notes = CreditNotesClient(client_wrapper=self._client_wrapper)
        self.purchase_orders = PurchaseOrdersClient(client_wrapper=self._client_wrapper)
        self.payables = PayablesClient(client_wrapper=self._client_wrapper)
        self.payment_intents = PaymentIntentsClient(client_wrapper=self._client_wrapper)
        self.payment_links = PaymentLinksClient(client_wrapper=self._client_wrapper)
        self.payment_records = PaymentRecordsClient(client_wrapper=self._client_wrapper)
        self.payment_reminders = PaymentRemindersClient(client_wrapper=self._client_wrapper)
        self.payment_terms = PaymentTermsClient(client_wrapper=self._client_wrapper)
        self.products = ProductsClient(client_wrapper=self._client_wrapper)
        self.projects = ProjectsClient(client_wrapper=self._client_wrapper)
        self.receivables = ReceivablesClient(client_wrapper=self._client_wrapper)
        self.recurrences = RecurrencesClient(client_wrapper=self._client_wrapper)
        self.roles = RolesClient(client_wrapper=self._client_wrapper)
        self.partner_settings = PartnerSettingsClient(client_wrapper=self._client_wrapper)
        self.tags = TagsClient(client_wrapper=self._client_wrapper)
        self.text_templates = TextTemplatesClient(client_wrapper=self._client_wrapper)
        self.vat_rates = VatRatesClient(client_wrapper=self._client_wrapper)
        self.webhook_deliveries = WebhookDeliveriesClient(client_wrapper=self._client_wrapper)
        self.webhook_subscriptions = WebhookSubscriptionsClient(client_wrapper=self._client_wrapper)
        self.accounting = AccountingClient(client_wrapper=self._client_wrapper)


class AsyncMonite:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : MoniteEnvironment
        The environment to use for requests from the client. from .environment import MoniteEnvironment



        Defaults to MoniteEnvironment.SANDBOX



    monite_version : str
    monite_entity_id : typing.Optional[str]
    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from monite import AsyncMonite

    client = AsyncMonite(
        monite_version="YOUR_MONITE_VERSION",
        monite_entity_id="YOUR_MONITE_ENTITY_ID",
        token="YOUR_TOKEN",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: MoniteEnvironment = MoniteEnvironment.SANDBOX,
        monite_version: str,
        monite_entity_id: typing.Optional[str] = None,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            monite_version=monite_version,
            monite_entity_id=monite_entity_id,
            token=token,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.analytics = AsyncAnalyticsClient(client_wrapper=self._client_wrapper)
        self.approval_policies = AsyncApprovalPoliciesClient(client_wrapper=self._client_wrapper)
        self.approval_requests = AsyncApprovalRequestsClient(client_wrapper=self._client_wrapper)
        self.audit_logs = AsyncAuditLogsClient(client_wrapper=self._client_wrapper)
        self.access_tokens = AsyncAccessTokensClient(client_wrapper=self._client_wrapper)
        self.batch_payments = AsyncBatchPaymentsClient(client_wrapper=self._client_wrapper)
        self.comments = AsyncCommentsClient(client_wrapper=self._client_wrapper)
        self.counterparts = AsyncCounterpartsClient(client_wrapper=self._client_wrapper)
        self.data_exports = AsyncDataExportsClient(client_wrapper=self._client_wrapper)
        self.pdf_templates = AsyncPdfTemplatesClient(client_wrapper=self._client_wrapper)
        self.entities = AsyncEntitiesClient(client_wrapper=self._client_wrapper)
        self.entity_users = AsyncEntityUsersClient(client_wrapper=self._client_wrapper)
        self.events = AsyncEventsClient(client_wrapper=self._client_wrapper)
        self.files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        self.financing = AsyncFinancingClient(client_wrapper=self._client_wrapper)
        self.mail_templates = AsyncMailTemplatesClient(client_wrapper=self._client_wrapper)
        self.mailbox_domains = AsyncMailboxDomainsClient(client_wrapper=self._client_wrapper)
        self.mailboxes = AsyncMailboxesClient(client_wrapper=self._client_wrapper)
        self.measure_units = AsyncMeasureUnitsClient(client_wrapper=self._client_wrapper)
        self.onboarding_links = AsyncOnboardingLinksClient(client_wrapper=self._client_wrapper)
        self.overdue_reminders = AsyncOverdueRemindersClient(client_wrapper=self._client_wrapper)
        self.credit_notes = AsyncCreditNotesClient(client_wrapper=self._client_wrapper)
        self.purchase_orders = AsyncPurchaseOrdersClient(client_wrapper=self._client_wrapper)
        self.payables = AsyncPayablesClient(client_wrapper=self._client_wrapper)
        self.payment_intents = AsyncPaymentIntentsClient(client_wrapper=self._client_wrapper)
        self.payment_links = AsyncPaymentLinksClient(client_wrapper=self._client_wrapper)
        self.payment_records = AsyncPaymentRecordsClient(client_wrapper=self._client_wrapper)
        self.payment_reminders = AsyncPaymentRemindersClient(client_wrapper=self._client_wrapper)
        self.payment_terms = AsyncPaymentTermsClient(client_wrapper=self._client_wrapper)
        self.products = AsyncProductsClient(client_wrapper=self._client_wrapper)
        self.projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        self.receivables = AsyncReceivablesClient(client_wrapper=self._client_wrapper)
        self.recurrences = AsyncRecurrencesClient(client_wrapper=self._client_wrapper)
        self.roles = AsyncRolesClient(client_wrapper=self._client_wrapper)
        self.partner_settings = AsyncPartnerSettingsClient(client_wrapper=self._client_wrapper)
        self.tags = AsyncTagsClient(client_wrapper=self._client_wrapper)
        self.text_templates = AsyncTextTemplatesClient(client_wrapper=self._client_wrapper)
        self.vat_rates = AsyncVatRatesClient(client_wrapper=self._client_wrapper)
        self.webhook_deliveries = AsyncWebhookDeliveriesClient(client_wrapper=self._client_wrapper)
        self.webhook_subscriptions = AsyncWebhookSubscriptionsClient(client_wrapper=self._client_wrapper)
        self.accounting = AsyncAccountingClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: MoniteEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
