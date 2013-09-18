class Config:
    """
    Config class
    """

    def __init__(self, config_file):
        """
        Initialize Config class

        :param config_file: full path for config file
        """

        self.config_file = config_file
        self.configs = list()

    def parse(self):
        """
        Parser method for Config class
        It parse config file to dict
        """

        with open(self.config_file, "r") as f:
            lines = f.read()

        lines = [line.split(">>") for line in lines.splitlines() if not line.startswith("#") and line]
        for line in lines:
            name, secret, file_p = line
            self.configs.append(dict(name=name.strip(),
                                     secret=secret.strip(),
                                     file=file_p.strip()))

        return self.configs


class Doorman:
    """
    Doorman main class
    """

    def __init__(self, status, config_file):
        """
        Initialize Doorman class

        :param status: boolean value for hide or unhide
        :param config_file: config file for parse
        """

        self.status = status
        self.config = Config(config_file).parse()

    def run(self):
        """
        Run method for main class.
        If status True, hide all secret thing;
        If status False, unhide all secret thing
        """

        if self.status:
            self.hide()
        else:
            self.unhide()

    def open_and_replace(self, file_path, old, new):
        """
        This method open file_path and replace old string with new string.

        :param file_path: Full path for open file
        :param old: Old string
        :param new: New string
        """
        try:
            with open(file_path, "r") as f:
                full_text = f.read()
        except IOError:
            print "File not read: " + file_path

        full_text = full_text.replace(old, new)

        try:
            with open(file_path, "w") as f:
                f.write(full_text)
        except IOError:
            print "File not write: " + file_path

    def wrapper(self, string):
        return "{{ " + string + " }}"

    def hide(self):
        """
        Hide all secret things
        """

        for config in self.config:
            print "# hide: " + config['file']
            self.open_and_replace(config['file'], config['secret'], self.wrapper(config['name']))


    def unhide(self):
        """
        Unhide all secret things
        """
        for config in self.config:
            print "# un-hide: " + config['file']
            self.open_and_replace(config['file'], self.wrapper(config['name']), config['secret'])
