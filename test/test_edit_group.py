# -*- coding: utf-8 -*-
from model.group import Group
import random


def test_edit_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group1"))
    old_groups = db.get_group_list()
    modifiable_group = random.choice(old_groups)
    index = old_groups.index(modifiable_group)
    group = Group(name="group2", header="person3", footer="person4")
    group.id = modifiable_group.id
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group2"))
    old_groups = db.get_group_list()
    modifiable_group = random.choice(old_groups)
    index = old_groups.index(modifiable_group)
    group = Group(name="group3")
    group.id = modifiable_group.id
    app.group.edit_group_by_id(group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test_group3"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="person5"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
