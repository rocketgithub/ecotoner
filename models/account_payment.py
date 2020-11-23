# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class account_payment(models.Model):
    _inherit = "account.payment"

    serie = fields.Char('Serie')
    tipo_ab= fields.Selection([ ('a', 'A'),('b', 'B'),],'A o B',default='b')
    numero_boleta = fields.Char('No. Boleta')
    banco = fields.Char('Banco')
