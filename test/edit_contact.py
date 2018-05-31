from model.contact import Contact


def test_edit_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test", middle_name="test", last_name="test", nickname="test"))
    app.contact.edit_first_contact(Contact(first_name="New first name", middle_name="New middle name",
                                           last_name="New last name"))


