import sys
from collections import *

u, v = map( int, sys.stdin.readline().split())

arr     = [0] * 101
dist    = [0] * 101

for i in range(u + v) :
    p, d = map( int, sys.stdin.readline().split())
    dist[p] = d


deq = deque()
deq.append(1)
while deq :
    x = deq.leftpop()
    if x == 100 :
        print(arr[100])
        break
    
    for i in range(1,7) :
        if i + x > 100 :
            continue
        if arr[ i + x] == 0 and dist[ i + x] == 0 :
            arr[i + x] = arr[x] + 1
            deq.append( i+x )
        elif arr[ dist[ i + x] ] == 0 and dist[ i + x] != 0 :
            arr[ dist[ i + x] ] = arr[x] + 1
            deq.append( dist[ i + x] )