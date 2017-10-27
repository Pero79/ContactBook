#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Contacts import Contact

def add_new_contact(contacts):
    first_name = raw_input("Prosim vnesite kotaktovo ime: ")
    last_name = raw_input("Prosim vnesite kotaktov priimek: ")
    email = raw_input("Prosim vnesite kotaktov e-poštni naslov: ")
    phone = raw_input("Prosim vnesite kotaktovo telefonsko številko: ")
    birth_year = raw_input("Prosim vnesite kotaktovo letnico rojstva: ")

    new = Contact(first_name=first_name, last_name=last_name, phone_number=phone, birth_year=birth_year, email=email)
    contacts.append(new)

    print ""  # empty line
    print new.get_full_name() + " je bil uspešno ddodan na vašo kontaktno listo."