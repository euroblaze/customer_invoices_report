from datetime import date, time, datetime, timedelta

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

from odoo.exceptions import UserError


class ClassResPartner(models.Model):
    _inherit = "res.partner"

    current_user = fields.Many2one('res.users', compute='_get_current_user', default=1)

    @api.depends()
    def _get_current_user(self):
        for rec in self:
            rec.current_user = self.env.user

        self.update({'current_user': self.env.user.id})
