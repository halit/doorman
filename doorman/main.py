import argparse

parser = argparse.ArgumentParser(description='Doorman keeps your secret things')
parser.add_argument('-s','--secret', action="store_true", dest="status", help='Hide all secret things')
parser.add_argument('-u','--unsecret', action="store_false", dest="status", help='Unhide all secret things')

args = parser.parse_args()

def main():
    if args.status:
        print "Hide all things!"
    else:
        print "Unhide all things!"

if __name__ == "__main__":
    main()