from model.contact import Contact
from random import randrange

def test_edit_first_contact_name(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", middle_name="test", last_name="test", nickname="test"))
    app.contact.edit_first_contact(Contact(first_name="New first name", middle_name="New middle name",
                                           last_name="New last name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_random_contact(app):
    contact = Contact(first_name="test", middle_name="test", last_name="test", nickname="test")
    modified_contact = Contact(first_name="New first name", middle_name="New middle name",
                                           last_name="New last name")
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(contact)
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(contact, index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)

