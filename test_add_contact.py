# -*- coding: utf-8 -*-
import unittest
from contact import Contact
from phones import Phones
from emails import Emails
from application import Application

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_contact(self):
        self.app.login(username="admin", password="secret")
        allphones = Phones(homephone="8(017)2851111", mobilephone="+375297111111", workphone="8(017)2841111",
                           faxphone="8(017)2841111")
        allemails = Emails(email1 = "111@mail.ru", email2 = "222@gmail.com", email3="333@gmail.com")
        self.app.create_new_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov",
                                               nickname="Iva", title="zaq", company="comp1", address="st. Qwerty 1",
                                               phones = allphones, emails = allemails))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
