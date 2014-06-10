import unittest, tempfile

from doorman.doorman import DoormanConfig, DoormanException

"""
Test the parseYAML function in the Doorman class
"""
class DoormanConfigTest(unittest.TestCase):
    """
    Setup the temporary files
    """
    def setUp(self):
        self.yml = tempfile.NamedTemporaryFile()
        self.txt = tempfile.NamedTemporaryFile()
        self.txt2 = tempfile.NamedTemporaryFile()

    def test_parseYAML_one_password(self):
        self.yml.write("""%s:
 pass: yaml""" % self.txt.name)
        self.yml.seek(0)

        parsed = DoormanConfig(self.yml.name).parseYAML()

        self.assertEqual(parsed, {self.txt.name: {'pass': 'yaml'}})

    def test_parseYAML_multiple_passwords(self):
        self.yml.write("""%s:
 pass: yaml
 pass2: yaml2""" % self.txt.name)
        self.yml.seek(0)

        parsed = DoormanConfig(self.yml.name).parseYAML()

        self.assertEqual(parsed, {self.txt.name: {'pass': 'yaml', 'pass2': 'yaml2'}})

    def test_parseYAML_multiple_files(self):
        self.yml.write("""%s:
 pass: yaml
%s:
 pass2: yaml2""" % (self.txt.name, self.txt2.name))
        self.yml.seek(0)

    def test_parseYAML_empty(self):
        with self.assertRaises(DoormanException) as e:
            parsed = DoormanConfig(self.yml.name).parseYAML()

        self.assertEqual(e.exception.name, "Error: empty config")

    def test_parseYAML_invalid(self):
        self.yml.write("\t")
        self.yml.seek(0)

        with self.assertRaises(DoormanException) as e:
            parsed = DoormanConfig(self.yml.name).parseYAML()

        self.assertEqual(e.exception.name, "Error parsing config YAML")

    def test_parseYAML_not_found(self):
        self.txt.close() # removes the file
        self.yml.write("""%s:
 pass: yaml""" % self.txt.name)
        self.yml.seek(0)

        with self.assertRaises(DoormanException) as e:
            parsed = DoormanConfig(self.yml.name).parseYAML()

        self.assertEqual(e.exception.name, "File in config not found")
