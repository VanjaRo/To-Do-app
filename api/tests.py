from django.test import TestCase
from .models import Task


class TaskModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='first todo', body='a body here')

    def test_title_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEquals(expected_object_name, 'first todo')

    def test_body_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.body}'
        self.assertEquals(expected_object_name, 'a body here')
