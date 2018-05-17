default:
	echo "Nothing to do"

test:
	nosetests --nocapture --with-coverage --cover-package=terminal
	coverage report -m --skip-covered