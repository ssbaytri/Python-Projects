# Compound Interest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amout: "))
    if principle < 0:
        print("Invalid value for principle.")
    else:
        break

while True:
    rate = float(input("Enter the rate amout: "))
    if rate < 0:
        print("Invalid value for rate.")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Invalid value for time.")
    else:
        break

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
