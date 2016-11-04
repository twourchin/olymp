import sys

SOUND_SPEED = 340.0

string_in = ' '.join([value.strip() for value in sys.stdin.readlines()])
arr = [int(value) for value in string_in.split(' ')]

arr_delta = []
for i in range(1, len(arr), 2):
    arr_delta.append(arr[i+1]-arr[i])

arr_delta.sort()
len_div = len(arr_delta)//2

if len(arr_delta) % 2 == 0:
    M = (arr_delta[len_div]+arr_delta[len_div-1])/2
else:
    M = arr_delta[len_div]

print('{:.4f}'.format(SOUND_SPEED*(M/2)/1000))
