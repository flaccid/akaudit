$ python setup.py sdist
    
The above commands will install setup all the necessary files for installation in the `dist/` folder.

Linux/OS X:

    # pip install dist/akaudit*.tar.gz

As paramiko depends on ecdsa, you will need to install this if not already on your system:

    # pip install ecdsa

You will likely need to install gcc and Python development files too:

	# apt-get install gcc python-dev
