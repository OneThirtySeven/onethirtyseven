from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'OneThirtySeven'
LONG_DESCRIPTION = 'Data Scraping Wrappers'

# Setting up
setup(
        name="onethirtyseven", 
        version=VERSION,
        author="Matt Cleary",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        include_package_data=True,
        package_data={'': ['assets/*.csv']},
        install_requires=[]
)