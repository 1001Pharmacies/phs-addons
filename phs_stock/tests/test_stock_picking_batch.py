from odoo.tests.common import TransactionCase
from odoo.tools.safe_eval import safe_eval


class TestStockPickingBatchRule(TransactionCase):
    """Tests for stock picking batch creation based on rules"""

    def setUp(self):
        super(TestStockPickingBatchRule, self).setUp()
        self.picking = self.env["stock.picking"]
        self.picking_batch = self.env["stock.picking.batch"]
        self.rules = self.env["stock.picking.batch.rule"]
        # clean existings rules
        self.rules.search([]).unlink()
        self.type_pick_out_id = self.env.ref("stock.picking_type_out")

    def test_no_rule_no_batch(self):
        # No batch creation without rules
        batch = self.rules.batch_creation()
        self.assertEqual(len(batch), 0)

    def test_rule_matching_all_pickings(self):
        """One rule matching all picking (8) split in batch of 2 orders
        expected result: 4 batch
        """
        filter_all = self.env["ir.filters"].create(
            {
                "name": "All",
                "model_id": "stock.picking",
                "domain": "[]",
                "context": "{'group_by': []}",
                "sort": "[]",
            }
        )
        rule = self.rules.create(
            {
                "name": "All",
                "filter_id": filter_all.id,
                "nbr_box": 2,
                "nbr_order": 1,
                "picking_type_id": self.type_pick_out_id.id,
            }
        )
        batch = rule.batch_creation()
        pre_filtered_domain = [
            ("picking_type_id", "=", rule.picking_type_id.id),
            ("state", "=", "assigned"),
        ]
        pickings = self.env["stock.picking"].search(
            pre_filtered_domain + safe_eval(rule.filter_id.domain)
        )
        self.assertEqual(len(batch), int(len(pickings) / 2))
