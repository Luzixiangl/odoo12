# -*- coding: utf-8 -*-

from odoo import models, fields, api

class nlbook(models.Model):
    _name = 'nlbook.nlbook'

    name = fields.Char('名称', help='书名', index=True)
    author = fields.Char('作者', help='作者', index=True)
    date = fields.Char('出版日期', help='日期')
    price = fields.Char('定价', help='定价')


    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    #
    # @api.depends('value')
    # def _value_pc(self):
    #     self.value2 = float(self.value) / 100