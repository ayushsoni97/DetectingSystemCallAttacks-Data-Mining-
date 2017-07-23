from myLib1729 import *
from time import sleep
print "\n\nReading Input File ...\n"

fNormalUser = open("totTrainData.txt","r")

print "What Weight do u want to use for ngrams division?\n"
n = int(raw_input())

print "\n\nCreating ngrams dictionaries for all files. Please Wait ...\n"
normalDict = ngramsDictionary(fNormalUser.read().split(),n)
print "Normal Dictionary Created!\n"

print "\nCreating Text Files for Dictionary Output ...\n"
top30Normal = []
out = open("normalDict.txt", "a+")
Ltot = len(normalDict)
c=0
sentinel = 4500
#sentinel = 150
#top30 = top30Data[i]
top30 = []
print "\nCreating top 30% arrays of tuples for Normal Data . . .\n"
sleep(1)
for key, value in sorted(normalDict.iteritems(), key=lambda (k,v): (v,k), reverse=True):
    c+=1
    out.write("%s: %s\n" % (key, value))
    if(sentinel >= c):
        top30.append(key)

finalFile = open("DATASET_1.arff","a+")
configString = "@relation KDDTest-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.Resample-B0.0-S1-Z18.0-weka.filters.unsupervised.instance.Randomize-S42-weka.filters.supervised.instance.SMOTE-C2-K5-P1000.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C2-K5-P125.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P500.0-S1-weka.filters.supervised.instance.SMOTE-C3-K5-P150.0-S1-weka.filters.supervised.instance.SMOTE-C4-K5-P800.0-S1-weka.filters.unsupervised.instance.Randomize-S42\n@attribute duration numeric\n@attribute src_bytes numeric\n@attribute dst_bytes numeric\n@attribute wrong_fragment numeric\n@attribute urgent numeric\n@attribute hot numeric\n@attribute num_failed_logins numeric\n@attribute num_compromised numeric\n@attribute root_shell numeric\n@attribute class {Normal}\n\n@data\n"
finalFile.write(configString)
print "--------------------------------------------------------\nCreating DATASHEET . . ."
sleep(3)
print "###################################################################################"
for i in range(0,sentinel,9):
    f1 = top30[i]
    f2 = top30[i+1]
    f3 = top30[i+2]
    f4 = top30[i+3]
    f5 = top30[i+4]
    f6 = top30[i+5]
    f7 = top30[i+6]
    f8 = top30[i+7]
    f9 = top30[i+8]
    features = [f1,f2,f3,f4,f5,f6,f7,f8,f9]
    dataSet = ""
    for j in range(9):
        try:
            dataSet+=str(addUserDict[features[j]])+", "
        except:
            dataSet += str(0) + ", "
    dataSet+="Normal\n"
    finalFile.write(dataSet)
print "Training Model Created !!!"
print "################################################################################"
