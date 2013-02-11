# coding: utf-8

from django.test import TestCase
from eventex.core.models import Contact, Speaker, Talk

class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name= u'Élysson MR', 
            slug='elysson-mr', url='http://google.com')
        s.contact_set.add(Contact(kind = 'E', value = 'elyssonmr@gmail.com'),
            Contact(kind = 'P', value= '35-35353535'),
            Contact(kind = 'F', value = '35-35353535'))

    def test_emails(self):
        'One email should be listed.'
        qs = Contact.emails.all()
        expected = ['<Contact: elyssonmr@gmail.com>']
        self.assertQuerysetEqual(qs, expected)

    def test_phones(self):
        'One phone should be listed.'
        qs = Contact.phones.all()
        expected = ['<Contact: 35-35353535>']
        self.assertQuerysetEqual(qs, expected)

    def test_faxes(self):
        'One fax should be listed.'
        qs = Contact.phones.all()
        expected = ['<Contact: 35-35353535>']
        self.assertQuerysetEqual(qs, expected)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start_time='10:00')
        Talk.objects.create(title='Afternoon Talk', start_time='14:00')

    def test_morning(self):
        'Should return only talks before 12:00'
        self.assertQuerysetEqual(Talk.objects.at_morning(), 
            ['Morning Talk'], lambda t: t.title)

    def test_afternoon(self):
        'Should return only talks after 11:59:59'
        self.assertQuerysetEqual(Talk.objects.at_afternoon(), 
            ['Afternoon Talk'], lambda t: t.title)