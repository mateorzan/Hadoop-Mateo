import sys

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 6:
        continue

    try:
        date, time, store, item, cost, payment = data
        cost = float(cost)
        print("{0}\t{1}".format(payment, cost))
    except (ValueError, IndexError):
        continue