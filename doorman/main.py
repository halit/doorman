import argparse
import os
from doorman import Doorman

DEFAULT_CONFIG_PATH = os.path.join(os.path.expanduser("~"), ".doormanrc")
DEFAULT_CONFIG = """test_secret >> my secret thing >> test_file"""

if not os.path.exists(DEFAULT_CONFIG_PATH):
    with open(DEFAULT_CONFIG_PATH, "w") as f:
        f.write(DEFAULT_CONFIG)


def is_default_config():
    return open(DEFAULT_CONFIG_PATH, "r").read() == DEFAULT_CONFIG

parser = argparse.ArgumentParser(description='Doorman keeps your secret things')
parser.add_argument('-s', '--secret', action="store_true", dest="status", help='Hide all secret things')
parser.add_argument('-u', '--unsecret', action="store_false", dest="status", help='Open all secret things')
parser.add_argument('-c', '--config', action="store", dest="config_file",
                    default=DEFAULT_CONFIG_PATH, type=file, help='Config file')
args = parser.parse_args()


def main():
    """
    Main function
    """

    if not is_default_config():
        print "# running" + args.config_file.name + " config file"
        doorman = Doorman(args.status, os.path.abspath(args.config_file.name))

        if args.status:
            print "# hide all secret things"
        else:
            print "# open all secret things"

        doorman.run()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()