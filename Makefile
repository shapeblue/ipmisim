all:
	python setup.py sdist

clean:
	rm -fr dist ipmisim.egg-info ipmisim/*pyc
