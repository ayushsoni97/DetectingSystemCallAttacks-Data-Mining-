import os,sys

out = open("totTrainDataValidation.txt","a+")

for f in os.listdir("./"):
    if f.startswith("UVD"):
        fileRead = open(f,"r")
        inp = fileRead.read()
        out.write(inp)
        out.write("-1 ")
        sys.stdout.write("Concatenating all normal test data files ...\n")