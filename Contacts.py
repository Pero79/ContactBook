#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Contact:
    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.birth_year = birth_year
        self.email = email

    def get_full_name(self):
        return self.first_name + " " + self.last_name


def list_all_contacts(contacts):
    for index, person in enumerate(contacts):
        print "ID: " + str(index)  # index is an order number of the contact object in the contacts list
        print person.get_full_name()
        print person.birth_year
        print person.email
        print ""  # empty line

    if not contacts:
        print "Nimate nobenih kontaktov  na vaši listi."







