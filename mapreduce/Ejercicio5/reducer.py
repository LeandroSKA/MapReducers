#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

total=0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    thisSale = data_mapped

    # Escribe un par key:value ante un cambio na key
    # Reinicia o total

    venta = float(thisSale[0])
    total=total + venta

print(total)

