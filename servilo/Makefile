SHELL = /bin/bash

all:
	@echo "Ne defaŭlta komando"
	@echo "No default command"
freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt
install:
	if [[ $(lsb_release -r -s) = '17.04' ]]; then
		sudo apt install -y python3.6 python3-pip python3-dev virtualenv
	elif [[ $(lsb_release -r -s) = '14.04' ]]; then
		sudo apt install -y virtualenv
	fi
	if [ ! -d ".venv" ]; then virtualenv -p python3.6 .venv; fi
	. .venv/bin/activate; pip install -r requirements.txt
