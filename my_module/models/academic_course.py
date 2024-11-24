from odoo import api, fields, models

class Course(models.Model):
    _name = 'open.course'
    _description = 'Academic Open Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')