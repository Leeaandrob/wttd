# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk

class TalkingListTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(name = u'Élysson MR', slug = 'elysson-mr',
            url = 'http://google.com', 
            description = u'Assassins Creed Player')
        t1 = Talk.objects.create(description = u'Descrição da Palestra', 
            title = u'Título', start_time = '10:00')
        t2 = Talk.objects.create(description = u'Descrição da Palestra', 
            title = u'Título', start_time = '13:00')
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        'GET should return status code 200.'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Template Should be core/talk_list.html'
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        'HTML should list talks.'
        self.assertContains(self.resp, u'Título', 2)
        self.assertContains(self.resp, u'/palestras/1/')
        self.assertContains(self.resp, u'/palestras/2/')
        self.assertContains(self.resp, u'/palestrantes/elysson-mr/', 2)
        self.assertContains(self.resp, u'Assassins Creed Player', 2)
        self.assertContains(self.resp, u'Élysson MR', 2)
        self.assertContains(self.resp, u'Descrição da Palestra', 2)

    def test_morning_talks_in_context(self):
        'Talkings in the morning shoould be in context.'
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        'Talkings in the afternoon shoould be in context.'
        self.assertIn('afternoon_talks', self.resp.context)