EXEC=./main.py
INSTALL_PYTHON_PACKAGE_MSG="By default python3 is used."
PYTHON_DEFAULT_EXEC=python3

all: run

scroller:
	$(PYTHON_DEFAULT_EXEC) python_version_scroller.py

dockeryaml:
	$(PYTHON_DEFAULT_EXEC) test_docker_from_yaml.py

run:
ifndef scenario
	$(MAKE) Convert
else ifeq ($(scenario), 1)
	$(MAKE) Convert
else ifeq ($(scenario), 2)
	$(MAKE) Exctract
else ifeq ($(scenario), 3)
	$(MAKE) ExtractNoExtension
else ifeq ($(scenario), 4)
	$(MAKE) AddExtension
else
	$(MAKE) Convert
endif

Convert:
	echo 'scenario 1'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -v true -f files/need-convert.txt -w "bonjour "

Exctract:
	echo 'scenario 2'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -v true -f files/need-convert.txt -d file/default-need-convert.txt -e "tst"

ExtractNoExtension:
	echo 'scenario 3'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -v true -f files/need-convert.txt -d file/default-need-convert.txt

AddExtension:
	echo 'scenario 4'
	$(PYTHON_DEFAULT_EXEC) $(EXEC) -v true -f files/need-convert.txt -e "finish"
