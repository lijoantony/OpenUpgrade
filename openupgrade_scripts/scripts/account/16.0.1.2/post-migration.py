# Copyright 2023 Lijo Antony <https://www.cargoz.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def fill_account_account_account_type(env):
    selection = [
        ("asset_receivable", "Receivable"),
        ("asset_cash", "Bank and Cash"),
        ("asset_current", "Current Assets"),
        ("asset_non_current", "Non-current Assets"),
        ("asset_prepayments", "Prepayments"),
        ("asset_fixed", "Fixed Assets"),
        ("liability_payable", "Payable"),
        ("liability_credit_card", "Credit Card"),
        ("liability_current", "Current Liabilities"),
        ("liability_non_current", "Non-current Liabilities"),
        ("equity", "Equity"),
        ("equity_unaffected", "Current Year Earnings"),
        ("income", "Income"),
        ("income_other", "Other Income"),
        ("expense", "Expenses"),
        ("expense_depreciation", "Depreciation"),
        ("expense_direct_cost", "Cost of Revenue"),
        ("off_balance", "Off-Balance Sheet"),
    ]

    """Faster way"""
    openupgrade.logged_query(
        env.cr,
        """
        ALTER TABLE account_account_type
        ADD COLUMN selection varchar""",
    )

    openupgrade.map_values(
        env.cr,
        "name->>'en_US'",
        "selection",
        [(y, x) for (x, y) in selection],
        table="account_account_type",
    )

    openupgrade.logged_query(
        env.cr,
        """
        UPDATE account_account aa
        SET account_type = aat.selection
        FROM account_account_type aat
        WHERE aa.user_type_id = aat.id""",
    )


@openupgrade.migrate()
def migrate(env, version):
    fill_account_account_account_type(env)
