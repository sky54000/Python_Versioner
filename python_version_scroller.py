import requests
import yaml
from bs4 import BeautifulSoup

def main():
    page = requests.get("https://www.python.org/doc/versions/")
    soup = BeautifulSoup(page.text, 'html.parser')

    list = soup.find(id="python-documentation-by-version").find('ul')
    list_version = []
    for item in list.find_all('a'):
        list_version.append(item.text.split(" ")[-1])
    data = dict({'version': list_version})
    with open('data.yml', 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

if __name__ == '__main__':
    main()
