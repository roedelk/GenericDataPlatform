import yaml

class Settings:

    @staticmethod
    def read(settingsFile):
        settingsFile = open(settingsFile, 'r')
        settings = yaml.load(settingsFile)
        return settings

    @staticmethod
    def write(settingsData, settingsFile='settings/GenericDataPlatform.cfg'):
        file = open(settingsFile, 'w')
        yaml.dump(settingsData, file)
        # safe_dump ?
        # logging
        return 1

if __name__ == '__main__':
    pass