# Python Versioner

## Summary

- [Description](#description)
- [Install](#install)
- [Use it](#user-it)
- [Tests](#test)
- [Documentation](#documentation)

## Description  
Tool to test your code in different python versions  
Python versioner use docker, it run multiple containers with python versions selected,  
then `pversioner` shared your code in a volume between each containers to evaluate your code status.

## Install

Install the package:
```shell
make install
```

Uninstall the package:
```shell
make uninstall
```

**manually :**

Install package:
```shell
pip install .
```

Uninstall package:
```shell
pip uninstall pversioner
```

## Use it


## Tests

run test:
```
make test
```

## Documentation

_Makefile commands available_:

|           **Commands name**           | **Description**                         |
|:-------------------------------------:|:--------------------------------------- |
|            `make install`             | install `pversioner`                    |
|                                       |                                         |
|           `make uninstall`            | uninstall `pversioner`                  |
|                                       |                                         |
|              `make test`              | run test                                |
|                                       |                                         |
|              `make run`               | run example                             |
| `make run scenarios=[1 , 2, 3, 4, 5]` | run example with a specifique scenarios |
|                                       |                                         |

you can specify makefile options:

|    **Define name**    | **Default** | **Description**                             |
|:---------------------:|:----------- | ------------------------------------------- |
|  `EXEC_DEFAULT_TEST`  | pytest      | Tools to run tests                          |
|                       |             |                                             |
| `PYTHON_DEFAULT_EXEC` | python3     | Use Python to run tests and install package |
|                       |             |                                             |

**releases version:**

| **releases version** | ** releases short** | **Description**                                         |
|:--------------------:|:------------------- | ------------------------------------------------------- |
|  `pversioner-0.0.1`  | 0.0.1               | [Base] basic usage of `pversioner` ('execution report') |
|                      |                     |                                                         |

__Reference__:

- [Python3.5 Documentation](https://www.python.org/downloads/release/python-350/)
- [pip](https://pip.pypa.io/en/stable/)
- [setuptools](https://setuptools.readthedocs.io/en/latest/)
