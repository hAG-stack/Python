contacts = {
    "Ahmed": "01012345678",
    "Sara": "011598714562",
    "Mona": "01255918453"
}

print("Contacts")

for name in contacts:
    print(name)

search_name = input("\nEnter the name you want to search for: ")

if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found")