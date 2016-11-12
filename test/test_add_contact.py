# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones


def test_add_contact(app):
    contact_phones = Phones(homephone="8(017)2851111", mobilephone="+375297111111", workphone="8(017)2841111",
                    faxphone="8(017)2841111")
    contact_emails = Emails(email1 = "111@mail.ru", email2 = "222@gmail.com", email3="333@gmail.com")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                               nickname="Iva", title="zaq", company="comp1", address="st. Qwerty 1",
                               phones=contact_phones, emails=contact_emails))


