# coding: utf-8

from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

class SuccessTest(TestCase):
    def setUp(self):
        self.s = Subscription.objects.create(name = 'Élysson MR',
            cpf = '12345678901', email = 'elyssonmr@gmail.com',
            phone = '35-12345678')
        self.resp = self.client.get(r('subscriptions:success', args=[self.s.pk]))

    def test_get(self):
        'GET /inscricao/1/ should return status_code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Uses Template'
        self.assertTemplateUsed(self.resp, 
            'subscriptions/subscription_detail.html')

    def test_context(self):
        'Context must have a Subscription instance'
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        'Check if subscription data was renderers.'
        self.assertContains(self.resp, self.s.name)

class SuccessNotFoundTest(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:success', args=[0]))
        self.assertEqual(404, resp.status_code)
    