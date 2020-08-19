# -*- coding: utf-8 -*-
##############################################################################


from odoo import api, models, fields, _
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo import SUPERUSER_ID


class SaleOrderOptica(models.Model):
    _inherit = 'sale.order'
    sucursal_id=fields.Many2one(comodel_name='stock.location', string='Sucursal de venta',default=lambda self: self.env.user.sucursal_id.id)
