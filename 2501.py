# [#3] Bronze3 no.2501 약수 구하기

a, b = map(int, input().split())
arr = [0]
cnt = 0

for i in range(1, a):
    if a % i == 0:
        arr.append(i)
        cnt += 1

if b > cnt:
    print(0)
else:
    print(arr[b])