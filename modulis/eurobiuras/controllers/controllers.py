# -*- coding: utf-8 -*-
# from odoo import http


# class Eurobiuras(http.Controller):
#     @http.route('/eurobiuras/eurobiuras/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/eurobiuras/eurobiuras/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('eurobiuras.listing', {
#             'root': '/eurobiuras/eurobiuras',
#             'objects': http.request.env['eurobiuras.eurobiuras'].search([]),
#         })

#     @http.route('/eurobiuras/eurobiuras/objects/<model("eurobiuras.eurobiuras"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('eurobiuras.object', {
#             'object': obj
#         })
