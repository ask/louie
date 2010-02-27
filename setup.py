import os
import codecs
import textwrap
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

try:
    import buildutils
except ImportError:
    pass

import louie

if os.path.exists("README.rst"):
    long_description = codecs.open("README.rst", "r", "utf-8").read()
else:
    long_description = "See http://pypi.python.org/pypi/Louie"

setup(
    name="Louie",

    version=louie.__version__,

    description=louie.__doc__,

    long_description=textwrap.dedent(long_description),

    classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='',
    author=louie.__author__,
    author_email=louie.__contact__,
    url=louie.__homepage__,
    license='BSD',
    packages=find_packages(exclude=['doc', 'ez_setup', 'examples', 'tests']),
    install_requires=[
    'nose >= 0.10.1',
    ],
    zip_safe=False,
    package_data={
    # -*- package_data: -*-
    },
    test_suite = 'nose.collector',
)
