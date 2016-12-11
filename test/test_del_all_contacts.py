# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_all_contacts(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact2"))
    app.contact.delete_all_contacts()
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == 0
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == []