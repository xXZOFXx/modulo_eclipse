# -*- coding: utf-8 -*-
from odoo import http

class ModuloEclipse(http.Controller):
     @http.route('/modulo_eclipse/', auth='public')
     def index(self, **kw):
        return http.request.render('modulo_eclipse.index', {})

#     @http.route('/modulo_eclipse/modulo_eclipse/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_eclipse.listing', {
#             'root': '/modulo_eclipse/modulo_eclipse',
#             'objects': http.request.env['modulo_eclipse.modulo_eclipse'].search([]),
#         })

#     @http.route('/modulo_eclipse/modulo_eclipse/objects/<model("modulo_eclipse.modulo_eclipse"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_eclipse.object', {
#             'object': obj
#         })
