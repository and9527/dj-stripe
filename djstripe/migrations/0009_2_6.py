# Generated by Django 3.2.4 on 2021-06-22 01:38

import uuid

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djstripe.enums
import djstripe.fields


class Migration(migrations.Migration):
    dependencies = [
        ("djstripe", "0008_2_5"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebhookEndpoint",
            fields=[
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(blank=True, null=True),
                ),
                (
                    "metadata",
                    djstripe.fields.JSONField(blank=True, null=True),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A description of this object.", null=True
                    ),
                ),
                (
                    "api_version",
                    models.CharField(
                        blank=True,
                        help_text="The API version events are rendered as for this webhook endpoint.",
                        max_length=10,
                    ),
                ),
                (
                    "enabled_events",
                    djstripe.fields.JSONField(),
                ),
                (
                    "secret",
                    models.CharField(
                        blank=True,
                        help_text="The endpoint's secret, used to generate webhook signatures.",
                        max_length=256,
                        editable=False,
                    ),
                ),
                (
                    "status",
                    djstripe.fields.StripeEnumField(
                        enum=djstripe.enums.WebhookEndpointStatus, max_length=8
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="The URL of the webhook endpoint.", max_length=2048
                    ),
                ),
                (
                    "application",
                    models.CharField(
                        blank=True,
                        help_text="The ID of the associated Connect application.",
                        max_length=255,
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                        help_text="The Stripe Account this object belongs to.",
                    ),
                ),
                (
                    "djstripe_uuid",
                    models.UUIDField(
                        null=True,
                        unique=True,
                        default=uuid.uuid4,
                        help_text="A UUID specific to dj-stripe generated for the endpoint",
                    ),
                ),
            ],
            options={"get_latest_by": "created", "abstract": False},
        ),
        migrations.CreateModel(
            name="UsageRecordSummary",
            fields=[
                ("djstripe_created", models.DateTimeField(auto_now_add=True)),
                ("djstripe_updated", models.DateTimeField(auto_now=True)),
                (
                    "djstripe_id",
                    models.BigAutoField(
                        primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("id", djstripe.fields.StripeIdField(max_length=255, unique=True)),
                (
                    "livemode",
                    models.BooleanField(
                        blank=True,
                        default=None,
                        help_text="Null here indicates that the livemode status is unknown or was previously unrecorded. Otherwise, this field indicates whether this record comes from Stripe test mode or live mode operation.",
                        null=True,
                    ),
                ),
                (
                    "created",
                    djstripe.fields.StripeDateTimeField(blank=True, null=True),
                ),
                (
                    "period",
                    djstripe.fields.JSONField(blank=True, null=True),
                ),
                (
                    "period_end",
                    djstripe.fields.StripeDateTimeField(blank=True, null=True),
                ),
                (
                    "period_start",
                    djstripe.fields.StripeDateTimeField(blank=True, null=True),
                ),
                (
                    "total_usage",
                    models.PositiveIntegerField(
                        help_text="The quantity of the plan to which the customer should be subscribed."
                    ),
                ),
                (
                    "djstripe_owner_account",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="djstripe.account",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                        help_text="The Stripe Account this object belongs to.",
                    ),
                ),
                (
                    "invoice",
                    djstripe.fields.StripeForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usage_record_summaries",
                        to="djstripe.invoice",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                    ),
                ),
                (
                    "subscription_item",
                    djstripe.fields.StripeForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="usage_record_summaries",
                        to="djstripe.subscriptionitem",
                        to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                        help_text="The subscription item this usage record contains data for.",
                    ),
                ),
            ],
            options={"get_latest_by": "created", "abstract": False},
        ),
        migrations.AddField(
            model_name="applicationfee",
            name="account",
            field=djstripe.fields.StripeForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="application_fees",
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                help_text="ID of the Stripe account this fee was taken from.",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="customer",
            name="deleted",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Whether the Customer instance has been deleted upstream in Stripe or not.",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="dispute",
            name="balance_transaction",
            field=djstripe.fields.StripeForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="disputes",
                to="djstripe.balancetransaction",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                help_text="Balance transaction that describes the impact on your account balance.",
            ),
        ),
        migrations.AddField(
            model_name="dispute",
            name="charge",
            field=djstripe.fields.StripeForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="disputes",
                to="djstripe.charge",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                help_text="The charge that was disputed",
            ),
        ),
        migrations.AddField(
            model_name="dispute",
            name="payment_intent",
            field=djstripe.fields.StripeForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="disputes",
                to="djstripe.paymentintent",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                help_text="The PaymentIntent that was disputed",
            ),
        ),
        migrations.AddField(
            model_name="dispute",
            name="balance_transactions",
            field=djstripe.fields.JSONField(
                default=list,
            ),
        ),
        migrations.AlterField(
            model_name="taxrate",
            name="percentage",
            field=djstripe.fields.StripePercentField(
                decimal_places=4,
                max_digits=7,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="transfer",
            name="destination",
            field=djstripe.fields.StripeIdField(
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="usagerecord",
            name="action",
            field=djstripe.fields.StripeEnumField(
                default="increment",
                enum=djstripe.enums.UsageAction,
                max_length=9,
            ),
        ),
        migrations.AddField(
            model_name="usagerecord",
            name="timestamp",
            field=djstripe.fields.StripeDateTimeField(
                blank=True,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="webhookeventtrigger",
            name="stripe_trigger_account",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="djstripe.account",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                help_text="The Stripe Account this object belongs to.",
            ),
        ),
        migrations.RemoveField(model_name="usagerecord", name="description"),
        migrations.RemoveField(model_name="usagerecord", name="metadata"),
        migrations.AlterField(
            model_name="paymentmethod",
            name="type",
            field=djstripe.fields.StripeEnumField(
                enum=djstripe.enums.PaymentMethodType, max_length=17
            ),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="acss_debit",
            field=djstripe.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="afterpay_clearpay",
            field=djstripe.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="boleto",
            field=djstripe.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="grabpay",
            field=djstripe.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="paymentmethod",
            name="wechat_pay",
            field=djstripe.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="subscription",
            name="latest_invoice",
            field=djstripe.fields.StripeForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="djstripe.invoice",
                to_field=settings.DJSTRIPE_FOREIGN_KEY_TO_FIELD,
                help_text="The most recent invoice this subscription has generated.",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="delinquent",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Whether or not the latest charge for the customer's latest invoice has failed.",
                null=True,
            ),
        ),
    ]
