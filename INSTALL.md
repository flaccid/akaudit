# akaudit Installation

## PIP

	# pip install akaudit

## From Source

	$ python setup.py sdist
    
The above command will install setup all the necessary files for installation in the `dist/` folder, then:

Linux/OS X:

    # pip install dist/akaudit*.tar.gz

As paramiko depends on ecdsa, you will need to install this if not already on your system:

    # pip install ecdsa

You will likely need to install gcc and Python development files too:

	# apt-get install gcc python-dev


If you are doing dev/test with your system you may like to:

	$ python setup.py sdist && sudo pip install dist/akaudit*.tar.gz --upgrade
