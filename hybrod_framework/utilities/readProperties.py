import configparser

config = configparser.RawConfigParser()
# config.read('.\\Configurations\\config.ini')
config.read(r"C:\Users\davud\PycharmProjects\hybrod_framework\Configurations\config.ini")

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url


    @staticmethod
    def getApplicationUserEmail():
        userName = config.get('common info', 'useremail')
        return userName


    @staticmethod
    def getApplicationPassword():
        password = config.get('common info', 'password')
        return password
