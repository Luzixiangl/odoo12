# -*- coding: utf-8 -*-

from datetime import datetime
from datetime import timedelta
from datetime import date
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class Book(models.Model):
    _name = 'book_store.book'
    _description = '新智联图书库,致力于收藏优质书籍'
    _order = 'name,date desc'  # 浏览时默认排序，等同于SQL 的 ORDER BY语句

    # _table = 'xxx'        # 指定模型对应的数据表名。默认表明为ORM通过替换模块名中的点为下划线来自动定义
    name = fields.Char('名称', help='书名')
    author = fields.Many2one('book_store.author', string='作者', help='作者', delegate=True)
    # 下拉选择列表，选项位置参数是一个[(‘value’ ,‘Title’ ),('', ''),...]元组列表
    # 元组第一个元素是存储在数据库中的值，第二个元素是展示在用户界面中的描述。
    # 该列表可由其它模块使用 selection_add 关键字参数扩展
    book_type = fields.Selection(
        [('tutorials', 'Tutorials'),
         ('literature', 'Literature'),
         ('other', 'Other')],
        '书籍类型'
    )
    date = fields.Date("出版日期", help="日期", default=date.today())
    price = fields.Float("定价", help="定价")
    # price = fields.Monetary(string='定价', currency_field='price', help='定价')
    ref = fields.Reference(
        selection=[('book_store.author', '作者'), ('book_store.publisher', '出版商')])
    age = fields.Integer('书龄', compute="_get_book_age", search="_search_ages")


    @api.one
    def btn_test(self):
        """测试方法"""
        _logger.info("测试创建出版商和作者")
        self.env['book_store.publisher'].sudo().create({
            "name": "超新星出版社",
            "signed_authors": [(0, 0, {'name': '本杰明 巴顿', 'age': 90}), (0, 0, {'name': '刘天然', 'age': 28})]
        })

    @api.depends('date')
    def _get_book_age(self):
        self.age = (date.today() - self.date).days

    @api.model
    def _search_ages(self, operator, operand):
        """search方法"""
        if operator not in ('>', '>=', '<', '<=', '='):
            return []
        if type(operand) not in (float, int):
            return []
        start_date = datetime.now().date() - timedelta(days=operand)
        ops = {
            ">": "<",
            ">=": "<=",
            "<": ">",
            "<=": ">=",
            "=": "="
        }
        return [('date', ops[operator], start_date)]

    @api.multi
    def write(self, vals):
        _logger.info("write:{vals}")
        _logger.info("self:{self}")
        res = super(Book, self).write(vals)
        _logger.info("write returns:{res}")
        self.log_book_name()
        return res

    @api.model
    def create(self, vals):
        return super(Book, self).create(vals)

    @api.one
    def log_book_name(self):
        self.__log_book_name()

    def __log_book_name(self):
        _logger.info("图书名称：{self.name}")

    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        res = super(Book, self).fields_view_get(
            view_id, view_type, toolbar, submenu)
        return res

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(Book, self).fields_get(allfields, attributes)
        return res


class eBook(models.Model):
    _inherit = "book_store.book"
    _name = "book_store.ebook"

    etype = fields.Selection(selection=[('mobi', 'Mobi'), ('epub', 'Epub'), (
        'awz', 'Awz3')], string='电子书格式', default='epub', help='')


class sBook(models.Model):

    _name = "book_store.sbook"
    _inherits = {'book_store.ebook': 'ebook_id'}
    is_Available = fields.Boolean('可借?')
    in_stock = fields.Integer('库存')
    ebook_id = fields.Many2one(
        'book_store.ebook', string='ebook', ondelete='restrict', required=True, help='')


class Author(models.Model):
    _name = 'book_store.author'

    name = fields.Char('名称', help='作者名称')
    age = fields.Integer('年龄')
    publisher_id = fields.Many2one(
        'book_store.publisher', string='签约出版商', ondelete='no action', required=True, help='')


class Publisher(models.Model):
    _name = "book_store.publisher"

    name = fields.Char('名称', help='出版商名称')
    signed_authors = fields.One2many(
        'book_store.author', 'publisher_id', string="签约作者")
