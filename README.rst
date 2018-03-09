===========
light_tester
============
------------------------------------------------------
This program is intended to test the proper functioning of LED display boards. You can feed it instructions telling it which lights of a display board to turn on or off and it will output the number of lights that should be turned on at the end of the instructions. 

To input an instruction file use solve_led --input <"local file or web address">. For example: solve_led --input "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt".

Note: The test modules were used to test the functionality of parts of the code. When all of these parts are put together to make the working program, the tests fail. 
------------------------------------------------------


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

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
