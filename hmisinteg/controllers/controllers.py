# -*- coding: utf-8 -*-
# from odoo import http


# class Hmisinteg(http.Controller):
#     @http.route('/hmisinteg/hmisinteg/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hmisinteg/hmisinteg/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hmisinteg.listing', {
#             'root': '/hmisinteg/hmisinteg',
#             'objects': http.request.env['hmisinteg.hmisinteg'].search([]),
#         })

#     @http.route('/hmisinteg/hmisinteg/objects/<model("hmisinteg.hmisinteg"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hmisinteg.object', {
#             'object': obj
#         })
