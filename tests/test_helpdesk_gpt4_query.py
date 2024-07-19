from odoo.tests.common import TransactionCase

class TestHelpdeskGpt4Query(TransactionCase):

    def setUp(self):
        super(TestHelpdeskGpt4Query, self).setUp()
        self.HelpdeskGpt4Query = self.env['helpdesk.gpt4.query']

    def test_query_gpt4(self):
        query = self.HelpdeskGpt4Query.create({
            'question': 'What is Odoo?'
        })
        query.button_fetch_gpt4_response()
        self.assertTrue(query.answer, "The GPT-4 response should not be empty")

