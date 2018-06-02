from model.group import Group
from random import randrange

def test_edit_group_name(app):
    group = Group(name="New Group")
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.edit_group_by_index(group, index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index]=group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     group = Group(header="New Header")
#     old_groups = app.group.get_group_list()
#     group.id = old_groups[0].id
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.edit_first_group(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0]=group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#
# def test_edit_group_footer(app):
#     group = Group(footer="New Footer")
#     old_groups = app.group.get_group_list()
#     group.id = old_groups[0].id
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     app.group.edit_first_group()
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0]=group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
