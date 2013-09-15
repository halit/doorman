from ConfigParser import ConfigParser


class Config:
    def __init__(self, config_file):
        self.config_file = config_file

    def parse(self):
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
    def __init__(self, status, config_file):
        self.status = status
        self.config = Config(config_file).parse()

    def run(self):
        if self.status:
            self.hide()
        else:
            self.unhide()

    def open_and_replace(self, file_path, old, new):
        with open(file_path, "w") as f:
            full_text = f.read()
            full_text = full_text.replace(old, new)
            f.write(full_text)

    def hide(self):
        for key, value in self.config.items():
            secret_thing, secret_file = value.items()
            self.open_and_replace(secret_file[1], secret_thing[1], secret_thing[1])


    def unhide(self):
        pass
