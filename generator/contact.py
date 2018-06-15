from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    symbols = string.digits + "-" + "(" + ")"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", home_telephone="", mobile_telephone="",
                    work_telephone="", email1="")] + [
    Contact(first_name=random_string("first_name", 10), middle_name=random_string("middle_name", 10),
            last_name=random_string("last_name", 10), home_telephone=random_digits(10),
            mobile_telephone=random_digits(10), work_telephone=random_digits(10),
            email1=random_string("email@", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
