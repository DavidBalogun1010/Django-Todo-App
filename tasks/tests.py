from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Task
from datetime import date

class TaskTests(TestCase):

    def setUp(self):
        # Create a sample task for testing
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test task",
            due_date=date.today(),
            resolved=False
        )

    # --------------------------
    # 1. Test Listing Tasks
    # --------------------------
    def test_task_list_view(self):
        response = self.client.get(reverse('tasks:task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
        self.assertTemplateUsed(response, 'tasks/task_list.html')

    # --------------------------
    # 2. Test Creating Task
    # --------------------------
    def test_create_task(self):
        response = self.client.post(reverse('tasks:task_create'), {
            'title': 'New Task',
            'description': 'Test description',
            'due_date': '2025-12-31',
            'resolved': False,
        })

        self.assertEqual(response.status_code, 302)  # redirect after save
        self.assertEqual(Task.objects.count(), 2)
        self.assertTrue(Task.objects.filter(title='New Task').exists())

    # --------------------------
    # 3. Test Updating Task
    # --------------------------
    def test_update_task(self):
        response = self.client.post(
            reverse('tasks:task_update', args=[self.task.id]),
            {
                'title': 'Updated Task Title',
                'description': 'Updated description',
                'due_date': '2025-12-31',
                'resolved': True,
            }
        )

        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Task Title")
        self.assertTrue(self.task.resolved)

    # --------------------------
    # 4. Test Deleting Task
    # --------------------------
    def test_delete_task(self):
        response = self.client.post(reverse('tasks:task_delete', args=[self.task.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    # --------------------------
    # 5. Test Marking as Resolved
    # --------------------------
    def test_mark_task_resolved(self):
        self.task.resolved = True
        self.task.save()

        task = Task.objects.get(id=self.task.id)
        self.assertTrue(task.resolved)
