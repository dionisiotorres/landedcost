# -*- coding: utf-8 -*-

{
    "name": "Optica SV2",
    "category": 'Sales',
    "summary": """
       Localizacion de Opticas .""",
    "description": """
	   Registra la orden de produccion para un laboratorio optico
	
    """,
    "sequence": 1,
    "author": "Strategi-k",
    "website": "http://strategi-k.com",
    "version": '12.0.0.4',
    "depends": ['sale','stock','sale_stock'],
    "data": [
        'security/ir.model.access.csv'
    ],
    "installable": True,
    "application": True,
    "auto_install": False,

}
