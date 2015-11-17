# PyMuPDF Optional Material
This repository contains optional material for PyMuPDF, the Python bindings for accessing PDF files with MuPDF.

Its purpose is to slim down the [PyMuPDF](https://github.com/rk700/PyMuPDF) repository to only contain material vital to create PyMuPDF in your Python installation.

However, this repository embodies stuff of interest, simplifying your setup effort and / or providing additional information:

* **Pre-generated Windows *.lib modules:** before you can use MuPDF in PyMuPDF, you must generate object code which is being linkedited to your Python PYD (DLL) file. This requires that you have Visual Studio installed on your system. If you cannot or do not want to meet this prerequisite, then the modules in directory Winlib32 provided here are there for you. They contain the required libraries, so you only need to execute the ``setup.py install`` command of PyMuPDF. This only requires that you have a working C++ compiler for Python on board (usually MS Visual C++ for Python).

* **CHM based help:** [PyMuPDF](https://github.com/rk700/PyMuPDF) comes with HTML based help files. If you wish to use a compiled HTML (CHM) Windows help, you will find it here.

# License
All material in this repository is licensed under the same licence as PyMuPDF, i.e. GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 as defined in the ``COPYING`` file.