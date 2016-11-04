import sys

count = 0
try:
    N = int(sys.stdin.readlines()[0])
except:
    print("ERROR")
    quit()

def number_sum(N):
    ret = 0
    while(N!=0):
        ret = ret + N % 10;
        N = N // 10
    return ret

def integer_div(N):
    if (N % number_sum(N)) == 0:
        return 1
    else:
        return 0

for i in range (1, N+1):
    count += integer_div(i)

print(count)
