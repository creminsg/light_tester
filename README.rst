===========
light_tester
============
------------------------------------------------
Once the package is installed, pasting the following into the command line should display to you the error I am getting: solve_led --input "data/input_assign4.txt". The error I am getting is: NameError: name 'ledSolve' is not defined. ledSolve is a module in the same directory as the cli.py file which is attempting to access it. It seems that the problem is that the cli.py file is failing to import ledSolve. To uninstall the package use "pip uninstall light-tester". Thank you for taking the time to look at my project.
------------------------------------------------



.. image:: https://img.shields.io/pypi/v/light_tester.svg
        :target: https://pypi.python.org/pypi/light_tester

.. image:: https://img.shields.io/travis/creminsg/light_tester.svg
        :target: https://travis-ci.org/creminsg/light_tester

.. image:: https://readthedocs.org/projects/light-tester/badge/?version=latest
        :target: https://light-tester.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Assignment 3 COMP30670


* Free software: MIT license
* Documentation: https://light-tester.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
