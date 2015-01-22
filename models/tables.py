# -*- coding: utf-8 -*-
from datetime import datetime


def get_first_name():
    name = 'Nobody'
    if auth.user:
        name = auth.user.first_name
    return name

def get_email():
    name = 'Nobody'
    if auth.user:
        name = auth.user.email
    return name



CATEGORY = ['Car', 'Bike', 'Books', 'Music', 'Outdoors', 'For the house', 'Misc.']
STATUS = [True,False]

# This is the main table, containing the posts.
db.define_table('bboard',
                Field('user_id', db.auth_user),
                Field('date_posted', 'datetime'),
                Field('name'),
                Field('phone'),
                Field('email'),
                Field('category'),
                Field('sold'),
                Field('price'),                
                Field('title'),
                Field('bbmessage', 'text'),
                Field('Image', 'upload'),
                )

db.bboard.id.readable = False
db.bboard.bbmessage.label = 'Message'
db.bboard.name.default = get_first_name()
db.bboard.email.default = get_email()
db.bboard.sold.required = True
db.bboard.sold.default = False
db.bboard.date_posted.default = datetime.utcnow()
db.bboard.name.writable = False
db.bboard.email.writable = False
db.bboard.date_posted.writable = False
db.bboard.user_id.default = auth.user_id
db.bboard.user_id.writable = db.bboard.user_id.readable = False
db.bboard.email.requires = IS_EMAIL()
db.bboard.category.requires = IS_IN_SET(CATEGORY)
db.bboard.sold.requires = IS_IN_SET(STATUS)
db.bboard.category.default = 'Misc.'
db.bboard.category.notnull = True
db.bboard.sold.notnull = True
db.bboard.sold.notnull = True
db.bboard.price.requires = IS_FLOAT_IN_RANGE(0, 100000.0, error_message='The price should be in the range 0..100000')
db.bboard.category.required = True
db.bboard.sold.writable = False
db.bboard.sold.default = False


db.bboard.price.requires = IS_MATCH('(?=.*\d)\d{0,6}(\.\d{1,2})?$', error_message='Invalid price.')
db.bboard.phone.requires = IS_MATCH('^1?(-?\d{3}-?|\(\d{3}\))\d{3}-?\d{4}$', error_message='Invalid phone number.')



