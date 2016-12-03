import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phones.homephone == contact_from_edit_page.phones.homephone
    assert contact_from_view_page.phones.workphone == contact_from_edit_page.phones.workphone
    assert contact_from_view_page.phones.mobilephone == contact_from_edit_page.phones.mobilephone
    assert contact_from_view_page.phones.secondaryphone == contact_from_edit_page.phones.secondaryphone
    assert contact_from_view_page.phones.faxphone == contact_from_edit_page.phones.faxphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.phones.homephone,
                                                                 contact.phones.mobilephone, contact.phones.workphone,
                                                                 contact.phones.secondaryphone]))))
