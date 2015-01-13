# -*- coding: utf-8 -*-

db.define_table('bboard',
                Field('name'),
                Field('phone'),
                Field('email'),
                Field('date_posted', 'datetime'),
                Field('bbmessage', 'text'),
                )

db.bboard.bbmessage.label = 'Message'


