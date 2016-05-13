import pip

__author__ = 'mhintz'

packages = [
    "flask==0.10.1",
    "flask_sqlalchemy==2.1",
]


def install(package):
    for i in package:
        print ("\n" + i + " :")
        pip.main(['install', i])

# Install necessary libraries
install(packages)

