from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <lastname>, <firstname>')
def new_contact(lastname, firstname):
    return Contact(lastname=lastname, firstname=firstname)


@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then('the new contact list is equal to the old list with the added contact')
def verify_group_added(db, contact_list, new_contact, app, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="some contact"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

@given('a new contact data <lastname>, <firstname>')
def new_contact_data(lastname, firstname):
    return Contact(lastname=lastname, firstname=firstname)

@when('I modify the contact from the list')
def edit_contact(app, random_contact, new_contact_data):
    new_contact_data.id = random_contact.id
    app.contact.edit_contact_by_id(new_contact_data)


@then('the new contact list is equal to the old list with changed contact data')
def verify_contact_modificated(db, non_empty_contact_list, random_contact, new_contact_data, app, check_ui):
    old_contacts = non_empty_contact_list
    index = old_contacts.index(random_contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = new_contact_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


@when('I delete all contacts from the list')
def delete_all_contacts(app):
    app.contact.delete_all_contacts()


@then('the new contact list is empty')
def verify_all_contacts_deleted(db, app, check_ui):
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == 0
    if check_ui:
        assert sorted(app.contact.get_contact_list(), key=Contact.id_or_max) == []

