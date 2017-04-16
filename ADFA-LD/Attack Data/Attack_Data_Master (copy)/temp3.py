from myLib1729 import ngrams
import sys
inp = open(sys.argv[1],"r").read()

dic = {}

n = 5
threeGrams = ngrams(inp.split(),n)
for i in threeGrams:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1

#for r,t in dic.items():
#    print r,"-->",t

for key, value in sorted(dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    print "%s: %s" % (key, value)