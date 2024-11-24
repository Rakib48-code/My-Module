from odoo import api,models, fields

class Session(models.Model):
    _name = 'open.session'
    _description = 'Academic Open Session'

    name = fields.Char(required=True)
    start_date = fields.Date(string='Start Date')
    duration = fields.Float(string='Duration', digits=(6,2))
    seats = fields.Integer(string='Number of seats')
    instructor_id = fields.Many2one('res.partner', string='Instructor')
    course_id = fields.Many2one('open.course', string='Course')
    attendance_id = fields.Many2many('res.partner', string='Attendance')
    taken_seats = fields.Float(string='Taken Seats', compute='_taken_seats')

    @api.depends('seats', 'attendance_id')
    def _taken_seats(self):
        for r in self:
            if r.seats > 0:
                # গণনা: taken_seats-এর শতাংশ নির্ধারণ করছি
                r.taken_seats = (100 * len(r.attendance_id)) / r.seats
            else:
                # যদি seats না থাকে, তাহলে taken_seats ০.০ সেট করুন
                r.taken_seats = 0.0