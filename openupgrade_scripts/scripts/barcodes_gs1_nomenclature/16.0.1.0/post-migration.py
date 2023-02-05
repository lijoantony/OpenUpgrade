# Copyright 2023 Lijo Antony <https://www.cargoz.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def map_barcode_rule_type(env):
    openupgrade.map_values(
        env.cr,
        openupgrade.get_legacy_name("type"),
        "type",
        [("packaging_date", "pack_date")],
        table="barcode_rule",
    )


@openupgrade.migrate()
def migrate(env, version):
    map_barcode_rule_type(env)
