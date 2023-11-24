from django.test import TestCase

class BlogAppTest(TestCase):
    def test_index(self):
        """Test that the index page loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world. You're at the blog_app index.")

    def test_about(self):
        """Test that the about page loads correctly."""
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the about page.")