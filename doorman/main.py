import argparse, os, logging, appdirs
from doorman import Doorman, DoormanException

DEFAULT_CONFIG_PATH = appdirs.user_config_dir("doorman")
DEFAULT_CONFIG_FILE = os.path.join(DEFAULT_CONFIG_PATH, "doorman.yml")
DEFAULT_CONFIG = """test_file:
 test_secret: my secret thing"""

if not os.path.exists(DEFAULT_CONFIG_PATH):
    os.makedirs(DEFAULT_CONFIG_PATH)

if not os.path.exists(DEFAULT_CONFIG_FILE):
    with open(DEFAULT_CONFIG_FILE, "w") as f:
        f.write(DEFAULT_CONFIG)
    os.chmod(DEFAULT_CONFIG_FILE, 0o600)


def is_default_config():
    return open(DEFAULT_CONFIG_FILE, "r").read() == DEFAULT_CONFIG

parser = argparse.ArgumentParser(description='Doorman keeps your secret things')
parser.set_defaults(status=True)
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('-u', '--unsecret', action="store_false", dest="status", help='Open all secret things')
group.add_argument('-s', '--secret', action="store_true", dest="status", help='Hide all secret things')
parser.add_argument('-v', '--verbose', action="store_true", dest="verbose", help='Show all messages')
parser.add_argument('-c', '--config', action="store", dest="config_file",
                    default=DEFAULT_CONFIG_PATH, help='Config file')
args = parser.parse_args()


def main():
    """
    Main function
    """

    if args.verbose:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.WARN)

    if not is_default_config():
        try:
            doorman = Doorman(args.status, os.path.abspath(args.config_file))
            doorman.run()
        except DoormanException, e:
            logging.error(e)
            parser.print_help()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
