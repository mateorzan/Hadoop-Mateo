import sys

max_sale = 0

for line in sys.stdin:
    try:
        sale = float(line.strip())
        max_sale = max(max_sale, sale)
    except ValueError:
        continue

print("{0}".format(max_sale))
