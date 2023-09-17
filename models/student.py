from odoo import fields, models, api


class Student(models.Model):
    _name = "school.student"
    _inherit = 'mail.thread'
    _description = "Student"

    name = fields.Char(string="Student", tracking=True)
    country = fields.Char(string="Country", tracking=True)
    dob = fields.Char(string="Date of Birth", tracking=True)
    age = fields.Char(string="Age", compute='_compute_age')

    @api.depends('dob')
    def _compute_age(self):
        for rec in self:
            if rec.dob:
                rec.age = 2023 - int(rec.dob.split('-')[2])
            else:
                rec.age = ""