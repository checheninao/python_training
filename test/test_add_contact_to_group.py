from model.group import Group
from model.contact import Contact
import random


def test_add_contact_to_group(app, dbORM):
    if len(dbORM.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(dbORM.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact1"))
    groups = dbORM.get_group_list()
    group = random.choice(groups)
    contacts = dbORM.get_contact_list()
    contact = random.choice(contacts)
    old_contacts_in_group = dbORM.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact, group)
    if contact not in old_contacts_in_group:
        old_contacts_in_group.append(contact)
    new_contacts_in_group = dbORM.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)

