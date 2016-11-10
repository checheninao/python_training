# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from phones import Phones
from emails import Emails
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    allphones = Phones(homephone="8(017)2851111", mobilephone="+375297111111", workphone="8(017)2841111",
                    faxphone="8(017)2841111")
    allemails = Emails(email1 = "111@mail.ru", email2 = "222@gmail.com", email3="333@gmail.com")
    app.create_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                                               nickname="Iva", title="zaq", company="comp1", address="st. Qwerty 1",
                                               phones = allphones, emails = allemails))
    app.logout()


