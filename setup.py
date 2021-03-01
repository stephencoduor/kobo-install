from distutils.core import setup
from setuptools import find_packages
from helpers.config import Config

setup(
    name='kobo-install',
    version=Config.KOBO_INSTALL_VERSION,
    # Include all the python modules except `tests`,
    packages=find_packages(exclude=['tests']),
    #url='https://github.com/kobotoolbox/kobo-install/',
    url='https://github.com/stephencoduor/kobo-install/',
    license='',
    author='stephencoduor',
    author_email='stephencoduor@gmail.com',
    description='Installer for KoBoToolbox'
)
