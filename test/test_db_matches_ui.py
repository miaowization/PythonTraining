from model.group import Group
from model.contact import Contact
from timeit import timeit

def test_group_list(app, db):
    print(timeit(lambda : app.group.get_group_list(), number=1))
    def clean(group):
        return Group(id=group.id, name= group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    assert False

def test_contact_list(app, db):
    print(timeit(lambda : app.contact.get_contact_list(), number=1))
    def clean(contact):
        return Contact(id=contact.id, first_name=contact.first_name.strip())
    print(timeit(lambda: map(clean, db.get_contact_list()), number=1000))
    assert False


    # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)