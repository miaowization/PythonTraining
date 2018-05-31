from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="newgroup1", header="new1", footer="new2"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


