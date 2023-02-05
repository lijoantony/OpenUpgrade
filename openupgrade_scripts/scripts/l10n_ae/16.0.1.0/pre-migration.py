# Copyright 2023 Lijo Antony <https://www.cargoz.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade

_model_renames = []

_table_renames = []

_field_renames = []

_xmlid_renames = [
    # ir.model.access
    # ("website.group_website_publisher", "website.group_website_restricted_editor"),
]


@openupgrade.migrate()
def migrate(env, version):
    # openupgrade.rename_models(env.cr, _model_renames)
    # openupgrade.rename_tables(env.cr, _table_renames)
    # openupgrade.rename_fields(env, _field_renames)
    # openupgrade.rename_xmlids(env.cr, _xmlid_renames)

    openupgrade.logged_query(
        env.cr,
        """
            UPDATE ir_model_data
            SET model = 'account.report'
            WHERE model = 'account.tax.report' AND name = 'tax_report' AND module = 'l10n_ae'""",
    )
