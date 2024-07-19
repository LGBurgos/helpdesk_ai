from odoo import models, fields, api
import openai
from datetime import datetime, timedelta

class HelpdeskGpt4Knowledge(models.Model):
    _name = 'helpdesk.gpt4.knowledge'
    _description = 'GPT-4 Knowledge Base Entry'
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('cancelled', 'Cancelled'),
        ('entered', 'Entered')
    ], default='draft', string="State")

    question = fields.Text(string="Question")
    answer = fields.Text(string="Answer")
    modified = fields.Boolean(string="Modified", default=False)

    @api.model
    def create_knowledge_entries(self):
        tickets = self.env['helpdesk.ticket'].search([('create_date', '>=', datetime.now() - timedelta(days=1))])
        for ticket in tickets:
            if ticket.description:
                entry = self.create({
                    'question': ticket.description,
                    'answer': '',  # Asigna aquí la respuesta de la AI si corresponde
                })

    def action_enter(self):
        for record in self:
            # Aquí deberías integrar la lógica para enviar la información a la base de datos de la AI
            record.state = 'entered'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'

    def action_reset_to_draft(self):
        for record in self:
            record.state = 'draft'

