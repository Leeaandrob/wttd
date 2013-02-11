# coding: utf-8
from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError

class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(name = u'Élysson MR', 
            slug = 'elysson-mr', url = 'http://google.com',
            description = "Assassins Creed Player")
        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved.'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker representing string shuld be the name'
        self.assertEqual(u'Élysson MR', unicode(self.speaker))

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(name = u'Élysson MR', 
            slug='elysson-mr', url='http://google.com', 
            description='Assassins Creed Player')

    def test_create(self):
        'Email contact should be created.'
        contact = Contact.objects.create(speaker = self.speaker, kind='E',
            value="elyssonmr@gmail.com")
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        'Phone should be created.'
        contact = Contact.objects.create(speaker = self.speaker, kind='P',
            value = '35-35353535')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        'Fax should be created.'
        contact = Contact.objects.create(speaker = self.speaker, kind = 'F',
            value= '35-35353535')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact king should be limited to E, P or F.'
        contact = Contact(speaker = self.speaker, kind = 'A', value = 'B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact String representation should be value.'
        contact = Contact(speaker = self.speaker, kind = 'E', 
            value = 'elyssonmr@gmail.com')
        self.assertEqual('elyssonmr@gmail.com', unicode(contact))