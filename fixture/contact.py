# -*- coding: utf-8 -*-
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(value)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phones.homephone)
        self.change_field_value("mobile", contact.phones.mobilephone)
        self.change_field_value("work", contact.phones.workphone)
        self.change_field_value("fax", contact.phones.faxphone)
        self.change_field_value("email", contact.emails.email1)
        self.change_field_value("email2", contact.emails.email2)
        self.change_field_value("email3", contact.emails.email3)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # press edit
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def edit_first_contact_from_details_page(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # press details
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[7]/a/img").click()
        # press modify on details page
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact)
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
        self.open_contacts_page()
        self.select_first_contact()
        self.delete_selected_contacts()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        self.delete_selected_contacts()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
