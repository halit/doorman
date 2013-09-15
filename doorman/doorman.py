from ConfigParser import ConfigParser


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

    def parse(self):
        """
        Parser method for Config class
        It parse config file to dict
        """

        config = ConfigParser()
        config.read([self.config_file])

        configs = dict()
        config_secrets = dict()

        for key, value in config.items('secrets'):
            config_secrets[key] = value

        for key, value in config.items('files'):
            configs[key] = dict(secret_thing=config_secrets[key],
                                secret_file=value)

        return configs


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

        with open(file_path, "w") as f:
            full_text = f.read()
            full_text = full_text.replace(old, new)
            f.write(full_text)

    def hide(self):
        """
        Hide all secret things

        secret_thing[1]:
        secret_file[1]:
        """

        for key, value in self.config.items():
            secret_thing, secret_file = value.items()
            print secret_file
            #self.open_and_replace(secret_file[1], secret_thing[1], secret_thing[1])


    def unhide(self):
        """
        Unhide all secret things
        """

        pass
