# -*- coding: utf-8 -*-

db.define_table('bboard',
                Field('name'),
                Field('phone'),
                Field('email'),
                Field('date_posted', 'datetime'),
                Field('message', 'text'),
                )


