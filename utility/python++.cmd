@echo off
PUSHD "C:\Program Files (x86)\Common Files\Microsoft\Visual C++ for Python"
call vcvarsall.bat x86
SET DISTUTILS_USE_SDK=1
SET MSSdk=1
POPD
python %*
