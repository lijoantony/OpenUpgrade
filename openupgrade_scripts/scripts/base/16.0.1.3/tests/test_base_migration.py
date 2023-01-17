from odoo.tests import TransactionCase


class TestBaseMigration(TransactionCase):
    def test_company_registry(self):
        """Make sure we copy res.company#company_registry to res.partner#company_registry"""
        self.assertEqual(self.env.ref("base.main_company").company_registry, "424242")
