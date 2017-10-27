#!/usr/bin/env python
# -*- coding: utf-8 -*-

def delete_contact(contacts):
    print "Prosim izberi število kontakta ki bi ga rad izbrisali:"

    for index, person in enumerate(contacts):
        print str(index) + ") " + person.get_full_name()

    print ""  # empty line
    selected_id = raw_input("Kateri kontakt bi radi izbrisali? (vnesi številko ki je pred njim): ")
    selected_contact = contacts[int(selected_id)]

    contacts.remove(selected_contact)
    print ""  # empty line
    print "Kontakt je bil uspešno izbrisan."