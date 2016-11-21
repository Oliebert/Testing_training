# -*- coding: utf-8 -*-


from model.contact import Contact

def test_add_contact(app):

    old_contacts = app.contact.get_contact_list()

    contact = Contact(firstname_of_contact="nk",
                      lastname_of_contact="kh",
                      contactnickname="kb",
                      contactcompany="lk", )

    app.contact.create_contact(contact)

    new_contacts = app.contact.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

'''
def test_add_empty_contact(app):

    app.contact.create_contact(Contact(firstname_of_contact="", middlename_of_contact="",
                                        lastname_of_contact="", contactnickname="",

                                        contacttittle="", contactcompany="", contactaddress="",
                                        homenumber="", mobilenumber="",

                                        worknumber="", contact_email="", contact_fax="", contact_notes="",
                                        contact_email2="",

                                        contact_email3="", contact_homepage="", contact_address2="",
                                        contact_phone2=""))
'''

