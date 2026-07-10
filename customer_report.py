customers = [
 ("Almaz", 1500), ("Dawit", 700), ("Tigist", 200),
 ("Hanna", 1200), ("Semhal",450),("Alador",900)
]

premium = 0
standard = 0
basic = 0

def tier(balance):
    if balance >= 1000:
        return 'Premium'
    elif balance >= 500:
        return "Standard"
    return "Basic"

for name , balance in customers:
    customer_tier = tier(balance)
    print("---------------------------------")
    print(f"Name: {name}")
    print(f'Balance: {balance} ETB')
    print(f'Tier: {customer_tier}')
    print("---------------------------------")
    

    if customer_tier == 'Premium':
        premium += 1
    elif customer_tier == "Standard":
        standard += 1
    else :
        basic += 1



print("---------------------------------")
print("---------------------------------")

print(f'{premium} Premium users')
print(f'{standard} Standard users')
print(f'{basic} Basic users')


