class ConfigState(object):
    __config: dict
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    @property
    def config(self) -> dict:
        return self.__config

    @config.setter
    def config(self, config: dict):
        self.__config = config
