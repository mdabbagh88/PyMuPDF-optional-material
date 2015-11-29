Script python++.cmd
===================

This script addresses the issue of ``Error: Unable to find vcvarsall.bat``.

It works under the assumption that ``Microsoft Visual C++ for Python`` has been installed in the standard way, i.e. is located in directory ``C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python``.

What it does
------------

The script switches (PUSHD command) to the VC++ directory and excutes ``vcvarsall.bat`` and some other commands. It then restores the original script directory (POPD command) and executes the Python interpreter with the parameters supplied to the script.

How to invoke
-------------

In order to perform a PyMuPDF setup execute the following in the command prompt of your PyFitz directory:

``python++ setup.py install``
