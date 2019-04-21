EXEC=pip
EXEC_DEFAULT_TEST=pytest
PYTHON_DEFAULT_EXEC=python3

all: t


run:
ifndef scenario
	$(MAKE) -C examples run_scenario_1
else ifeq ($(scenario), 2)
	$(MAKE) -C examples run_scenario_2
else ifeq ($(scenario), 3)
	$(MAKE) -C examples run_scenario_3
else ifeq ($(scenario), 4)
	$(MAKE) -C examples run_scenario_4
else ifeq ($(scenario), 5)
	$(MAKE) -C examples run_scenario_5
else
	$(MAKE) -C examples run_scenario_defaults
endif

test:
ifndef exec_test
	$(PYTHON_DEFAULT_EXEC) -m $(EXEC_DEFAULT_TEST) -q test -s
else
	$(PYTHON_DEFAULT_EXEC) -m $(exec_test) -q test -s
endif

install:
	$(PYTHON_DEFAULT_EXEC) -m $(EXEC) install .
	echo "pversioner installed"

uninstall:
	$(PYTHON_DEFAULT_EXEC) -m $(EXEC) uninstall pversioner
	echo "pversioner uninstall"
