from django.test import TestCase
from .models import Contact


class TestContactModels(TestCase):
    """
    A class for testing product models
    """
    def setUp(self):
        """
        Create test reason, name, email and body
        """

        Contact.objects.create(
            reason='test_reason',
            name='test_name',
            email='test@email,.com',
            body='test_message'
        )

    def tearDown(self):
        """
        Delete the test reason, name, email and body
        """
        Contact.objects.all().delete()

    def test_course_str_method(self):
        """
        This test tests the contact string
        """
        contact = Contact.objects.get(name='test_name')
        self.assertEqual((contact.__str__()), contact.name)
