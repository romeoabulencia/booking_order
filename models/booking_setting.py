from odoo import api
from odoo import fields
from odoo import models

class booking_settings(models.Model):
    _name="booking.settings"
    
    post_booking_time = fields.Integer('Post Booking Time')
    pre_booking_time = fields.Integer('Pre Booking Time')
    
# Post Booking Time – Numeric field
# Pre Booking Time – Numeric field
# Example post booking is 30 <integer> minutes <static text>
# That means when the system does the "check" for the booking of
# stakeholders, it will check whether they have any event during that duration
# + the post booking time and pre booking time
# Employee A has an event 15 August 3pm – 4pm
# There is a booking for 4.15 – 5:15pmpm, then it checks employee A.
# while Employee A has a booking at 3pm – 4pm +30 minutes which overlaps
# with 4.15, thus employee A is unavailable
# Default Pre and Post booking time is 0 minutes.    
    