# PyMuPDF Optional Material
This repository contains optional material for PyMuPDF, the Python bindings for accessing PDF files with MuPDF.

Its purpose is to slim down the rk700/PyMuPDF repository to only contain material vital to create PyMuPDF in your Python installation.

However, this repository embodies stuff of interest, simplifying your setup effort and / or providing additional information:

* Pre-generated Windows *.lib modules: before you can use MuPDF in PyMuPDF, you must generate object code which is being linkedited to your Python PYD (DLL) file. This requires that you have Visual Studio installed on your system. If you cannot or do not want to meet this prerequisite, then the modules in directory Winlib32 provided here are there for you. They contain the required libraries, so you only need to execute the "setup.py install" command of PyMuPDF.

* rk700/PyMuPDF comes with HTML based help files. If you wish to use to use the compiled HTML version for Windows or a PDF version, you will find the respective files here.
