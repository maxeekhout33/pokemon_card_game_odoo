from odoo import models, fields

class Card(models.Model):
    _name = "card"
    _description = "Carta de Pokemon"

    name = fields.Char(string="Nombre del Pokemon")
    gender = fields.Selection(selection=[('male', 'Masculino'), ('female', 'Femenino')], string="Genero")
    type = fields.Selection(selection=[('grass', 'Hoja'), ('fire', 'Fuego'),('electric', 'Electrico'), ('water', 'Agua'),('fight', 'Lucha'), ('ghost', 'Fantasma'),('ground', 'Tierra'), ('psycho', 'Psiquico')], string="Tipo de Pokemon")
    life = fields.Integer(string="Puntos de vida")
    user_ids = fields.Many2many(
        comodel_name='user',
        relation='user_card_rel',
        column1='card_id_col',
        column2='user_id_col',
        string="Jugadores"
    )