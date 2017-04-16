import os,sys

out = open("totTrainData.txt","a+")

for f in os.listdir("./"):
    if f.startswith("UTD"):
        fileRead = open(f,"r")
        inp = fileRead.read()
        out.write(inp)
        out.write("-1 ")
        sys.stdout.write("Concatenating all normal data files ...\n")