from odoo import fields,models

class Book(models.Model):
    _inherit = 'book_store.book'        # 继承book_store.book模型
    is_available = fields.Boolean('可借?')
