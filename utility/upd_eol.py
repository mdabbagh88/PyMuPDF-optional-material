'''
This utility adapts end-of-line characters to the standard of the operating
system - specifically, it will replace the UNIX standard 'LF' with the Windows
standard 'CRLF'.
This process will occur for all header (*.h) files in the include directory
of the MuPDF source and its 'fitz' / 'pdf' subdirectories.
The user must either specify the top level directory of MuPDF source in the
command line, or this script must be started in a directory one level higher
than the source.
'''
import os, sys
def change_eol(verz):
    flist = os.listdir(verz)
    print "=====>", len(flist), "elements in", verz
    for datei in flist:
        if datei.endswith(".h"):
            xfle = os.path.join(verz, datei)
            print "processing", xfle
            fle = open(xfle)
            text = fle.read()
            fle.close()
            fle = open(xfle, "w")
            fle.write(text)
            fle.close()

verz = ""
if len(sys.argv) > 1:
    verz = sys.argv[1]
    verz_inc = os.path.join(verz, "include", "mupdf")
    verz = verz_inc
    if not os.path.exists(verz):
        print verz, "does not exist - exiting"
        raise SystemExit

if not verz:
    print "no dir parameter found, checking current dir"
    verz = os.listdir(os.curdir)
    for mu_dir in verz:
        if mu_dir.lower().startswith("mupdf"):
            break
        else:
            mud_dir = ""
    if mu_dir:
        verz = os.path.join(os.curdir, mu_dir, "include", "mupdf")
        if not os.path.exists(verz):
            print "cannot find MuPDF include dir - exiting"
            raise SystemExit
    else:
        print "cannot find MuPDF include dir - exiting"
        raise SystemExit

verz_fitz = os.path.join(verz, "fitz")
verz_pdf  = os.path.join(verz, "pdf")
if not os.path.exists(verz_fitz):
    print "direcotry", verz_fitz, "does not exist - exiting"
    raise SystemExit
if not os.path.exists(verz_pdf):
    print "direcotry", verz_pdf, "does not exist - exiting"
    raise SystemExit

print "found all required directories - start processing?"
antw = raw_input("y/n: ")
print "answer", antw
if antw == "y":
    change_eol(verz)
    change_eol(verz_fitz)
    change_eol(verz_pdf)
