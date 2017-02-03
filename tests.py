import os
import unittest

from flask import json, Response
from flask.testing import FlaskClient
from werkzeug.utils import cached_property

from config import base_dir
from models import app, db

class MyResponse(Response):
    @cached_property
    def json(self):
        return json.loads(self.data)

class MyTestClient(FlaskClient):
    def open(self, *args, **kwargs):
        if 'json' in kwargs:
            kwargs['data'] = json.dumps(kwargs.pop('json'))
            kwargs['content_type'] = 'application/json'
        return super(MyTestClient, self).open(*args, **kwargs)

app.response_class = MyResponse
app.test_client_class = MyTestClient

class MyTestCase(unittest.TestCase):
    """Setup and teardown for the testing database"""

    TESTS_DB_PATH = os.path.join(base_dir, 'tests.sqlite')

    def setUp(self):

        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + self.TESTS_DB_PATH
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        os.unlink(self.TESTS_DB_PATH)


class ApiTests(MyTestCase):

    def test_1(self):
        pass


if __name__ == '__main__':
    unittest.main()