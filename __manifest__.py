{
    'name' : 'Catalogo Management',
    'version' : '1.0',
    'summary' : 'Catalogo Management Software',
    'sequence' : 10,
    'description' : """Catalogo Management Software""",
    'category' : 'Productivity',
    'website' : 'https://www.odomates.tech',
    'license' : 'LGPL-3',
    'depends' : [
        'mail'
        ],
    'data' : [
        'security/ir.model.access.csv',
        'data/data.xml', 
        'views/menus.xml',
        #'views/catalogo_view.xml',
        'views/animes_view.xml'
        ],
    'demo' : [],
    'qweb' : [],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}