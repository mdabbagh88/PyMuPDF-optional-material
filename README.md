# PyMuPDF Optional Material
This repository contains some Windows-specific optional material for [PyMuPDF](https://github.com/rk700/PyMuPDF), the Python bindings for accessing PDF files with MuPDF.

Its purpose is to slim down the PyMuPDF repository to only contain material vital to create PyMuPDF in your Python installation.

However, this repository does embody stuff of interest, that may simplify your setup effort and / or provide additional information:

* **Pre-generated Windows *.lib modules:** Before you can use MuPDF in PyMuPDF, you must generate object code which is then being linkedited to your Python PYD (DLL) file. This requires that you have Visual Studio installed on your system (a several gigabyte beast). If you cannot or do not want to meet this prerequisite, then the modules in directory ``LibWin32`` are for you. They contain the required libraries, so you only need to execute the ``setup.py install`` command of PyMuPDF and do **not need to generate MuPDF**. You still must have a working C++ compiler for Python on board of course (usually ``MS Visual C++ for Python`` to be downloaded e.g. from [here](http://www.microsoft.com/en-us/download/details.aspx?id=44266)).

* **MuPDF include directory:** This directory, together with the ``*.lib`` modules from above, can be used to setup PyMuPDF. No download of MuPDF is required.

* **CHM based help:** PyMuPDF comes with HTML based help files. If you wish to use a compiled HTML (CHM) Windows help, you will find it here.

* **minor utilities:** Included here are: (1) a setup command utility for avoiding the pesky problem ``Unable to locate vcvarsall.bat``, and (2) a tool to ensure that the header files in MuPDF source have the Windows standard end-of-line characters CRLF.


# License
All material in this repository is licensed under the same licence as PyMuPDF, i.e. the GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007 or later, as defined in the ``COPYING`` file.
