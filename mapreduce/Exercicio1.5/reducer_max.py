#!/usr/bin/python
import sys

ventas = 0

for line in sys.stdin:
    sale = line.strip()
    sale = float(sale)
    ventas += sale

print(ventas)
