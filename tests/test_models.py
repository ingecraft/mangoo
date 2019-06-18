import unittest
from flask import current_app
from app import create_app, db
from app.models import User

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_user_model(self):
        u1 = User()
        self.assertTrue(True)

