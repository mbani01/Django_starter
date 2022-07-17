from django.test import TestCase
# Create your tests here.

class homeTest(TestCase):
	def test_home_status_code(self):
		print("")
		response = self.client.get('/boards', follow=True)
		self.assertEqual(response.status_code, 200)