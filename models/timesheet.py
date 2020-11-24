# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields, _
from dateutil.relativedelta import relativedelta, MO, SU, SA, FR

import logging

_logger = logging.getLogger(__name__)

START_OF_WEEK = {
    'week': relativedelta(weekday=SA(-1)),
    'month': relativedelta(day=1, weekday=MO(-1)),
    'year': relativedelta(yearday=1, weekday=MO(-1)),
}
START_OF = {
    'week': relativedelta(weekday=SA(-1)),
    'month': relativedelta(day=1),
    'year': relativedelta(yearday=1),
}

END_OF = {
    'week': relativedelta(weekday=FR),
    'month': relativedelta(months=1, day=1, days=-1),
    'year': relativedelta(years=1, yearday=1, days=-1),
}
END_OF_WEEK = {
    'week': relativedelta(weekday=FR),
    'month': relativedelta(months=1, day=1, days=-1, weekday=SU),
    'year': relativedelta(years=1, yearday=1, days=-1, weekday=SU),
}


class BaseInherit(models.AbstractModel):
    _inherit = 'base'

    def _grid_start_of(self, span, step, anchor):
        if step == 'week':
            return anchor + START_OF_WEEK[span]
        return anchor + START_OF[span]
    
    def _grid_end_of(self, span, step, anchor):
        if step == 'week':
            return anchor + END_OF_WEEK[span]
        return anchor + END_OF[span]


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    timesheet_start_from_saturday = fields.Boolean("Timsheet start from saturday", readonly=False,
        help="If checked, timesheet week starts from Saturday")

