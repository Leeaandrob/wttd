# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker

class SpeakerDetailTest(TestCase):
    def setUp(self):
        Speaker.objects.create(name = u'Élysson MR',
            slug = 'elysson-mr',
            url = 'http://google.com',
            description = "Assassins Creed Player")
        url = r('core:speaker_detail', kwargs={'slug' : 'elysson-mr'})
        self.resp = self.client.get(url)

    def test_get(self):
        'Get should result in 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template should be core/speaker_detail'
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        'HTML must contain data.'
        self.assertContains(self.resp, u'Élysson MR')
        self.assertContains(self.resp, "Assassins Creed Player")
        self.assertContains(self.resp, 'http://google.com')

    def test_context(self):
        'Speaker must be in the context'
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)

class SpeakerDetailNotFound(TestCase):
    def test_not_found(self):
        'Should return 404'
        url = r('core:speaker_detail', kwargs = {'slug' : 'larinha'})
        response = self.client.get(url)
        self.assertEqual(404, response.status_code)
        