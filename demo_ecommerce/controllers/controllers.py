# -*- coding: utf-8 -*-
# from odoo import http


# class DemoEcommerce(http.Controller):
#     @http.route('/demo_ecommerce/demo_ecommerce', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_ecommerce/demo_ecommerce/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_ecommerce.listing', {
#             'root': '/demo_ecommerce/demo_ecommerce',
#             'objects': http.request.env['demo_ecommerce.demo_ecommerce'].search([]),
#         })

#     @http.route('/demo_ecommerce/demo_ecommerce/objects/<model("demo_ecommerce.demo_ecommerce"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_ecommerce.object', {
#             'object': obj
#         })
