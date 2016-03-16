clean:
	find . -name "*.pyc" -delete
	rm -rf test/__pycache__
	rm -rf jotto/__pycache__
test: clean
	python -m unittest discover
