from odoo import models, fields

class User(models.Model):
    _name = "user"
    _description = "Usuario del juego"

    name = fields.Char(string="Nombre")
    email = fields.Char(string="Email")
    date = fields.Date(string="Fecha de nacimento")
    gender = fields.Selection(selection=[('male', 'Masculino'), ('fale', 'Femenino')], string="Genero")
    card_ids = fields.Many2many(
        comodel_name='card',
        relation='user_card_rel',
        column1='user_id_col',
        column2='card_id_col',
        string="Cartas"
    )