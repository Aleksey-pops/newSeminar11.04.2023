# 15. Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно
# выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.
from random import random

melonCount = int(input("Input melon counts: "))
massMin = 30000
massMax = 0

for i in range(1, melonCount + 1):
    mass = random.randrange(10000, 30001)
    # mass = int(input("Input mass: "))
    print(mass, end=", ")
    if mass < massMin:
        massMin = mass
    elif mass > massMax:
        massMax = mass
print(f"\nMass: {massMin} {massMax}")

# Простое число определить

#  2,3, 5,7
# Простое число определить

number = int(input("Input number: "))

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        print("Not simple")
        break
else:
     print("Simple")

# if number % 2 != 0 or number % 3 != 0 or number % 5 != 0 or number % 7 != 0:
#     print("ok")
# else:
#     print("not ok")
    # 2,3,5,7


    # number ** 0.5