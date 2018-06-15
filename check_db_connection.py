import pymysql.cursors
from model.group import Group
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_contacts_in_group(Group(id="130"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
    # db.destroy()
