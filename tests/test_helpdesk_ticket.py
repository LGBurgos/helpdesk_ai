from odoo.tests.common import TransactionCase

class TestHelpdeskTicket(TransactionCase):

    def setUp(self):
        super(TestHelpdeskTicket, self).setUp()
        self.HelpdeskTicket = self.env['helpdesk.ticket']
        self.test_ticket = self.HelpdeskTicket.create({
            'name': 'Test Ticket',
            'description': 'Test Description'
        })

    def test_fetch_gpt4_response(self):
        response = self.test_ticket.fetch_gpt4_response("What is Odoo?")
        self.assertTrue(response, "The GPT-4 response should not be empty")

    def test_cron_auto_respond_tickets(self):
        self.test_ticket.write({'create_date': fields.Datetime.now() - timedelta(days=2)})
        self.env['ir.cron'].create({
            'name': 'Test Auto Respond',
            'model_id': self.env.ref('helpdesk.model_helpdesk_ticket').id,
            'state': 'code',
            'code': 'model.cron_auto_respond_tickets()',
            'user_id': self.env.ref('base.user_root').id,
            'interval_number': 1,
            'interval_type': 'days'
        }).method_direct_trigger()
        self.assertIn('Automated Response', self.test_ticket.message_ids.mapped('body'), "The ticket should have an automated response")

