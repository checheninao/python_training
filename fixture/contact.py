# -*- coding: utf-8 -*-
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contacts_page(self):
        wd = self.app.wd
        if not ((wd.current_url.endswith("/addressbook/") or wd.current_url.endswith("/addressbook/index.php"))
                and len(wd.find_elements_by_link_text("Last name")) > 0):
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
        self.return_to_home_page()
        self.contact_cache = None

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
        self.return_to_home_page()
        self.contact_cache = None

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
        self.return_to_home_page()
        self.contact_cache = None

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
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        self.delete_selected_contacts()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def return_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_link_text("home page")) > 0:
            wd.find_element_by_link_text("home page").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            rows = wd.find_elements_by_name("entry")
            for row in rows:
                row_id = row.find_element_by_name("selected[]").get_attribute("id")
                cells = row.find_elements_by_tag_name("td")
                self.contact_cache.append(Contact(lastname=cells[1].text, firstname=cells[2].text, id=row_id))
        return list(self.contact_cache)