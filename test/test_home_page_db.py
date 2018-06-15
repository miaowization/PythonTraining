import re

def test_phones_on_home_page(app, db):
    contacts_from_db = db.get_full_contact_list()
    contacts_from_home_page = app.contact.get_contact_list()
    for contact_from_db in contacts_from_db:
        id = contact_from_db.id
        for contact_from_home_page in contacts_from_home_page:
            if contact_from_home_page.id == id:
                assert contact_from_home_page.last_name == clear(contact_from_db.last_name)
                assert contact_from_home_page.first_name == clear(contact_from_db.first_name)
                assert contact_from_home_page.address == clear(contact_from_db.address)
                assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
                assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)

def clear(s):
    return re.sub(" [()-]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.secondary_telephone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email1, contact.email2, contact.email3]))))