import argparse
import os
from doorman import Doorman

parser = argparse.ArgumentParser(description='Doorman keeps your secret things')
parser.add_argument('-s', '--secret', action="store_true", dest="status", help='Hide all secret things')
parser.add_argument('-u', '--unsecret', action="store_false", dest="status", help='Unhide all secret things')
parser.add_argument('-c', '--config', action="store", dest="config_file", type=file, help='Config file')

args = parser.parse_args()


def main():
    doorman = Doorman(args.status, os.path.abspath(args.config_file.name))
    doorman.run()

if __name__ == "__main__":
    main()