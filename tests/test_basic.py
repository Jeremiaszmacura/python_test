import unittest
from lab_app.main import APP


class BasicTestCase(unittest.TestCase):
    """This class represents the Basic test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP()

    # def test_smoke_basic(self):
    #     """Test APP has 'run' attribute"""
    #     self.app.run("some_file")

    def tearDown(self):
        """Teardown all initialized variables and close app."""
        pass
