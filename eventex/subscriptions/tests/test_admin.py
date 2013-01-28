# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin
from mock import Mock

class MarkAsPaidTest(TestCase):
    def setUp(self):
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)
        Subscription.objects.create(name=u'Élysson MR', cpf='12345678901', email='elyssonmr@gmail.com')

    def test_has_action(self):
        'Action is not installed.'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'Everyone must be marked as paid'
        fake_request = Mock()
        queryset = Subscription.objects.all()
        self.model_admin.mark_as_paid(fake_request, queryset)

        self.assertEqual(1, Subscription.objects.filter(paid=True).count())