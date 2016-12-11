# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones
import random

def test_edit_contact_from_details_page(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact1"))
    old_contacts = db.get_contact_list()
    modifiable_contact = random.choice(old_contacts)
    index = old_contacts.index(modifiable_contact)
    contact_phones = Phones(homephone="8(017)237333", mobilephone="+3754463333", workphone="8(017)2683333",
                            secondaryphone="2888765", faxphone="8(017)268333")
    contact_emails = Emails(email1 = "zaq@mail.ru", email2 = "xsw@gmail.com", email3="cde@gmail.com")
    contact = Contact(firstname="Alexei", middlename="Pavlovich", lastname="Pavlov",
                               nickname="APP", title="wer", company="comp3", address="st. Pterty 3",
                               phones=contact_phones, emails = contact_emails)
    contact.id = modifiable_contact.id
    app.contact.edit_contact_by_id_from_details_page(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)