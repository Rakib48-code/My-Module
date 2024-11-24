from odoo import api, fields, models

class Course(models.Model):
    _name = 'open.course'
    _description = 'Academic Open Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('open.session','course_id', string='Sessions')