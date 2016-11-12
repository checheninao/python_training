# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group2", header="person3", footer="person4"))
    app.session.logout()


def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group3"))
    app.session.logout()


def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="person5"))
    app.session.logout()
