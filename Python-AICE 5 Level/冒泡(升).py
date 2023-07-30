array = [8, 3, 6, 5, 7]
for i in range(len(array) - 1):
    for j in range(len(array) - 1 - i):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)
