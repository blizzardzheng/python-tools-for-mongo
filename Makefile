VIRTUALENV = $(shell which virtualenv)

clean: kill
	rm -fr venv

venv:
	$(VIRTUALENV) venv

install: venv
	. venv/bin/activate; pip install -r requirements.txt

mongo:
	ssh -fN -i ~/.ssh/id_rsa -L 27017:localhost:27017 coredev@dctars01.digitwalk.com

start: venv
	. venv/bin/activate; python survey.py

kill:
	ps -ef | grep "mongo" | grep -v grep | awk '{print $$2}' | xargs kill
