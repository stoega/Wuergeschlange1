import sys

duration = int(input("Please enter the duration of your subscription (in months): "))

if(duration <= 0):
    print("Invalid subscription duration")
    sys.exit()

price = 0.0
if(duration < 6):
    price = 6.5
elif(duration < 12):
    price = 5.9
else:
    postal = int(input("Please enter your postal code: "))
    if(postal < 1000 or postal > 9999):
        print("Invalid postal code")
        sys.exit()
    fee = int(postal/10) - (int(postal / 1000))*100
    price = (4+fee/100)
cost = duration * price
print(f"The price per month is {price: .2f}")
print(f"The full price for {duration} months is {cost: .2f}")
