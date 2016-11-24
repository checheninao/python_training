# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact_phones = Phones(homephone="8(017)2851111", mobilephone="+375297111111", workphone="8(017)2841111",
                    faxphone="8(017)2841111")
    contact_emails = Emails(email1 = "111@mail.ru", email2 = "222@gmail.com", email3="333@gmail.com")
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                               nickname="Iva", title="zaq", company="comp1", address="st. Qwerty 1",
                               phones=contact_phones, emails=contact_emails)
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

