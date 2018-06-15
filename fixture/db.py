import pymysql
from model.group import Group
from model.contact import Contact
import re

class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password)
        self.connection.autocommit(True)

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, first_name, last_name) = row
                list.append(Contact(id=str(id), first_name=first_name, last_name=last_name))
        finally:
            cursor.close()
        return list

    def get_full_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, lastname, firstname, address, home, mobile, work, phone2, email, email2, email3"
                           " from addressbook WHERE deprecated = 0")
            for row in cursor:
                (id, lastname, firstname, address, home, mobile, work, phone2, email, email2, email3) = row
                list.append(Contact(id=str(id), last_name=re.sub("\s+", " ", lastname).strip(),
                        first_name=re.sub("\s+", " ", firstname).strip(), address=re.sub("\s+", " ", address).strip(),
                        home_telephone=re.sub("\s+", " ", home).strip(),mobile_telephone=re.sub("\s+", " ", mobile).strip(),
                                    work_telephone=re.sub("\s+", " ", work).strip(), secondary_telephone=re.sub("\s+", " ", phone2).strip(),
                                    email1 =re.sub("\s+", " ", email).strip(),
                                    email2=re.sub("\s+", " ", email2).strip(),email3 =re.sub("\s+", " ", email3).strip(),))
        finally:
            cursor.close()
        return list

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()