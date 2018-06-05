import re
import random

def test_phones_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = random.randrange(len((contacts)))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contacts = app.contact.get_contact_list()
    index = random.randrange(len((contacts)))
    contact_from_view_page = app.contact.get_contact_info_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home_telephone == contact_from_edit_page.home_telephone
    assert contact_from_view_page.work_telephone == contact_from_edit_page.work_telephone
    assert contact_from_view_page.mobile_telephone == contact_from_edit_page.mobile_telephone
    assert contact_from_view_page.secondary_telephone == contact_from_edit_page.secondary_telephone


