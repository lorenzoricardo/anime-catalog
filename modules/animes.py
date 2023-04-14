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
    ],required=False,string="Status",default="incomplete")
    sinopsis = fields.Text(string="Sinopsis")
    animes_id = fields.Many2one('catalogo.animes',string="Precuela",required=False)
    caps = fields.Integer(string="Capitulos")
    precuela = fields.Many2one('catalogo.animes',string="Precuela",required=False)
    secuela = fields.Many2one('catalogo.animes',string="Secuela",required=False,default=True)
   
    
    
    @api.constrains('name')
    def check_name(self):
        print(repr(self.precuela))
        for rec in self:
            animes=self.env['catalogo.animes'].search([('name','=',rec.name),('id','!=',rec.id)])
            if animes:
                raise ValidationError("Anime %s Already Exist" % rec.name)
            
    def action_complete(self):
        self.state='complete'
        
    def action_incomplete(self):
        self.state='incomplete'
        
    