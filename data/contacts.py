from model.contact import Contact
from model.emails import Emails
from model.phones import Phones


testdata = [Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Iva", title="zaq",
                    company="comp1", address="st. Qwerty 1",
                    phones=Phones(homephone="8(017)2851111", mobilephone="+375297111111", workphone="8(017)2841111",
                            secondaryphone="285-33-77", faxphone="8(017)2841111"),
                    emails=Emails(email1 = "111@mail.ru", email2 = "222@gmail.com", email3="333@gmail.com"))
]