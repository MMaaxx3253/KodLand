import random
elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
userpasswd_len = int(input("Длина пароля для генерации:"))
password = ""

for i in range(userpasswd_len):
    password += random.choice(elements)

print(password)
