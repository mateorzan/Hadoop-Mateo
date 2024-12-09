import sys


for line in sys.stdin:
        data = line.strip().split("\t")
        
        # Data validation
        if len(data) != 6:
            continue
        
        try:
            # Unpack fields
            date, time, store, item, cost, payment = data
            
            # Validate cost (convertible to float)
            float(cost)
            
            # Output for stdout in format: category\tcost
            print("{0}\t{1}".format(item, cost))
        
        except (ValueError, IndexError):
            # Ignore lines with invalid data
            continue
