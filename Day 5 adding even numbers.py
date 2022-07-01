#Write your code below this row 👇
list_num = list()


for num in range(2, 101, 2):
    list_num.append(num)
    add_num = sum(list_num)
print(add_num)

total = 0
for num in range(2, 101, 2):
    total += num

print(total)

total2 = 0
for num in range(1, 101):
    if num % 2 == 0:
        total2 += num
print (total2)
