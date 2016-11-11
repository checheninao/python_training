# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_form(self, contact):
        wd = self.app.wd
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phones.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.phones.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.phones.workphone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.phones.faxphone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.emails.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.emails.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.emails.email3)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # press edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def edit_first_contact_from_details_page(self, contact):
        wd = self.app.wd
        self.select_first_contact()
        # press details
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        # press modify on details page
        wd.find_element_by_name("modifiy").click()
        self.fill_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def delete_selected_contacts(self):
        wd = self.app.wd
        # press Delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # submit contact deletion
        wd.switch_to_alert().accept()

    def delete_first_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        self.delete_selected_contacts()

    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        self.delete_selected_contacts()
