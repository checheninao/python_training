# -*- coding: utf-8 -*-
from model.contact import Contact
from model.phones import Phones
from model.emails import Emails
import re


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
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # press edit
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[7].click()
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(contact.id)
        # press edit
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % contact.id).click()
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_first_contact_from_details_page(self, contact):
        self.edit_contact_by_index_from_details_page(0, contact)

    def edit_contact_by_index_from_details_page(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # press details
        wd.find_elements_by_name("entry")[index].find_elements_by_tag_name("td")[6].click()
        # press modify on details page
        wd.find_element_by_name("modifiy").click()
        self.fill_contact_form(contact)
        # submit contact edition
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id_from_details_page(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(contact.id)
        # press details
        wd.find_element_by_css_selector("a[href='view.php?id=%s']" % contact.id).click()
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
        self.return_to_home_page()


    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        self.delete_selected_contacts()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
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
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                                  address=address, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        faxphone = wd.find_element_by_name("fax").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        contact_phones=Phones(homephone=homephone, workphone=workphone, mobilephone=mobilephone,
                              secondaryphone=secondaryphone, faxphone=faxphone)
        all_emails=Emails(email1=email1, email2=email2, email3=email3)
        return Contact(firstname=firstname, lastname=lastname, id=id, phones=contact_phones, address=address, emails=all_emails)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        faxphone = re.search("F: (.*)", text).group(1)
        return Contact(phones=Phones(homephone=homephone, workphone=workphone,
                              mobilephone=mobilephone, secondaryphone=secondaryphone,faxphone=faxphone))


