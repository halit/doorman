import yaml, os, logging

class DoormanException(Exception):
    """
    Doorman exception class
    """
    def __init__(self, name, message):
        """
        DoormanException class constructor
        :param name: string
        """
        self.name = name
        self.message = message

        Exception.__init__(self, '%s: %s' % (self.name,self.message))


class DoormanConfig(object):
    """
    Doorman config class
    """
    def __init__(self, config_file):
        """
        DoormanConfig class constructor
        :param config_file: file path
        """
        self.__config_file = config_file
        self.__configs = []

    def parseYAML(self):
        """
        Config parser method for parsing YAML
        :return type: list of dict(name, secret, file_name)
        """
        with open(self.__config_file, "r") as f:
            lines = f.read()

        try:
            self.__configs = yaml.load(lines)
        except yaml.scanner.ScannerError, e:
            raise DoormanException("Error parsing config YAML", e)

        if self.__configs is None:
            raise DoormanException("Error: empty config", None)

        for location in self.__configs:
            if not os.path.exists(location):
                raise DoormanException("File in config not found", location)


        return self.__configs;

class Doorman(object):
    """
    Doorman main class
    """
    def __init__(self, status, config_file):
        """
        Doorman main class constructor
        :param status: boolean flag
        :param config_file: file path
        """
        self.__status = status
        self.__config = DoormanConfig(config_file).parseYAML()

    def run(self):
        """
        Doorman runner method
        """
        if self.__status:
            self.__hide()
        else:
            self.__unhide()

    def __open_and_replace(self, file_path, old, new):
        """
        Method for open and raplace old string with new string
        :param file_path: file path
        :param old: old string
        :param new: new string
        """
        try:
            with open(file_path, "r") as f:
                full_text = f.read()
        except IOError:
            raise DoormanException("File not read", str(file_path))


        full_text = full_text.replace(old, new)

        try:
            with open(file_path, "w") as f:
                f.write(full_text)
        except IOError:
            raise DoormanException("File not write", str(file_path))

    def __wrapper(self, s):
        """
        Wrapper method for strings
        :param s: string to be wrapped
        :return type: string
        """
        return "{{" + s + "}}"

    def __hide(self):
        """
        Method for hide all secret things
        """
        for location, replacevalues in self.__config.items():
            for name, secret in replacevalues.items():
                self.__open_and_replace(location,
                                        secret,
                                        self.__wrapper(name))
                logging.info("hide: %s" % location)

    def __unhide(self):
        """
        Method for unhide all secret things
        """
        for location, replacevalues in self.__config.items():
            for name, secret in replacevalues.items():
                self.__open_and_replace(location,
                                        self.__wrapper(name),
                                        secret)
                logging.info("unhide: %s" % location)