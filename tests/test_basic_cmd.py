import pytest
import pytest_virtualenv as venv

from distutils.dir_util import copy_tree

@pytest.fixture(scope="session")
def init_env():
    v = venv.VirtualEnv()
    copy_tree("{}/".format(v.env["PWD"]), v.workspace)
    v.run("pip install .")
    return v

def test_start(init_env):
    init_env.run("My_Python_script --help")
