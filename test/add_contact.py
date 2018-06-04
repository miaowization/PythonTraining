from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Contact", middle_name="Contactovich", last_name="Contactov",
                      nickname="Contactik", title="Manager", company="GDC", company_address="Prospect Pobedy",
                      home_telephone="7894584", mobile_telephone="8448558", work_telephone="448454", fax="1448",
                      email1="contact@mail.com", email2="contactik@ya.ru", email3="cont@gmail.com",
                      homepage="contact.ya.ru", address="Lenina 22", secondary_telephone="334475", notes="Do not write here")

    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    empty_contact = Contact(first_name="", middle_name="", last_name="", nickname="",
                            title="", company="",
                            company_address="", home_telephone="",
                            mobile_telephone="", work_telephone="", fax="",
                            email1="", email2="", email3="",
                            homepage="", address="", secondary_telephone="", notes="")
    app.contact.create(empty_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)




