import sys

current_payment = None
max_cost = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    payment, cost = data
    try:
        cost = float(cost)
    except ValueError:
        continue

    if current_payment and current_payment != payment:

        print("{0}\t{1}".format(current_payment, max_cost))
        max_cost = 0

    current_payment = payment
    max_cost = max(max_cost, cost)

if current_payment is not None:
    print("{0}\t{1}".format(current_payment, max_cost))
