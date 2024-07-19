from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    gpt4_api_key = fields.Char("OpenAI API Key", related='company_id.gpt4_api_key', readonly=False)
    azure_api_key = fields.Char("Azure API Key", related='company_id.azure_api_key', readonly=False)
    azure_endpoint = fields.Char("Azure Endpoint", related='company_id.azure_endpoint', readonly=False)
    google_api_key = fields.Char("Google API Key", related='company_id.google_api_key', readonly=False)
    ai_provider = fields.Selection([
        ('openai', 'OpenAI'),
        ('azure', 'Azure AI'),
        ('google', 'Google AI'),
    ], string="AI Provider", default='openai', related='company_id.ai_provider', readonly=False)
    cron_interval_number = fields.Integer("Cron Interval Number", related='company_id.cron_interval_number', readonly=False)
    cron_interval_type = fields.Selection([
        ('minutes', 'Minutes'),
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months')
    ], string="Cron Interval Type", related='company_id.cron_interval_type', readonly=False)

class ResCompany(models.Model):
    _inherit = 'res.company'

    gpt4_api_key = fields.Char("OpenAI API Key")
    azure_api_key = fields.Char("Azure API Key")
    azure_endpoint = fields.Char("Azure Endpoint")
    google_api_key = fields.Char("Google API Key")
    ai_provider = fields.Selection([
        ('openai', 'OpenAI'),
        ('azure', 'Azure AI'),
        ('google', 'Google AI'),
    ], string="AI Provider", default='openai')
    cron_interval_number = fields.Integer("Cron Interval Number", default=1)
    cron_interval_type = fields.Selection([
        ('minutes', 'Minutes'),
        ('hours', 'Hours'),
        ('days', 'Days'),
        ('weeks', 'Weeks'),
        ('months', 'Months')
    ], string="Cron Interval Type", default='days')
