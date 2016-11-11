# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    allphones = Phones(homephone="8(017)2372222", mobilephone="+3754462222", workphone="8(017)2682222",
                    faxphone="8(017)2682222")
    allemails = Emails(email1 = "qqq@mail.ru", email2 = "www@gmail.com", email3="eee@gmail.com")
    app.contact.edit_first_contact(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                               nickname="Pet", title="qwe", company="comp2", address="st. Zaq 2",
                               phones = allphones, emails = allemails))
    app.session.logout()