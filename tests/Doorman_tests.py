import unittest, tempfile, os
from doorman.doorman import Doorman, DoormanException

class DoormanTest(unittest.TestCase):
    """
    Doorman test class
    """
    def setUp(self):
        self.yml = tempfile.NamedTemporaryFile()
        self.txt = tempfile.NamedTemporaryFile()
        self.txt2 = tempfile.NamedTemporaryFile()

        self.yml.write("""%s:
 pass: yaml""" % self.txt.name)
        self.yml.seek(0)

    def test_doorman_hide(self):
        self.txt.write("""ayamlb""")
        self.txt.seek(0)

        dm = Doorman(True, self.yml.name)

        dm.run()

        self.assertEqual("a{{pass}}b", self.txt.read())

    def test_doorman_unhide(self):
        self.txt.write("a{{pass}}b")
        self.txt.seek(0)

        dm = Doorman(False, self.yml.name)
        dm.run()

        self.assertEqual("ayamlb", self.txt.read())

    def test_doorman_nohide(self):
        self.txt.write("hello")
        self.txt.seek(0)

        dm = Doorman(False, self.yml.name)
        dm.run()

        self.assertEqual("hello", self.txt.read())

    def test_doorman_readfail(self):
        os.chmod(self.txt.name, 0o200)

        dm = Doorman(True, self.yml.name)
        with self.assertRaises(DoormanException) as e:
            dm.run()

        self.assertEqual(e.exception.name, "File not read")

    def test_doorman_writefail(self):
        os.chmod(self.txt.name, 0o400)

        dm = Doorman(True, self.yml.name)
        with self.assertRaises(DoormanException) as e:
            dm.run()

        self.assertEqual(e.exception.name, "File not write")
