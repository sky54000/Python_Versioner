import yaml
import docker


def main():
    with open("data.yml", 'r') as fd:
        conf = yaml.load(fd)

    client = docker.from_env()
    containers_list = []
    for e in conf["version"]:
        print("run python:{}".format(e))
        container = client.containers.run("python:{}".format(e), "pip install argparse-graph", detach=True) # work
        containers_list.append(container)
        print(container.logs())

if __name__ == '__main__':
    main()

class Template_python_package:

    def __init__(self):
        pass
