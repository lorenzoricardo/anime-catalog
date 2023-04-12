# -*- coding = utf-8 -*-

from odoo import api,fields,models

class Catalogo(models.Model):
    _name="catalogo.catalogo"
    _inherit=['mail.thread','mail.activity.mixin']
    _description="Catalogo"
    
   
    image=fields.Binary(string="Image")
   
    