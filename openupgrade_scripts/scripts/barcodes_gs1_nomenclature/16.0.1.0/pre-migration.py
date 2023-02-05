# Copyright 2023 Lijo Antony <https://www.cargoz.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

_model_renames = [
    ("stock.location.route", "stock.route"),
    ("stock.production.lot", "stock.lot"),
]

_table_renames = [
    ("stock_location_route", "stock_route"),
    ("stock_production_lot", "stock_lot"),
    # many2many tables
    # transients
]

_field_renames = [
    # ("link.tracker.click", "link_tracker_click", "mail_stat_id", "mailing_trace_id"),
    # ("mailing.trace", "mailing_trace", "mass_mailing_campaign_id", "campaign_id"),
    # ("mail.mail", "mail_mail", "statistics_ids", "mailing_trace_ids"),
    # ("utm.campaign", "utm_campaign", "mass_mailing_ids", "mailing_mail_ids"),
    # ("mailing.mailing", "mailing_mailing", "statistics_ids", "mailing_trace_ids"),
]

_xmlid_renames = [
    # ir.model.access
    # ("mass_mailing.access_mass_mailing", "mass_mailing.access_mailing_mailing_mm_user"),
    # (
    #     "mass_mailing.access_mass_mailing_system",
    #     "mass_mailing.access_mailing_mailing_system",
    # ),
    # (
    #     "mass_mailing.access_mass_mailing_list",
    #     "mass_mailing.access_mailing_list_mm_user",
    # ),
    # (
    #     "mass_mailing.access_mass_mailing_contact",
    #     "mass_mailing.access_mailing_contact_mm_user",
    # ),
    # (
    #     "mass_mailing.access_mail_statistics_report",
    #     "mass_mailing.access_mailing_trace_report_mm_user",
    # ),
    # (
    #     "mass_mailing.access_mail_mass_mailing_list_contact_rel",
    #     "mass_mailing.access_mailing_contact_subscription_mm_user",
    # ),
    # (
    #     "mass_mailing.access_mail_mail_statistics_user",
    #     "mass_mailing.access_mailing_trace_user",
    # ),
    # (
    #     "mass_mailing.access_mail_mail_statistics_mass_mailing_user",
    #     "mass_mailing.access_mailing_trace_mm_user",
    # ),
    # ("mass_mailing.access_mass_mailing_stage", "mass_mailing.access_utm_stage"),
    # (
    #     "mass_mailing.access_mass_mailing_tag",
    #     "mass_mailing.access_utm_tag_mass_mailing_campaign",
    # ),
]


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.rename_models(env.cr, _model_renames)
    openupgrade.rename_tables(env.cr, _table_renames)
    openupgrade.rename_fields(env, _field_renames)
    openupgrade.rename_xmlids(env.cr, _xmlid_renames)
    # openupgrade.set_xml_ids_noupdate_value(
    #     env,
    #     "mass_mailing",
    #     [
    #         "mass_mailing_mail_layout",
    #     ],
    #     True,
    # )
