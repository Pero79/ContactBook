#!/usr/bin/env python
# -*- coding: utf-8 -*-

def edit_contact(contacts):
    print "Prosim izberi število kontakta ki bi ga rad uredili:"

    for index, person in enumerate(contacts):
        print str(index) + ") " + person.get_full_name()

    print ""  # empty line
    selected_id = raw_input("Kateri kontakt bi radi uredili? (vnesi številko ki je pred njim): ")
    selected_contact = contacts[int(selected_id)]

    new_email = raw_input("Prosim vnesite novo e-poštni za %s: " % selected_contact.get_full_name())
    selected_contact.email = new_email

    print ""  # empty line
    print "E-pošta popravljena."
    # ... you can do the same for other fields.