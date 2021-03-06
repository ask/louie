.. Louie documentation master file, created by
   sphinx-quickstart on Sat Sep 12 10:51:46 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Louie's documentation!
=================================

Contents:

.. toctree::
   :maxdepth: 2

   about
   changes
   contributors

Louie provides Python programmers with a straightforward way to
dispatch signals between objects in a wide variety of contexts. It is
based on PyDispatcher_, which in turn was based on a highly-rated
recipe_ in the Python Cookbook.

Louie is licensed under `The BSD License`_.

.. _PyDispatcher: http://pydispatcher.sf.net/

.. _recipe: http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/87056

.. _The BSD License: http://opensource.org/licenses/bsd-license.php


Louie Requirements
==================

- Python 2.3 or higher.


Installing Louie
================

Louie uses `easy_install`_ for installation, and is distributed via
the `Python Cheese Shop`_.

.. _easy_install: http://peak.telecommunity.com/DevCenter/EasyInstall

.. _Python Cheese Shop: http://cheeseshop.python.org/pypi/Louie

If you already have `easy_install`, run this command::

  easy_install Louie

If that failed, you do not have `easy_install`.  To install that,
download `ez_setup.py`_, then run this command::

  python ez_setup.py setuptools

.. _ez_setup.py: http://peak.telecommunity.com/dist/ez_setup.py

Then, run the `easy_install` command given above again.


Upgrading Louie
===============

Run this command to upgrade Louie to the latest release::

  easy_install -U Louie


Development
===========

You can track the latest changes in Louie using the Subversion
repository or using regularly-built snapshots.


Using easy_install
------------------

Provided you already have `easy_install`, run this command::

  easy_install -f http://louie.berlios.de/dist/ Louie


Using Subversion
----------------

Check out the Louie trunk as per the `Berlios usage information
<http://developer.berlios.de/svn/?group_id=5432>`__.

Run this command inside your checkout path::

  python setup.py install

Alternatively, you may use Louie directly from your checkout path
using this command::

  python setup.py develop


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
