'''
Created on Nov 20, 2017

@author: Saimir Bala <saimir.bala@gmail.com>
'''
from datetime import datetime
import json
import os
import glob

from at.ac.wu.eventmesh.json_to_csv import convertAndAnynomizePayload, convert

if __name__ == '__main__':
    pass

def transform(infileJSON, outfileCSV):
    # Reading data back
    with open(infileJSON, 'r') as f:
        data = json.load(f)    
  
#     for k in keys:
#         #print k, type(k), len(k)
#         if type(k)=='dict':
#             print k.keys() 
    hits = data['hits']['hits']    
    # senstive data only on payload
    # convertAndAnynomizePayload('hits',hits,outfileCSV)
    convert('hits',hits,outfileCSV)
    

startTime = datetime.now()

homedir = os.getcwd()
cwd = '/home/saimir/ownCloud/PhD/PHACTUM/magma/data20171130/'
os.chdir(cwd)
files = glob.glob("*.json")

outfileName = "allEvents.csv"

try:
    os.remove(outfileName)
except OSError:
    pass

outfile=open(homedir+"/"+outfileName, "a")

i=0
for f in files:
    i+=1
    print ("Done: %.2f" % (i*100/len(files)))
    outCSV = f.replace(".json", ".csv")
    transform(f, outCSV)
    if(f==files[0]):
        outfile.writelines(open(outCSV, "r").readlines())
    else:
        outfile.writelines(open(outCSV, "r").readlines()[1:])
outfile.close()

print "Done ",(datetime.now()-startTime), ". Output saved in ", outfileName

