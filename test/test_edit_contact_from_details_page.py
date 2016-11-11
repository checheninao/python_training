# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    allphones = Phones(homephone="8(017)237333", mobilephone="+3754463333", workphone="8(017)2683333",
                    faxphone="8(017)268333")
    allemails = Emails(email1 = "zaq@mail.ru", email2 = "xsw@gmail.com", email3="cde@gmail.com")
    app.contact.edit_first_contact_from_details_page(Contact(firstname="Alexei", middlename="Pavlovich", lastname="Pavlov",
                               nickname="APP", title="wer", company="comp3", address="st. Pterty 3",
                               phones = allphones, emails = allemails))
    app.session.logout()