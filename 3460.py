## Bronze3 no.3460 이진수

t = int(input())

while t > 0:
    n = int(input())
    arr = []
    cnt = 0
    while n > 0:
        if n % 2 == 1:
            arr.append(cnt)
        n //= 2
        cnt += 1
    for i in range(len(arr)):
        print(arr[i], end = ' ')
    t -= 1