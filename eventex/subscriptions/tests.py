"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

#coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubcribeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

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