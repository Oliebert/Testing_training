from sys import maxsize

class Contact:

    def __init__(self, firstname_of_contact=None, lastname_of_contact=None, contactnickname=None,  contactcompany=None, id=None ):



        self.firstname_of_contact = firstname_of_contact
        #self.middlename_of_contact = middlename_of_contact
        self.lastname_of_contact = lastname_of_contact
        self.contactnickname = contactnickname
        #self.contacttittle = contacttittle
        self.contactcompany = contactcompany
        #self.contactaddress = contactaddress
        #self.homenumber = homenumber
        #self.mobilenumber = mobilenumber
        #self.worknumber = worknumber
        #self.contact_email = contact_email
        #self.contact_fax = contact_fax
        #self.contact_notes = contact_notes
        #self.contact_email2 = contact_email2
        #self.contact_email3 = contact_email3
        #self.contact_homepage = contact_homepage
        #self.contact_address2 = contact_address2
        #self.contact_phone2 = contact_phone2
        self.id = id

    def __repr__(self):
        return "%s:%s:s%" % (self.id, self.firstname_of_contact, self.lastname_of_contact)

    def __eq__(self, other):                                                                            # gruppen sind gleich wenn Namen oder ids sind gleich
                                                                                                        # oder einer der ids ist None
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname_of_contact == other.firstname_of_contact and self.lastname_of_contact == other.lastname_of_contact

    def id_or_max(self):                                                                                # функция вычисляет по группе ключ для сравнения

        if self.id:                                                                                     # если есть идентификатор, то возращается именно он
            return int(self.id)
        else:
            return maxsize                                                                              # еcли нет идентификатора, то присваевается максимально возможное число


''' contactaddress=None, homenumber=None, mobilenumber=None, worknumber=None,
                      contact_email=None, contact_fax=None, contact_notes=None, contact_email2=None, contact_email3=None, contact_homepage=None,
                      contact_address2=None, contact_phone2=None,  middlename_of_contact=None,contacttittle=None,
                     '''
