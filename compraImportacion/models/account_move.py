 #-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class FacturaProveedor(models.Model):
    _inherit="account.move"

    nro_autorizacion = fields.Char(string= 'Nro Autorización')
    cod_control= fields.Char(string='Código de Control')
    nro_dui= fields.Char(string='DUI')

    