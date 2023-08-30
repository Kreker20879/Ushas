import random 
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
long = int(input("Длинна пароля"))
for i in range(long):
    capybara = random.choice(password)
    print(capybara)