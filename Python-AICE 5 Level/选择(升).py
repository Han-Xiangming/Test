array = [8, 3, 6, 5, 7]
for j in range(len(array) - 1):
    minindex = j
    for i in range(minindex + 1, len(array)):
        if array[minindex] > array[i]:
            minindex = i
    array[j], array[minindex] = array[minindex], array[j]
print(array)
