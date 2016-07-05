import os
from setuptools import setup

# Credit to Andrew Carter for some code obtained at https://pythonhosted.org/an_example_pypi_project/setuptools.html covered by BSD License

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read_version():
	folder_path = os.path.dirname(os.path.abspath(__file__))
	version_file_path = os.path.join(folder_path, 'VERSION')
	with open(version_file_path, 'r') as version_file:
		version = version_file.read().strip()
	return version
		
setup(
    name = "advanced_python_project",
    version = read_version(),
    author = "Aleksey Orekhov",
    author_email = "aleksey.orekhov@continuum.io",
    description = ("Simplest python project that can be built with conda."),
    license = "Creative Commons Attribution 4.0 International License.",
    keywords = "example documentation tutorial",
    url = "http://conda.pydata.org/",
    packages=['advanced_python_project'],
    long_description=read_file('README.md'),
	
	# classifiers are tags that will appear on pypi.python.org
	# go to https://pypi.python.org/pypi and hit 'browse' in the toolbar on the left hand side
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
