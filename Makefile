all: clean
	rm -rf build/ dist; python setup.py sdist

upload: all
	python setup.py upload

clean:
	rm -rf *.egg Wraptor.egg-info dist build
	find . -iname "*.pyc" -exec rm {} \;
	find . -iname "__pycache__" -exec rm -rf {} \;
	python setup.py clean --all

test:
	python setup.py test

.PHONY: flake8
flake8:
	flake8 --config=.flake8 .
