import configparser
import sys
from os.path import isfile

#  TODO create fun load_single_ini, load_multiple_ini and load_single

class Config:

    def __init__(self, ini_file):
        if not isfile(ini_file):
            print(f"Config file: {ini_file} did not exist")
            sys.exit(2)

        self.__config = configparser.ConfigParser()
        self.__config.read(ini_file)
        self.bots_list = self.__get_bots()

    def __get_bots(self) -> list:
        bots = []
        for bot in self.__config:
            token_list = []
            if bot != "DEFAULT":
                for token in self.__config[bot]:
                    token_list.append(self.__config[bot][token])
                if len(token_list) > 0:
                    bots.append((bot, token_list))
        if len(bots) > 0:
            return bots
        else:
            return None


if __name__ == '__main__':
    config = Config("../../test.ini")