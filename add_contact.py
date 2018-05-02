# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    contact = Contact(first_name="Contact", middle_name="Contactovich", last_name="Contactov",
                      nickname="Contactik", title="Manager", company="GDC", company_address="Prospect Pobedy",
                      home_telephone="7894584", mobile_telephone="8448558", work_telephone="448454", fax="1448",
                      email1="contact@mail.com", email2="contactik@ya.ru", email3="cont@gmail.com",
                      homepage="contact.ya.ru", address="Lenina 22", home="334475", notes="Do not write here")
    app.login(username="admin", password="secret")
    app.create_contact(contact)
    app.logout()


def test_add_empty_contact(app):
    empty_contact = Contact(first_name="", middle_name="", last_name="", nickname="",
                            title="", company="",
                            company_address="", home_telephone="",
                            mobile_telephone="", work_telephone="", fax="",
                            email1="", email2="", email3="",
                            homepage="", address="", home="", notes="")
    app.login(username="admin", password="secret")
    app.create_contact(empty_contact)
    app.logout()



