from odoo import fields, models, api, exceptions


class Lesson(models.Model):
    _name = "school.lesson"
    _inherit = 'mail.thread'
    _description = "Lesson"

    subject = fields.Selection([('arabic', 'Arabic'), ('english', 'English'), ('math', 'Math'), ('physics', 'Physics'), ('python', 'Python'), ('chemistry', 'Chemistry')], string="Subject",
                               tracking=True)
    lesson = fields.Selection([('arabic-2023-01', 'Arabic-2023-01'), ('english-2023-01', 'English-2023-01'),
                               ('math-2023-01', 'Math-2023-01'), ('physics-2023-01', 'Physics-2023-01'), ('python-2023-01', 'Python-2023-01'), ('chemistry-2023-01', 'Chemistry-2023-01')], string="Lesson", tracking=True)
    student_id = fields.Many2one('school.student', string="Student")
    teacher_id = fields.Many2one('school.teacher', string="Teacher")
    active = fields.Boolean(default=True)
    country_mismatch = fields.Boolean(compute='_compute_country_mismatch', store=True)

    @api.depends('student_id', 'teacher_id')
    def _compute_country_mismatch(self):
        for lesson in self:
            lesson.country_mismatch = (
                lesson.student_id.country != lesson.teacher_id.country
                if lesson.student_id and lesson.teacher_id else False
            )

    @api.constrains('student_id', 'teacher_id')
    def _check_country_match(self):
        for lesson in self:
            if lesson.student_id and lesson.teacher_id and lesson.country_mismatch:
                raise exceptions.ValidationError("The student and teacher must belong to the same country!")