from model.group import Group
from model.contact import Contact
from fixture.orm import ORMFixture
import random
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_to_group(app):
    global db
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="contact1"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    old_contacts_in_group = db.get_contacts_in_group(group)
    app.contact.add_contact_to_group(contact.id, group.id)
    if contact not in old_contacts_in_group:
        old_contacts_in_group.append(contact)
    new_contacts_in_group = db.get_contacts_in_group(group)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)
