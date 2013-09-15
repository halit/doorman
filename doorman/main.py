import argparse
import os
from doorman import Doorman

DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".doormanrc")
DEFAULT_CONFIG = """[secrets]
test_secret =

[files]
test_secret =
"""

if not os.path.exists(DEFAULT_CONFIG_PATH):
    with open(DEFAULT_CONFIG_PATH, "w") as f:
        f.write(DEFAULT_CONFIG)

parser = argparse.ArgumentParser(description='Doorman keeps your secret things')
parser.add_argument('-s', '--secret', action="store_true", dest="status", help='Hide all secret things')
parser.add_argument('-u', '--unsecret', action="store_false", dest="status", help='Unhide all secret things')
parser.add_argument('-c', '--config', action="store", dest="config_file",
                    default=DEFAULT_CONFIG_PATH, type=file, help='Config file')
args = parser.parse_args()


def main():
    """
    Main function
    """
    if args.config_file.name is DEFAULT_CONFIG_PATH:
        parser.print_help()
    else:
        doorman = Doorman(args.status, os.path.abspath(args.config_file.name))
        doorman.run()


if __name__ == "__main__":
    main()