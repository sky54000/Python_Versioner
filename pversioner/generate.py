import requests
from bs4 import BeautifulSoup
import yaml

from pversioner import DEFAULT_PYTHON_LIST_URL

class Generate:

    def __init__(self, filename):
        self._html_id_pars = "python-documentation-by-version"
        self.__filename = filename
        self.__get_page()
        self.__parse()
        
    def __get_page(self):
        try:
            self.__page = requests.get(DEFAULT_PYTHON_LIST_URL)
        except Exception as err:
            raise Exception(err)

    def __parse(self):
        soup = BeautifulSoup(self.__page.text, 'html.parser')
        list = soup.find(id=self._html_id_pars).find('ul')
        list_version = []
        for item in list.find_all('a'):
            list_version.append(item.text.split(" ")[-1])

        self.__versions_available = list_version

    def __export(self):
        try:
            data = dict({'versions': self.__versions_available })
            with open(self.__filename, 'w+') as outfile:
                yaml.dump(data, outfile, default_flow_style=False)
        except Exception as err:
            raise Exception(err)

    def action(self):
        self.__export()
