# -*- coding: utf-8 -*- 
from odoo import models, fields # type: ignore
from odoo import api # type: ignore

class Marcas(models.Model):
    _name = "marcas"
    _description = "Automoviles"
    name = fields.Char(string='Marca de automóvil', store=True)
    modelo_auto = fields.One2many('modelos','marca',string='Modelo de auto')


class Modelos(models.Model):
    _name = "modelos"
    _description = "Modelo de automoviles "
    name = fields.Char(string= 'Modelo de automóvil')
    marca = fields.Many2one('marcas', string='Marca de automovil')
    imagen= fields.Binary()

class Clientes (models.Model):
    _inherit = 'res.partner'
    _description= 'Modelos de autos'
    auto_marca = fields.Many2one('marcas', string='Tipo de auto')
    auto_modelo = fields.Many2one('modelos', string='Modelo de auto')
    auto_marca_2 = fields.Many2one('marcas', string='Tipo de auto')
    auto_modelo_2 = fields.Many2one('modelos', string='Modelo de auto')

