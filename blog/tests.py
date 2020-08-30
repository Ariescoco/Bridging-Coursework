from django.urls import resolve, reverse
from django.test import TestCase
from django.apps import apps
from django.contrib.auth.models import User
from .models import info, work, education, voluneering, skills
from .views import cv 
# Create your tests here.

class CVTest(TestCase):
    def setUp(self):

        self.info = info.objects.create(text = 'test info')
        self.work = work.objects.create(text = 'test work')
        self.education = education.objects.create(text = 'test education')
        self.voluneering = voluneering.objects.create(text = 'test voluneering')
        self.skills = skills.objects.create(text = 'test skills')

        self.url = '/cv/'
        self.url_add = '/cv/new_cv/'

    def test_model_test_info(self):
        self.assertEqual(self.info.__str__(), self.info.text)

    def test_model_test_work(self):
        self.assertEqual(self.work.__str__(), self.work.text)

    def test_model_test_education(self):
        self.assertEqual(self.education.__str__(), self.education.text)

    def test_model_test_voluneering(self):
        self.assertEqual(self.voluneering.__str__(), self.voluneering.text)

    def test_model_test_skills(self):
        self.assertEqual(self.skills.__str__(), self.skills.text)                        

    def test_guest_add_cv(self):
        response = self.client.post(self.url_add)
        # User should be redirect to login page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/accounts/login/?next=/cv/new_cv/')

