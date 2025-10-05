# Go Dutch - Smart Split Based on Item Sharing + (n%) Tax Split Evenly

print(" Welcome to the Go Dutch - Itemized Split App with Tax\n")

# Step 1: Input group members
num_people = int(input("How many people are there? "))
names = []
for i in range(num_people):
    name = input(f"Enter name of person {i + 1}: ").strip()
    names.append(name)

# Step 2: Input ordered items
items = []
print("\n Enter the items ordered (type 'done' when finished):")
while True:
    item_name = input("\nEnter item name (or 'done' to finish): ").strip()
    if item_name.lower() == 'done':
        break
    item_price = float(input(f"Enter price of '{item_name}': ₹ "))

    print(f"Who had '{item_name}'? (Enter names separated by commas):")
    sharers_input = input("> ").split(',')
    sharers = [name.strip() for name in sharers_input if name.strip() in names]

    if not sharers:
        print(" No valid person entered. Try again.")
        continue

    items.append({
        "name": item_name,
        "price": item_price,
        "sharers": sharers
    })

# Step 3: Calculate item-wise contributions
bill_split = {name: 0.0 for name in names}
total_before_tax = 0

for item in items:
    total_before_tax += item["price"]
    if len(item["sharers"]) == 1:
        # Single person pays full
        person = item["sharers"][0]
        bill_split[person] += item["price"]
    else:
        # Shared cost
        split_price = item["price"] / len(item["sharers"])
        for sharer in item["sharers"]:
            bill_split[sharer] += split_price

# Step 4: Add tax
tax = int(input("enter the amount of tax: "))
tax_rate= tax/100
tax_amount = total_before_tax * tax_rate
tax_per_person = tax_amount / num_people

for name in bill_split:
    bill_split[name] += tax_per_person

# Step 5: Show final results
print("\n Final Amounts to Pay (with",tax,"% Tax):\n")
total_after_tax = 0
for name in names:
    amount = round(bill_split[name], 2)
    total_after_tax += amount
    print(f"{name} should pay: ₹{amount:.2f}")

print(f"\n Subtotal (before tax): ₹{total_before_tax:.2f}")
print(f"Tax {(tax)}% : ₹{tax_amount:.2f}")
print(f" Total Bill (with tax): ₹{total_after_tax:.2f}")