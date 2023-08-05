Unprompt
========

|Version| |License|

    Simply ask the user

*Unprompt* is the user inquiry prompt.
It provides a simple and elegant way of asking the user for input in interactive scripts and programs.

-  **Source:** https://github.com/tylerh111/unprompt
-  **Documentation:** https://unprompt.readthedocs.io

Installation
------------

*Unprompt* can be installed by running :bash:`pip install unprompt`.
To get the latest development version, use: :bash:`pip install git+https://github.com/tylerh111/unprompt`.

Usage
-----

*Unprompt* can be used as command or in your python code.
To ask the user for input on the command line, run the following command:

.. code-block:: bash

    unprompt "How are you?"  # How are you? Great!

To ask the user for input on the command line, simply import the package and call the :python:`ask` function.

.. code-block:: python

    import unprompt

    answer = unprompt.ask("How are you?")  # How are you? Great!

Contents
--------

.. toctree::
   :maxdepth: 2

   Home <self>
   api
   releases

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`


.. |Version| image:: https://img.shields.io/badge/version-0.0-blue
   :target: https://github.com/tylerh111/unprompt
.. |License| image:: https://img.shields.io/badge/license-MIT-blueviolet
   :target: https://github.com/tylerh111/unprompt/blob/main/LICENSE.md
