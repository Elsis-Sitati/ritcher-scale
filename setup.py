# making the installer for this python pacakage

try:
	# setuptools allows you to specify all the various attributes for this package
	# all systems may not have set up tools installed thats why we try 
	from setuptools import setup
except ImportError:
	# all versions of python come with distutils so it will fall back to distutils incase setuptools is not found
	from distutils.core import setup

# do not specify the version so that the latest is installed on install
dependencies = ['docopt', 'termcolor']

setup(
	# name for the application
	name="ritcher",
	version="0.0.1",
	description="outputing ritcher-scale graph",
	url="https://github.com/Elsis-Sitati/ritcher-scale",
	author="Elsis Sitati",
	author_email="sitatielsis@gmail.com",
	# specifying which applications your app depends on
	install_requires=dependencies,
	packages=["ritcher",],
	# this is what actually runs when you call ritcher from the command line
	# the entry point says which function is called when you type in ritcher
	entry_points={
	'console_scripts': [
		# ritcher is the name of the command
		# from ritcher package access the main module and execute the start method
		'ritcher=ritcher.main:start'
	 		
	 		],
		},
	)