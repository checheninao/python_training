from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, dbORM):
    if len(dbORM.get_group_list()) == 0:
        app.group.create(Group(name="test2"))
    if len(dbORM.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact2"))
    if len(dbORM.get_group_list_with_contacts()) == 0:
        groups = dbORM.get_group_list()
        group = random.choice(groups)
        contacts = dbORM.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_contact_to_group(contact, group)
        pass
    group = random.choice(dbORM.get_group_list_with_contacts())
    old_contacts_in_group = dbORM.get_contacts_in_group(group)
    contact = random.choice(old_contacts_in_group)
    app.contact.delete_contact_from_group(contact, group)
    old_contacts_in_group.remove(contact)
    new_contacts_in_group = dbORM.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
