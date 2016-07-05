import logging
import os

import pkg_resources  # part of setuptools

try:
	__version__ = pkg_resources.require(__name__)[0].version
except pkg_resources.DistributionNotFound:
	# obtain version number while developing package when setup.py has not been run
	logger = logging.getLogger(__name__)
	logger.debug("Version number obtained in development mode")
	
	folder_path = os.path.dirname(os.path.abspath(__file__))
	version_file_path = os.path.join(folder_path, '..', 'VERSION')
	with open(version_file_path, 'r') as version_file:
		__version__ = version_file.read().strip()
