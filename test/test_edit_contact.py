# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones


def test_edit_first_contact(app):
    contact_phones = Phones(homephone="8(017)2372222", mobilephone="+3754462222", workphone="8(017)2682222",
                    faxphone="8(017)2682222")
    contact_emails = Emails(email1 = "qqq@mail.ru", email2 = "www@gmail.com", email3="eee@gmail.com")
    app.contact.edit_first_contact(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                               nickname="Pet", title="qwe", company="comp2", address="st. Zaq 2",
                               phones=contact_phones, emails=contact_emails))


def test_edit_contact_emails(app):
    app.contact.edit_first_contact(Contact(emails=Emails(email1="new1@tut.by",email3="new2@tut.by")))