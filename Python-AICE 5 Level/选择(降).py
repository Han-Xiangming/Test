array = [8, 3, 6, 5, 7]
for j in range(len(array) - 1):
    maxindex = j
    for i in range(maxindex + 1, len(array)):
        if array[maxindex] < array[i]:
            maxindex = i
    array[maxindex], array[j] = array[j], array[maxindex]
print(array)
