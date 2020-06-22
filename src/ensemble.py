import os
import pandas
def file_split(inputfile,outputfile,single_len):
    a = open(inputfile,"r")
    ss = a.read()
    sslist = ss.split('\n')
    singlen = single_len
    all = []
    for i in range(0,len(sslist),singlen):
        all.append("\n".join(sslist[i:i+singlen]))
    for i in range(len(all)):
        b = open(outputfile+"%04d"%(i,),'w')
        b.write(all[i])
        b.close()

# def 
def val_from(inputfile):
    return pandas.read_csv(inputfile,sep = '\t')
if (__name__=="__main__"):
    file_split("alleval","alleval",3)
    file_split('allans','anssplit',1064)
    listF = [
        "anssplit0006",
        "anssplit0007",
        "anssplit0009",
        "anssplit0017",
        "anssplit0018",
        "anssplit0019",
        "anssplit0021",
        "anssplit0022",
        "anssplit0024",
        "anssplit0026",
        "anssplit0027",
        "anssplit0028",
        "anssplit0031",
    ]
    allf = None
    for infile in listF:
        if (allf is None):
            allf = val_from(infile)
        else:
            allf += val_from(infile)
    allf = (allf + len(listF)//2)//len(listF)
    allf.to_csv('ens.csv',index = False,sep = '\t')