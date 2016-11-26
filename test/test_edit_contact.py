# -*- coding: utf-8 -*-
from model.contact import Contact
from model.emails import Emails
from model.phones import Phones
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact1"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_phones = Phones(homephone="8(017)2372222", mobilephone="+3754462222", workphone="8(017)2682222",
                            secondaryphone="2888765", faxphone="8(017)2682222")
    contact_emails = Emails(email1 = "qqq@mail.ru", email2 = "www@gmail.com", email3="eee@gmail.com")
    contact = Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov",
                               nickname="Pet", title="qwe", company="comp2", address="st. Zaq 2",
                               phones=contact_phones, emails=contact_emails)
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_contact_emails(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="contact1"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(emails=Emails(email1="new1@tut.by",email3="new2@tut.by")))
    assert len(old_contacts) == app.contact.count()