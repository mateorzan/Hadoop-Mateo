#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# Lista para almacenar os resultados
lista = []


for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    thisKey, thisSale = data_mapped

    # Escribe un par key:value cando cambie a key
    # Reinicia o total
    if oldKey and oldKey != thisKey:
        lista.append("{0}\t{1}".format(oldKey, salesTotal))
        oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

    if oldKey is not None:
       lista.append("{0}\t{1}".format(oldKey, salesTotal))

# Agora escribimos os resultados no ficheiro 'sales_report.txt'
with open('sales_report.txt', 'w') as file:
    for item in lista:
        file.write(item + '\n')

print("Os resultados foron gardados en 'sales_report.txt'.")
