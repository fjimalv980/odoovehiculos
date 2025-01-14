from odoo import models, fields

class vehiculo(models.Model):
    _name = 'vehiculo.management'
    _description = 'Gestión de vehículos'
    matricula= fields.Char(string='Matrícula', required=True)
    marca = fields.Char(string='Marca', required=True)
    modelo = fields.Char(string='Modelo', required=True)
    activo = fields.Boolean(string='¿Activo?', default=True)