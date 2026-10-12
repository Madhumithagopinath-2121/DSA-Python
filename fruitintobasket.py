
n = int(input("Enter number of trees: "))
fruits = [0] * n

for i in range(n):
    fruits[i] = int(input("Enter fruit type: "))

left = 0
max_length = 0

type1 = -1
type2 = -1
count1 = 0
count2 = 0

for right in range(n):
    fruit = fruits[right]

    if fruit == type1:
        count1 = count1 + 1

    elif fruit == type2:
        count2 = count2 + 1

    elif count1 == 0:
        type1 = fruit
        count1 = 1

    elif count2 == 0:
        type2 = fruit
        count2 = 1

    while count1 > 0 and count2 > 0 and type1 != type2:
        break

    if fruit != type1 and fruit != type2:
        while count1 > 0 and count2 > 0:
            left_fruit = fruits[left]

            if left_fruit == type1:
                count1 = count1 - 1
            else:
                count2 = count2 - 1

            left = left + 1

        if count1 == 0:
            type1 = fruit
            count1 = 1
        else:
            type2 = fruit
            count2 = 1

    length = right - left + 1

    if length > max_length:
        max_length = length

print(max_length)
