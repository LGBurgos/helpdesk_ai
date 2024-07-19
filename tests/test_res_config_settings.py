from odoo.tests.common import TransactionCase

class TestResConfigSettings(TransactionCase):

    def setUp(self):
        super(TestResConfigSettings, self).setUp()
        self.ResConfigSettings = self.env['res.config.settings']

    def test_default_values(self):
        settings = self.ResConfigSettings.create({})
        self.assertEqual(settings.ai_provider, 'openai', "Default AI provider should be OpenAI")
        self.assertEqual(settings.cron_interval_number, 1, "Default cron interval number should be 1")
        self.assertEqual(settings.cron_interval_type, 'days', "Default cron interval type should be 'days'")

