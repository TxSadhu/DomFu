from setuptools import setup, find_packages

setup(
    name='DomFu',
    version='1.0',
    author='Suman Basuli',
    author_email='thinisadhu@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://pypi.python.org/pypi/domfu/',
    license='LICENSE.txt',
    description='A CLI app to find domains and subdomains of a given domain',
    long_description=open('README.md').read(),
    install_requires=[
        "fire",
        "yaspin",
        "requests",
        "validators",
    ],
    entry_points='''
        [console_scripts]
        domfu=DomFu.__main__:main
    ''',
)