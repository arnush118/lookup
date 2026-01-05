phone = input('Please enter your phone number: ').strip()

numbers = {
    "3215645": "Alex",
    "546332": "John",
    "7754607": "Bob",
    "129800": "Tim"
}

owner = numbers.get(phone)
if owner:
    print(f"The number belongs to {owner}")
else:
    print("Number not found")
