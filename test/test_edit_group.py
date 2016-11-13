# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group1"))
    app.group.edit_first_group(Group(name="group2", header="person3", footer="person4"))


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group2"))
    app.group.edit_first_group(Group(name="group3"))


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group3"))
    app.group.edit_first_group(Group(header="person5"))
