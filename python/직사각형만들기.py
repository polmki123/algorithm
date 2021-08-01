import math 
import sys

n = 0
k = 0 
board = []

sumA = [0] * ( 1 << 16 )
half = [0] * ( 1 << 16 )


# n = int(sys.stdin.readline().rstrip())
# board = list(map( int, sys.stdin.readline().split()))
# print(board)
n = 6
board = [1, 3, 3, 3, 5, 7]
board.sort()

k = (1 << n) - 1
 
for i in range(1, k + 1) :
    # 000001 ~~ 111111
    for j in range(0, n ): 
        # 1, 2, 3, 4, 5, 6
        if (i & (1 << j)) :
            # 000001 000001 
            # 000010 000001
            # 000010 000010
            # 000110 000001
            # 000110 000011
            # 모든 나뭇가지의 덧셈 구하기 
            sumA[i] += board[j]
            

for i in range(1, k + 1) :
    # 만약 sumA[i] 가 공백이면 0 이 된다. 
    if (sumA[i] & 1):
        continue

    # 현재 분기 최대 나뭇가지 합의 값 
    j = i
    while j :
        # 만약 001000 000100 과 같다면 
        if (sumA[j] == (sumA[i] >> 1)) :
            # 그 분기를 True로 나둔다. 
            half[i] = True
            break
        # j 가 i와 and가 될 때 까지 반복 
        # j - 1 & i 라는 것은 
        # 001000 -1 => 000111 & 0010000이면 그만 반대로 
        # 001110 -1 => 001101 & 001110 -> 001100
        #              001011 & 001110 -> 001010
        #              001001 & 001110 -> 001000
        #              000111 & 001110 -> 000110 
        #              000101 & 001110 -> 000100 
        #              000011 & 001110 -> 000010 
        #              000001 & 001110 -> 000000 

        j = (j - 1) & i

ans = -1
# 0111111
i = k

while i :
    # 000001
    # 000010
    # 000011
    # 000100

    x = (~i&k)
    j = x
    if i < k/2 :
        break
    while j :
        if (half[i] & half[j]) :
            print( "i, j", i, j, sumA[i], sumA[j], sumA[i] * sumA[j], sumA[i] * sumA[j]  >> 2 )
            ans = max(ans, sumA[i] * sumA[j] >> 2)

        j = ((j - 1) & x) 

    # 내림 차순으로 구해짐 
    # 0111111
    # 0111110
    # 0111101
    # 0111001
    i = ((i - 1)&k)

print(ans)
