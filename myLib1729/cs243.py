import os,sys

def ngrams(seq,n):
    ans = []
    for i in range(len(seq)-n+1):
        ans.append(tuple(seq[i:i+n]))
    return ans

def ngramsDictionary(seq,n):
    ans = {}
    for i in range(len(seq)-n+1):
        tup = tuple(seq[i:i+n])
        if(tup not in ans):
            ans[tup]=1
        else:
            ans[tup]+=1
    return ans

def countSort(dictionary,maxentry):
    count = [[] for _ in range(maxentry+1)]
    arr = list(dictionary.values())
    keys1 = list(dictionary.keys())
    for i in range(len(arr)):
        count[arr[i]].append(keys1[i])
    ansArr = []
    for i in range(1,len(count)+1):
        for j in count[-i]:
            ansArr.append((j,maxentry - i + 1))
    return ansArr