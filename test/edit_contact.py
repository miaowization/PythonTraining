from model.contact import Contact


def test_edit_first_contact_name(app):
    app.contact.edit_first_contact(Contact(first_name="New first name", middle_name="New middle name",
                                           last_name="New last name"))
    app.session.logout()

