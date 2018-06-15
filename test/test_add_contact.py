from model.contact import Contact
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name=first_name, middle_name=middle_name, last_name=last_name,
                    home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                    work_telephone=work_telephone, email1=email1
                    # title=title, company=company, company_address=company_address,
                    #   home_telephone=home_telephone, mobile_telephone=mobile_telephone, work_telephone=work_telephone,
                    #   fax=fax, email1=email1, email2=email2, email3=email3, homepage=homepage, address=address,
                    #   secondary_telephone=secondary_telephone, notes=notes
                    )
            for first_name in ["", random_string("first_name", 10)]
            for middle_name in ["", random_string("middle_name", 10)]
            for last_name in ["", random_string("last_name", 10)]
            for home_telephone in ["", random_digits(10)]
            for mobile_telephone in ["", random_digits(10)]
            for work_telephone in ["", random_digits(10)]
            # for fax in ["", random_digits(10)]
            for email1 in ["", random_string("title", 10)]
            # for email2 in ["", random_string("title", 10)]
            # for email3 in ["", random_string("title", 10)]
            # for homepage in ["", random_string("homepage", 10)]
            # for address in ["", random_string("address", 20)]
            # for secondary_telephone in ["", random_digits(10)]
            # for notes in ["", random_string("notes", 20)]
            # for nickname in ["", random_string("nickname", 10)]
            # nickname=nickname
            # for title in ["", random_string("title", 10)]
            # for company in ["", random_string("company", 5)]
            # for company_address in ["", random_string("company_address", 10)]
]


def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



