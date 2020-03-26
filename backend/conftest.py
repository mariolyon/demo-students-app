import os

import pytest

from app import app as _app
from app import db as _db

basedir = os.path.abspath(os.path.dirname(__file__))

TESTDB = 'test.db'
TESTDB_PATH = "%s/%s" % (basedir, TESTDB)
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH

@pytest.fixture
def client(app):
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    app.config["SQLALCHEMY_DATABASE_URI"] = TEST_DATABASE_URI
    _db.create_all()
    _db.app = app
    yield app.test_client()

@pytest.fixture(autouse=True, scope='session')
def setup(request):
    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    request.addfinalizer(teardown)

@pytest.fixture
def app():
    """Yield app with its context set up and ready"""
    with _app.app_context():
        yield _app
