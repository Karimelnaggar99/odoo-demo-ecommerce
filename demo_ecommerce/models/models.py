# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class demo_ecommerce(models.Model):
#     _name = 'demo_ecommerce.demo_ecommerce'
#     _description = 'demo_ecommerce.demo_ecommerce'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
