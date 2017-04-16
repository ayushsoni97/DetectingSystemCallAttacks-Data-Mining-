from nltk import ngrams
import sys
inp = open(sys.argv[1],"r").read()

dic = {}

n = 3
threeGrams = ngrams(inp.split(),n)
for i in threeGrams:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1

#for r,t in dic.items():
#    print r,"-->",t
#Ltot = len(dic)
#c=0
for key, value in sorted(dic.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    #c+=1
    #print key, value
    print "%s: %s" % (key, value)
    #if(Ltot*0.3 <= c):
     #   break