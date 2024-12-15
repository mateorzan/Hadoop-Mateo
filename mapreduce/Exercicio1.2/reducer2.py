#!/usr/bin/python
import sys

salesTotal = 0
oldKey = None

for line in sys.stdin:
        
   data_mapped = line.strip().split("\t")
   if len(data_mapped) != 2:
      continue
        
   try:
     thisKey, thisSale = data_mapped
     thisSale = float(thisSale)

            
     if oldKey and oldKey != thisKey:
               
        print("{0}\t{1}".format(oldKey, salesTotal))
        salesTotal = 0
            
     oldKey = thisKey
     salesTotal += thisSale
    
   except:
     continue
if oldKey is not None:
   print("{0}\t{1}".format(oldKey, salesTotal))
