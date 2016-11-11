# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="group2", header="person3", footer="person4"))
    app.session.logout()