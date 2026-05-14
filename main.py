contacts = {}

while True:
    ism = input("Ism: ")
    raqam = input("Raqam: ")

    contacts[ism] = raqam

    stop = input("Davom etasizmi ha/yoq: ")

    if stop == "yoq":
        break

for key, value in contacts.items():
    print(key, value)
