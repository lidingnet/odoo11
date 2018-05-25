# -*- coding: utf-8 -*-
import logging


from odoo import models, fields, api, _
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)


class PurchaseTrackTony(models.Model):
    _name = 'purchase.track'

    f1 = fields.Char(string="字段1")
