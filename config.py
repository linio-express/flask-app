import os
from configparser import ConfigParser


class Config:
    """Interact with configuration variables."""

    configParser = ConfigParser()
    configFilePath = (os.path.join(os.getcwd(), 'config.ini'))

    @classmethod
    def initialize(cls):
        """Start config by reading config.ini."""
        print("Caso")
        cls.configParser.read(cls.configFilePath)

    @classmethod
    def get(cls, key):
        """Get prod values from config.ini."""
        return cls.configParser.get('GENERAL', key)
