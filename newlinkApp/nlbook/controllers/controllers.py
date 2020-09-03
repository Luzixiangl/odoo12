# -*- coding: utf-8 -*-
from odoo import http

# class Nlbook(http.Controller):
#     @http.route('/nlbook/nlbook/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nlbook/nlbook/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nlbook.listing', {
#             'root': '/nlbook/nlbook',
#             'objects': http.request.env['nlbook.nlbook'].search([]),
#         })

#     @http.route('/nlbook/nlbook/objects/<model("nlbook.nlbook"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nlbook.object', {
#             'object': obj
#         })