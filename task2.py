import sys

arr = [int(value) for value in ' '.join(sys.stdin.readlines()).strip().split(' ')]
arr_sort = []

for i in range(0, len(arr)-1):
    arr_sort.append([arr[i+1]-arr[i], i, arr[i+1], arr[i]])

arr_sort.sort(key=lambda value: value[0])
all_count = sum(arr)

count = 0
for i in range(len(arr_sort)-1,0,-1):
    value = arr_sort[i]
    if arr[value[1]] != 0 and arr[value[1]+1] !=0:
        tmp_count = count + arr[value[1]+1]*2
        tmp_all_count = all_count - arr[value[1]+1] - arr[value[1]]

        if (tmp_count+tmp_all_count<count+all_count):
            break

        arr[value[1]] = 0
        arr[value[1]+1] = 0
        count = tmp_count
        all_count = tmp_all_count

print(count+all_count)
