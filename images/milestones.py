# This program calculates the price of a meal, sales tax, total,and change.
child_meal_price = float(input("what is the price of a child's meal? "))
adult_meal_price = float(input("what is the price of an adult's meal? ")) 
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
child_subtotal = child_meal_price * children
adult_subtotal = adult_meal_price * adults
subtotal = child_subtotal + adult_subtotal
print(f"Subtotal: ${subtotal:.2f}")
tax_rate = float(input("what is the sales tax rate?"))
sales_tax = subtotal * tax_rate / 100
print(f"Sales Tax: ${sales_tax:.2f}")
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")
payment_amount = float(input("What is the payment amount?"))
change = payment_amount - total
print(f"Change: ${change:.2f}")


