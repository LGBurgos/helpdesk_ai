from odoo.tests.common import TransactionCase

class TestHelpdeskGpt4Knowledge(TransactionCase):

    def setUp(self):
        super(TestHelpdeskGpt4Knowledge, self).setUp()
        self.HelpdeskGpt4Knowledge = self.env['helpdesk.gpt4.knowledge']

    def test_create_knowledge_entries(self):
        self.env['helpdesk.ticket'].create({
            'name': 'Test Ticket',
            'description': 'Test Description'
        })
        self.HelpdeskGpt4Knowledge.create_knowledge_entries()
        entries = self.HelpdeskGpt4Knowledge.search([('question', '=', 'Test Description')])
        self.assertTrue(entries, "Knowledge entry should be created for the ticket")

    def test_action_enter(self):
        entry = self.HelpdeskGpt4Knowledge.create({
            'question': 'Test Question',
            'answer': 'Test Answer'
        })
        entry.action_enter()
        self.assertEqual(entry.state, 'entered', "The state should be 'entered' after action_enter")

    def test_action_cancel(self):
        entry = self.HelpdeskGpt4Knowledge.create({
            'question': 'Test Question',
            'answer': 'Test Answer'
        })
        entry.action_cancel()
        self.assertEqual(entry.state, 'cancelled', "The state should be 'cancelled' after action_cancel")

    def test_action_reset_to_draft(self):
        entry = self.HelpdeskGpt4Knowledge.create({
            'question': 'Test Question',
            'answer': 'Test Answer',
            'state': 'cancelled'
        })
        entry.action_reset_to_draft()
        self.assertEqual(entry.state, 'draft', "The state should be 'draft' after action_reset_to_draft")

