from odoo import fields, models


class Teacher(models.Model):
    _name = "school.teacher"
    _inherit = 'mail.thread'
    _description = "Teacher"

    name = fields.Char(string="Teacher", tracking=True)
    country = fields.Char(string="Country", tracking=True)