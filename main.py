#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Contacts import Contact
from Contacts import list_all_contacts
from addContact import add_new_contact
from editContact import edit_contact
from deleteContact import delete_contact


def main():
    print "Pozdravljeni v vaši kjižici kontaktov"

    # let's add some contacts in our contact list so it's not empty
    john = Contact(first_name="Janez", last_name="Novak", phone_number="02 258 55 77", birth_year="1979", email="janez@novak.si")
    marissa = Contact(first_name="Metka", last_name="Marin", phone_number="03 852 47 14", birth_year="1978", email="metka.marin@gmx.com")
    bruce = Contact(first_name="Sašo", last_name="Bertoncelj", phone_number="01 555 44 89", birth_year="1956", email="saso.bertoncelj@yahoo.com")
    contacts = [john, marissa, bruce]

    while True:
        print ""  # empty line
        print "Prosim izberi si opcijo:"
        print "a) Izpis vseh kontaktov"
        print "b) Dodaj kontaktt"
        print "c) Uredi kotakt"
        print "d) Izbriši kontakt"
        print "e) Zapusti program"
        print ""  # empty line

        selection = raw_input("Izberi opcijo (a, b, c, d or e): ")
        print ""  # empty line

        if selection.lower() == "a":
            list_all_contacts(contacts)
        elif selection.lower() == "b":
            add_new_contact(contacts)
        elif selection.lower() == "c":
            edit_contact(contacts)
        elif selection.lower() == "d":
            delete_contact(contacts)
        elif selection.lower() == "e":
            print "Hvala za uporabo programa, nasvidenje."
            break
        else:
            print "Nisem razumel vaše želje, vpišite ponovno opcijo :"
            continue

if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()
