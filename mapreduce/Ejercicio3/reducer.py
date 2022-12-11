#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

payments={}
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total

    if thisKey not in payments:
        payments[thisKey] = float(thisSale)
    else:
        # Si el nombre ya está en el diccionario,
        # comparar el gasto actual con el gasto más alto actual
        # Si el gasto actual es mayor, actualizar el gasto más alto
        if float(thisSale) > payments[thisKey]:
            payments[thisKey] = float(thisSale)    


# Escribe o ultimo par, unha vez rematado o bucle
for pay in payments:
    print(pay, payments[pay])
