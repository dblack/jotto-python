clean:
	find . -name "*.pyc" -delete
	rm -rf test/__pycache__
	rm -rf jotto/__pycache__
