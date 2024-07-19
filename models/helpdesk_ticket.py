from odoo import models, fields, api
import openai
import requests
import json
from datetime import datetime, timedelta

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    def fetch_gpt4_response(self, question):
        company = self.env.user.company_id
        ai_provider = company.ai_provider
        api_key = company.gpt4_api_key

        if ai_provider == 'openai':
            openai.api_key = api_key
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=question,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        elif ai_provider == 'azure':
            headers = {
                'Ocp-Apim-Subscription-Key': company.azure_api_key,
                'Content-Type': 'application/json'
            }
            body = {
                "prompt": question,
                "max_tokens": 150
            }
            response = requests.post(company.azure_endpoint, headers=headers, json=body)
            return response.json().get('choices')[0].get('text').strip()
        elif ai_provider == 'google':
            url = f"https://api.openai.com/v1/engines/davinci-codex/completions"
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {company.google_api_key}'
            }
            body = {
                "prompt": question,
                "max_tokens": 150
            }
            response = requests.post(url, headers=headers, json=body)
            return response.json().get('choices')[0].get('text').strip()

    def button_fetch_gpt4_response(self):
        for ticket in self:
            question = ticket.description
            response = self.fetch_gpt4_response(question)
            ticket.description += f"\n\nAI Response:\n{response}"

    @api.model
    def cron_auto_respond_tickets(self):
        company = self.env.user.company_id
        interval_type = company.cron_interval_type
        interval_number = company.cron_interval_number
        if interval_type == 'minutes':
            delta = timedelta(minutes=interval_number)
        elif interval_type == 'hours':
            delta = timedelta(hours=interval_number)
        elif interval_type == 'days':
            delta = timedelta(days=interval_number)
        elif interval_type == 'weeks':
            delta = timedelta(weeks=interval_number)
        elif interval_type == 'months':
            delta = timedelta(days=30 * interval_number)
        threshold_date = datetime.now() - delta
        tickets = self.search([('create_date', '<=', threshold_date), ('stage_id.is_close', '=', False)])
        for ticket in tickets:
            if not ticket.message_ids.filtered(lambda m: m.create_date > threshold_date):
                question = ticket.description
                response = self.fetch_gpt4_response(question)
                ticket.message_post(body=f"Automated Response:\n{response}")
