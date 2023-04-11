# 11. Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.


a = int(input('input number: '))
i = 1
j = 1
sum =0
for index in range(1, a):
    sum = i + j
    i = j
    j = sum
    if sum == a:
        print(f'index {index}. Sum ={sum}')
    print(sum)

# 9. По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0!
# = 1 Решить задачу используя цикл while

number = int(input("Input number: "))
i = 1
sum = 1

while i <= number:
    sum *= i
    i += 1
print(sum)
# 11. Дано натуральное число A > 1. Определите, каким
# по счету числом Фибоначчи оно является, то есть выведите
# такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.

a = int(input("Input number: "))

i = 0
j = 1
sum = 0
for index in range(1, a):
    sum = i + j
    i = j
    j = sum
    print(f"{index} - {sum}")
    if sum == a:
        print(f"Index {index}. Number = {sum}")
        break
else:
    print("-1")