#-*- coding = utf=8 -*-

from odoo import api,fields,models
from odoo.exceptions import ValidationError

class CatalogoSee(models.Model):
    _name="catalogo.see"
    _description="Animes To See"
    
    name=fields.Char(string="Name",required=True)
    state=fields.Selection([
        ('airing','Airing'),
        ('finished','Finished')
    ],required=True,string='Status')
    
    @api.constrains('name')
    def check_name(self):
        for rec in self:
            see=self.env['catalogo.see'].search([('name','=',rec.name),('id','!=',rec.id)])
            if see:
                raise ValidationError("Name is Already Taken")