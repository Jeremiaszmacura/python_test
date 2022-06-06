import unittest
from unittest.mock import patch, Mock

from lab_app.main import APP


class AppTestCase(unittest.TestCase):
    """This class represents the App test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = APP()

    @patch("lab_app.main.DataLoader")
    def test_app_basic(self, data_loader_mock):
        """Test APP generates mail adressess"""

        test_data = [("John", "Smith"), ("Joe", "Doe")]
        data_loader_instance_mock = Mock()
        data_loader_instance_mock.read_data = Mock(return_value=test_data)
        data_loader_mock.return_value = data_loader_instance_mock

        expected_mails = ["john_smith@example.com", "joe_doe@example.com"]

        # example of dummy
        mails = APP().run(Mock())

        self.assertEqual(expected_mails, mails)

    def test_app_basic_spy(self):
        """Test APP generates mail adressess with spy"""
        file_name = "./input_test.csv"
        expected_mails = ["john_smith@example.com", "john_doe@example.com"]

        # Mock as spy
        with patch.object(
            self.app.data_loader, "read_data", wraps=self.app.data_loader.read_data
        ) as wrapped_foo:

            mails = self.app.run(file_name)

            self.assertEqual(expected_mails, mails)

            wrapped_foo.assert_called_with("./input_test.csv")

    def tearDown(self):
        """Teardown all initialized variables and close app."""
        pass
