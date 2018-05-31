from sys import maxsize


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, company_address=None,
                 home_telephone=None, mobile_telephone=None, work_telephone=None, fax=None, email1=None, email2=None,
                 email3=None, homepage=None, address=None, home=None, notes=None, id=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.company_address = company_address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address = address
        self.home = home
        self.notes = notes
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
