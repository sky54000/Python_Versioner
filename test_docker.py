import docker

def main():
    print("Hello world !!")
    client = docker.from_env()
    container = client.containers.run("python:2.7", "echo hello world", detach=True)
    print(container.logs())
    
if __name__ == '__main__':
    main()
