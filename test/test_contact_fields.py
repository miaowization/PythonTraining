from random import randrange
import re

def test_contact_fields(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len((contacts)))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == \
           app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == \
           app.contact.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name






