# coding: utf-8

from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Talk

class TalkDetailTest(TestCase):
    def setUp(self):
        t = Talk.objects.create(title = 'Talk', start_time = '10:00')
        t.speakers.create(name = u'Élysson MR', slug = 'elysson-mr')
        self.resp = self.client.get(r('core:talk_detail', args = [1]))

    def test_get(self):
        'Should return Status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Should be rendered core/talk_detail.html'
        self.assertTemplateUsed(self.resp, 'core/talk_detail.html')

    def test_talk_in_context(self):
        'Talk object should be in context'
        talk = self.resp.context['talk']
        self.assertIsInstance(talk, Talk)

    def test_not_found(self):
        'Should not found a talk detail with id 0'
        response = self.client.get(r('core:talk_detail', args = [0]))
        self.assertEqual(404, response.status_code)

#    def test_videos_in_context(self):
#        'videos should be in the context'
#        self.assertIn('videos', self.resp.context)

#    def test_slides_in_context(self):
#        'slides in should be in the context'
#        self.assertIn('slides', self.resp.context)

    def test_html(self):
        'HTML should contain the title, speaker link and his name'
        self.assertContains(self.resp, 'Talk')
        self.assertContains(self.resp, '/palestrantes/elysson-mr')
        self.assertContains(self.resp, u'Élysson MR')