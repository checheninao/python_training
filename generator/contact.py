from model.contact import Contact
from model.emails import Emails
from model.phones import Phones
import os.path
import string
import random
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

def random_name(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_address(rows_count, row_maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    address = ""
    for i in range(0, rows_count):
        address += "".join([random.choice(symbols) for i in range(random.randrange(row_maxlen))])
        if i != rows_count-1:
            address += "\n"
    return address


def random_email(prefix, name_maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(name_maxlen))]) + "@" \
           + random.choice(["mail", "com", "gmail", "".join([random.choice(symbols) for i in range(random.randrange(10))])]) + "."\
           + random.choice(["ru", "by", "com"])


testdata = [Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Iva", title="zaq",
                    company="comp1", address="st. Qwerty 1",
                    phones=Phones(homephone="8(017)2851111", mobilephone="+375297111111", workphone="8(017)2841111",
                            secondaryphone="285-33-77", faxphone="8(017)2841111"),
                    emails=Emails(email1 = "111@mail.ru", email2 = "222@gmail.com", email3="333@gmail.com"))] + [
            Contact(firstname=random_name("first", 10), middlename=random_name("middle", 20),
                    lastname=random_name("last", 20), address=random_address(4, 10),
                    emails=Emails(email1=random_email("em1", 4), email2=random_email("em2", 7), email3=random_email("em3", 5)))
            for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))