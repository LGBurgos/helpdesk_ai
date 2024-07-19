from odoo import models, fields, api
import openai

class HelpdeskGpt4Query(models.TransientModel):
    _name = 'helpdesk.gpt4.query'
    _description = 'GPT-4 Query'

    question = fields.Text(string="Question")
    answer = fields.Text(string="Answer", readonly=True)

    def button_fetch_gpt4_response(self):
        self.ensure_one()
        company = self.env.user.company_id
        api_key = company.gpt4_api_key
        openai.api_key = api_key
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self.question,
            max_tokens=150
        )
        self.answer = response.choices[0].text.strip()
