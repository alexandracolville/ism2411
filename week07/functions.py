# 1. I found the missing colon first. I found it through the traceback. It shows that I ran the code first.
# 2. It takes into account the price and tier, and calculates what the new price is with the price and discount included. I do not beleve that a collegue could use it without some understanding of the tiers and how to input values. 
# 3. No AI used. For the exception of the part that the AI was asked to be used. There, it helped me troubleshoot the code.

# Exercise 1

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate 

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # $7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # $20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold": 
         return price * 0.85
    elif tier =="silver":
        return price * 0.90
    elif tier =="bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")


 # Exercise 3

 # Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax =calculate_tax(discounted, .07)
after_tax =discounted+tax
print(f"After gold discount: ${after_tax:,.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax 

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "Silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
   total = final_price(price, tier, 0.07)
   print(f"Price: ${price:,.2f}, Tier: {tier}, Final: ${total:,.2f}")


# Exercise 6 

x = 100

def double_it():
  x= 999 # local apple, not the same as above
  return x * 2

print(x)
print(double_it())
print(x)