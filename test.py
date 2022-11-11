#name = input("Как вас зовут?")
#print(f"Привет, {name}")

#name = input("Как Вас зовут? ")
#print("Привет,", name)

#print("2 + 2 = 4" * 3, sep="\n")

#phrase = input()
#print(phrase * 3)

#name = input("Как Вас зовут? ")
#print('Привет, %' .format(name))

#name = input("Как Вас зовут? ")
#print("Привет, ", name, sep="")

# goods = input()
# price = int(input())
# weight = int(input())
# cash = int(input())
# sum = cash - (weight * price)
# print('Чек')
# print(f'{goods} - {weight}кг - {price}руб/кг')
# print(f"Итого: {weight * price}руб")
# print(f"Внесено: {cash}руб")
# print(f"Сдача: {sum}руб")

#username = input("Как Вас зовут? ")
#print('Привет, %s' % username)

# phrase = int(input())
# print(phrase * "Купи слона!\n")

# count = int(input())
# phrase = input()
# print(f'Я больше никогда не буду писать "{phrase}"!\n' * count)

# minute = int(input())
# children = int(input())
# sum = (minute / 2) * children
# print(int(sum))

# name_child = input()
# number = int(input())
# group = number // 100
# print(f"Группа №{group}.")
# print(f"{number % 10}. {name_child}.")
# print(f"Шкафчик: {number}.")
# print(f"Кроватка: {number // 10 % 10}.")

# number = int(input())
# first = number % 100
# first_1 = first % 10
# first_2 = first // 10
# second = number // 100
# second_1 = second % 10
# second_2 = second // 10
# print(f"{second_1}{second_2}{first_1}{first_2}")

num_1 = int(input())
num_2 = int(input())
num_1_1 = num_1 % 10
num_1_2 = num_1 // 10 % 10
num_1_3 = num_1 // 100
num_2_1 = num_2 % 10
num_2_2 = num_2 // 10 % 10
num_2_3 = num_2 // 100
sum1 = (num_1_1 + num_2_1) % 10
sum2 = (num_1_2 + num_2_2) % 10
sum3 = (num_1_3 + num_2_3) % 10
print(num_1_3, num_1_2, num_1_1)
print(num_2_3, num_2_2, num_2_1)
print(f"{sum3}{sum2}{sum1}")