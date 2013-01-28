# coding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""


from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r


class SubcribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:subscribe'))

    def test_get(self):
        'GET / inscricao/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template.'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        'HTML must contain inputs controls.'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp,'type="text"', 4)
        self.assertContains(self.resp, 'type="submit"',)

    def test_csrf(self):
        'HTML must contain a csrf token.'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def teste_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscriberPostTest(TestCase):
    def setUp(self):
        data = dict(name = 'Élysson MR', cpf = '09876543210', 
            email = "elyssonmr@gmail.com", phone = '35-12345678')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Valid Post should redirect to /inscricao/1'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Valid Post must be saved.'
        self.assertTrue(Subscription.objects.exists())

class SubscriberInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name = 'Élysson MR', cpf = '000000000012',
            email = 'elyssonmr@gmail.com', phone = '35-12345678')
        self.resp = self.client.post(r('subscriptions:subscribe'), data)

    def test_post(self):
        'Invalid Post should not redirect'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain erros.'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())