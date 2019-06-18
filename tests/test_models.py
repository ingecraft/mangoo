import unittest
from flask import current_app
from app import create_app, db
from app.models import User, Lead, Call, Donation, Pass, Callback

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_model_creation(self):
        u1 = User()
        l1 = Lead()
        c1 = Call()
        d1 = Donation()
        p1 = Pass()
        cb1 = Callback()
        self.assertTrue(True)



