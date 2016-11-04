import sys

DIRECTIONS = {'N': [0,-1],
              'S': [0,1],
              'W': [-1,0],
              'E': [1,0],
              'H': [0,0] }

arr_strings = (' '.join([value.strip() for value in sys.stdin.readlines()])).split(' ')

q1_route = []
for i in range(1,int(arr_strings[0])*2,2):
    q1_route.append([arr_strings[i], int(arr_strings[i+1])])

q2_route = []
for i in range(int(arr_strings[0])*2+2,len(arr_strings),2):
    q2_route.append([arr_strings[i], int(arr_strings[i+1])])

q1 = [0, 0]
q2 = [-35, 10]

def route_step(step, position):
    q = position[:]
    q[0]+= DIRECTIONS[step[0]][0]
    q[1]+= DIRECTIONS[step[0]][1]
    return q

timer = 0
stop = False
while(not stop):
    if q1[0]==q2[0] and q1[1]==q2[1]:
        print(timer)
        quit()

    q1=route_step(q1_route[0],q1)
    q2=route_step(q2_route[0],q2)

    timer+=1

    q1_route[0][1]-=1
    q2_route[0][1]-=1

    if (q1_route[0][1] < 1):
        q1_route.pop(0)
    if (q2_route[0][1] < 1):
        q2_route.pop(0)

    if len(q1_route)*len(q2_route) == 0:
        stop = True
