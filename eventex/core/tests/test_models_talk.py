# coding: utf-8

from django.test import TestCase
from eventex.core.models import Talk, Course
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title = u'Introdução ao Django',
            description = u'Descrição da Palestra.',
            start_time = '10:00')

    def test_create(self):
        'Talk should be Created'
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        'Unicode should be Talk.title'
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_speaker(self):
        'A talk has many Speakers and vice-versa'
        self.talk.speakers.create(name = u'Élysson MR', 
            slug = 'elysson-mr', 
            url = 'http://google.com')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        'Talk default manager must be a instance of PeriodManager'
        self.assertIsInstance(Talk.objects, PeriodManager)


class CourseModelTest(object):
    def setUp(self):
        self.course = Course.objects.create(title = 'Tutorial Python',
            description = u'Descrição do Curso', start_time = '10:00', slots = 10)

    def test_create(self):
        'Course Should be contain a PK.'
        self.assertEqual(1, self.course.pk)

    def test_unicode(self):
        'Course Unicode should be its title'
        self.assertEqual('Tutorial Python', unicode(self.course))

    def test_speakers(self):
        'Couse should contain at least one Speaker'
        self.course.speakers.create(name = u'Élysson MR',slug = 'elysson-mr', 
            url = 'http://google.com')
        self.assertEqual(1, self.course.speakers.count())

    def test_period_manager(self):
        'Course default manager must be instance of PeriodManager'
        self.assertIsInstance(Couse.objects, PeriodManager)