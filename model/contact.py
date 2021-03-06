from model.phones import Phones
from model.emails import Emails
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, title=None, company=None,
                 address=None, all_phones_from_home_page=None, phones=Phones(), all_emails_from_home_page=None, emails=Emails()):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.phones = phones
        self.emails = emails
        self.id = id

    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname \
               and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize