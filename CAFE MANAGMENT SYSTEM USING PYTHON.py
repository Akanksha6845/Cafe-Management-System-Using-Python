menu = {
    "Cheeseburger": 70,
    "Cheese_sandwich": 45,
    "Chicken_burgers": 90,
    "Spicy_chicken": 150,
    "Hot_dog": 120,
    "Cold coffee": 40,
    "Hot Chocolate": 120,
    "Fries": 60,
}

print("Welcome To Our Cafe !!")
print("Here's Our Menu.....\n")
for item, price in menu.items():
    print(f"{item}: {price}")

total_bill = 0
ordered_items = []

while True:
    order = input("\nWhat do you want to order? : ").strip().title()

    if order in menu:
        total_bill += menu[order]
        ordered_items.append(order)
    else:
        print("Sorry, we don't have that item.")

    more = input("Do you want to order more? (Yes/No): ").strip().lower()
    if more == "no":
        break

if "Cold Coffee" in ordered_items and len(ordered_items) == 1:
    print("Sorry, you can't order just coffee.")
else:
    Coupon = input("Do you have a coupon code? If yes, enter it: ").strip()
    if Coupon == "CAFE500":
        discount = total_bill * 0.2
        total_bill -= discount
        print(f"Your bill after 20% discount: {total_bill:.2f}")
    else:
        print(f"Your total bill is: {total_bill}")

print("Thank you for ordering!")
