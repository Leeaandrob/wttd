# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscrtionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name = u'Élysson MR',
            cpf = '12345678901',
            email = 'elyssonmr@gmail.com',
            phone = '35-98765432'
        )        

    def test_create(self):
        'Subscription mus have name, cpf, email and phone'
        self.obj.save()
        self.assertEqual(1, self.obj.id)

    def test_has_created_at(self):
        'Subscription must have automatic created_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        'Must be the name of subscriptor'
        self.assertEqual(u'Élysson MR', unicode(self.obj))

    def test_paid_default_value_is_false(self):
        'By default paid must be False.'
        self.assertEqual(False, self.obj.paid)

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        Subscription.objects.create(
            name = u'Élysson', 
            cpf = '98765432101',
            email = 'elyssonmr@live.com',
            phone = '35-35353535'
            )

    def test_unique_cpf(self):
        'CPF must bem unique.'
        s = Subscription(name = 'Élysson', cpf = '98765432101',
            email = 'elyssonmr@live.com', phone = '35-35353535')
        self.assertRaises(IntegrityError, s.save)

    def test_unique_can_repeat(self):
        'Email is not unique anymore.'
        s = Subscription(name = 'Élysson', cpf = '98765432131',
            email = 'elyssonmr@live.com', phone = '35-35353535')
        s.save()
        self.assertEqual(2, s.pk)
