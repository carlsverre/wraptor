.PHONY: all
all: clean
	rm -rf build/ dist; python setup.py sdist

.PHONY: upload
upload: all venv
	. venv/bin/activate && twine upload dist/*

.PHONY: clean
clean:
	rm -rf *.egg Wraptor.egg-info dist build
	find . -type f -name "*.pyc" -exec rm {} \;
	for _kill_path in $$(find . -name "__pycache__"); do rm -rf $$_kill_path; done
	python setup.py clean --all

.PHONY: test
test: venv
	. venv/bin/activate && pytest

.PHONY: flake8
flake8:
	. venv/bin/activate && flake8 --config=.flake8 .

venv: dev_requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate && pip install -r dev_requirements.txt
