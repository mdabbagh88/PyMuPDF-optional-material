Updating End-Of-Line Characters in Windows
===========================================

The utility upd_eol.py addresses an issue Windows users may encounter when installing PyMuPDF:

MuPDF source comes with the UNIX specific end-of-line character 'LF' (0x0A).
The VC++ compile step of the command ``python setup.py install`` may end with error messages (like includes not being found, etc.) when being supplied with such sources.

This utility locates the MuPDF include directory and changes all eol characters to the Windows standard CRLF for all header files (*.h) it finds in

* ``./include/mupdf``
* ``./include/mupdf/fitz``
* ``./include/mupdf/pdf``

Possible invocations:
=====================

``python upd_eol.py <mupdf source dir>``
----------------------------------------

In this case, the MuPDF source directory must be specified. The utility will check whether ``./include/mupdf`` exists, and will stop it not.

``python upd_eol.py``
---------------------

When invoked without parameters, the utility assumes it is located one directory level above MuPDF source and will search for the first directory starting with "mupdf".

If no such directory is found or if it has no subdirectory ``./include/mupdf`` processing will stop.
