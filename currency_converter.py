def usd_to_inr(usd, rate):
    return usd * rate

def inr_to_usd(inr, rate):
    return inr / rate

print("Currency Converter")
print("1. USD → INR")
print("2. INR → USD")

try:
    choice = int(input("Choose an option (1/2): "))
    amount = float(input("Enter amount: "))
    
    exchange_rate = 83.25  # Example: 1 USD = 83.25 INR
    
    if choice == 1:
        print(f"{amount} USD = {usd_to_inr(amount, exchange_rate):.2f} INR")
    elif choice == 2:
        print(f"{amount} INR = {inr_to_usd(amount, exchange_rate):.2f} USD")
    else:
        print("Invalid choice.")
except ValueError:
    print("Please enter valid numeric values.")
