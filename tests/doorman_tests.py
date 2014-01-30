import doorman
import unittest

class DoormanTest(unittest.TestCase):
    """
    Doorman test class
    """
    def setUp(self):
        self.config = [{"name":"twitter",
                        "secret": "123456",
                        "file_path":"twitter"},
                       {"name":"facebook",
                        "secret":"12345678",
                        "file_path":"facebook"}]

    def test_doorman_config_type(self):
        self.assertIsInstance(self.config[0], dict)

    def test_doorman_config(self):
        self.assertIsInstance(self.config, list)

    def test_doorman_config_len(self):
        self.assertEqual(len(self.config), 2)
