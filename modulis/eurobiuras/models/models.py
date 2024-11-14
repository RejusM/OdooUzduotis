# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DocumentManagement(models.Model):
    _name = 'document.management'
    _description = 'Document Management'

    name = fields.char(string='Pavadinimas', required=True)
    description = fields.Text(string='Aprašymas')
    company_id = fields.Many2one('res.company', string='Įmonė')
    create_uid = fields.Many2one('res.users', string='Sukurė', readonly=True, default=lambda self: self.env.user)
    employee_ids = fields.Many2many('hr.employee', string='Atsakingi Darbuotojai')
