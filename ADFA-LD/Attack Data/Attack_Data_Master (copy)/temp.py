from nltk import ngrams

import os
import sys

flist = open("metr.txt","r")
out = open("totTestMetr.txt","a+")
a = flist.read().splitlines()
sent = "./Meterpreter_"
for f in a:
    if f.startswith(sent+"8") or f.startswith(sent + "9") or f.startswith(sent + "10"):
        fileo = open(f,"r")
        r = fileo.read()
        out.write(r)
        print f
    
