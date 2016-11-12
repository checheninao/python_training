from model.phones import Phones
from model.emails import Emails
class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None,
                 phones=Phones(), emails=Emails()):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.phones = phones
        self.emails = emails