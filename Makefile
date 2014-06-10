init:
	pip install -r requirements.txt --use-mirrors

test:
	nosetests tests

coverage:
	nosetests --with-coverage --cover-erase --cover-html --cover-package=doorman tests

