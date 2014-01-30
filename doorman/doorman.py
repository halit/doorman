class DoormanError(Exception):
    """
    Doorman exception class
    """
    def __init__(self, name):
        """
        DoormanException class constructor
        :param name: string
        """
        self.name = name

    def __repr__(self):
        """
        DoormanException repr method
        """
        return "<", self.name, ">"


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

    def parse(self):
        """
        Config parser method
        :return type: list of dict(name, secret, file_name)
        """
        with open(self.__config_file, "r") as f:
            lines = f.read()

        lines = [line.split(">>") for line in lines.splitlines()
                 if not line.startswith("#") and line]
        for line in lines:
            name, secret, file_path = line
            self.__configs.append(dict(name=name.strip(),
                                       secret=secret.strip(),
                                       file_path=file_path.strip()))
            return self.__configs


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
        self.__config = DoormanConfig(config_file).parse()

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
            raise DoormanError("File not read", str(file_path))

        full_text = full_text.replace(old, new)

        try:
            with open(file_path, "w") as f:
                f.write(full_text)
        except IOError:
            raise DoormanError("File not write", str(file_path))

    def __wrapper(self, s):
        """
        Wrapper method for strings
        :param s: string to will be wrap
        :return type: string
        """
        return "{{" + s + "}}"

    def __hide(self):
        """
        Method for hide all secret things
        """
        for config in self.__config:
            self.__open_and_replace(config['file_path'],
                                    config['secret'],
                                    self.__wrapper(config['name']))
            print "# " + "hide:" + " " + config['file_path']

    def __unhide(self):
        """
        Method for unhide all secret things
        """
        for config in self.__config:
            self.__open_and_replace(config['file_path'],
                                    self.__wrapper(config['name']),
                                    config['secret'])
            print "# " + "unhide:" + " " + config['file_path']
