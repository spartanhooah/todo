password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for char in password:
    if char.isdigit():
        digit = True
        break

result.append(digit)

upper = False
for char in password:
    if char.isupper():
        upper = True
        break

result.append(upper)

if all(result):
    print("Strong password")
else:
    print("Weak password")
