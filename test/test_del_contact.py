# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


def test_delete_some_contact(app, db, check_ui):
    with pytest.allure.step('Given a non-empty contact list'):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="contact1"))
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Given a random contact from the list'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('When I delete the contact %s from the list' % contact):
        app.contact.delete_contact_by_id(contact.id)
    with pytest.allure.step('Then the new contact list is equal to the old list without the deleted contact'):
        new_contacts = db.get_contact_list()
        assert len(old_contacts) - 1 == len(new_contacts)
        old_contacts.remove(contact)
        assert old_contacts == new_contacts
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
