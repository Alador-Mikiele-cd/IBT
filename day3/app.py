totals = {}

try:
    file = open("transactions.txt", "r")
    for line in file:
        name, amount = line.strip().split(",")
        amount = float(amount)
        totals[name] =   amount
        
    file.close()

    report = open("report.txt", "w")

    for name in sorted(totals, key=totals.get, reverse=True):
        print(name, totals[name])
        report.write(name + ": " + str(totals[name]) + "\n")

    report.close()

except FileNotFoundError:
    print("transactions.txt not found.")

