import os
import argparse
import yaml

from pkg_resources import Requirement, resource_filename
from argparseGraph.argparseGraph import argparseGraph as agG

class Parameters:

    def __init__(self):
        self.__parsarg()
        self.__state = 0
        self.__check_parameters()

    def __parsarg(self):
        parser = argparse.ArgumentParser(description="Test your code on multiple python versions")
        parser.add_argument("-g", "--generate",dest="generate", help="Create a default configuration file.", action="store_true")
        parser.add_argument("-f", "--configuration-file", dest="conf_file", help="Specify the configuration file name.", type=str)
        parser.add_argument("-w", "--worker", dest="worker", help="Number of containers run simultaneously.", type=int, default=4)
        parser.add_argument("-r", "--run", dest="run", help="Run to generate report.", action="store_true")
        parser.add_argument("-v", "--volume", dest="volume", help="Specify the volume path.", type=str)
        parser.add_argument("-c", "--commande-line", dest="cmdline", help="Commands line to test.(default='python -u -B main.py')", type=str, default="python -u -B main.py")
        parser.add_argument("-e", "--export", dest="report", help="Report file name.", type=str)
        args = parser.parse_args()

        print(args)
        self._raw_parameters = args

    def __checkdir(self, dir):
        if dir:
            if os.path.isdir(dir):
                return dir
        return None

    def __check_parameters(self):

        if self._raw_parameters.generate:
            self.__state = dict({
                "action": 0,
                "data": self._raw_parameters.conf_file if self._raw_parameters.conf_file != None else "pversioner-configuration.yml"
            })
        if self._raw_parameters.run:
            self.__state = dict({
                "action": 1,
                "data": {
                    "conf_file": self._raw_parameters.conf_file if self._raw_parameters.conf_file != None else "pversioner-configuration.yml",
                    "volume": self.__checkdir(self._raw_parameters.volume),
                    "cmdline": self._raw_parameters.cmdline,
                    "worker": self._raw_parameters.worker,
                    "report": self._raw_parameters.report
                    }
                })
        pass

    def get_state(self):
        return self.__state
