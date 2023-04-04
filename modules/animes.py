# -*- coding = utf-8 -*-

from odoo import api,models,fields
from odoo.exceptions import ValidationError

class CatalogoAnimes(models.Model):
    _name='catalogo.animes'
    _inherit=['mail.thread','mail.activity.mixin']
    _description='Catalogo Animes'
    
    name = fields.Char(string="Anime",required=True,tracking=True)
    image = fields.Binary(string=" ",required=False)
    state = fields.Selection([
        ('incomplete','Incompleted'),
        ('complete','Completed')
    ],required=False,string="Status")
    sinopsis = fields.Text(string="Sinopsis")
    animes_id = fields.Many2one('catalogo.animes',string="Animes",required=True)
    
    
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            animes=self.env['catalogo.animes'].search([('name','=',rec.name),('id','!=',rec.id)])
            if animes:
                raise ValidationError("Anime %s Already Exist" % rec.name)
            
    def action_complete(self):
        self.state='complete'
        
    def action_incomplete(self):
        self.state='incomplete'
    