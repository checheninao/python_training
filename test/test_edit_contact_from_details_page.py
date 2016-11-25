# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones
from random import randrange


def test_edit_contact_from_details_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_phones = Phones(homephone="8(017)237333", mobilephone="+3754463333", workphone="8(017)2683333",
                    faxphone="8(017)268333")
    contact_emails = Emails(email1 = "zaq@mail.ru", email2 = "xsw@gmail.com", email3="cde@gmail.com")
    contact = Contact(firstname="Alexei", middlename="Pavlovich", lastname="Pavlov",
                               nickname="APP", title="wer", company="comp3", address="st. Pterty 3",
                               phones=contact_phones, emails = contact_emails)
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index_from_details_page(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)