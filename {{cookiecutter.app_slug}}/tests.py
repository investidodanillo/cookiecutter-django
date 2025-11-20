from django.test import TestCase

class SmokeTest(TestCase):
    def test_imports(self):
        from . import models
        from . import views
        self.assertTrue(True)
