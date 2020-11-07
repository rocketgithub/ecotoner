# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class account_payment(models.Model):
    _inherit = "account.payment"

    serie_a = fields.Char('Serie A')
    serie_b = fields.Char('Serie B')
    numero_boleta = fields.Char('No. Boleta')
    banco = fields.Char('Banco')
