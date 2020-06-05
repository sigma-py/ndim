default:
	@echo "\"make format\"?"

format:
	isort -rc .
	black .

black:
	black .

lint:
	black --check .
	flake8 .
