#3. Bronze3 no.10818 최소, 최대

N = int(input())

integer = list(map(int, input().split()))

max = integer[0]
min = integer[0]

for i in range(len(integer)):
    if integer[i] > max:
        max = integer[i]

for i in range(len(integer)):
    if integer[i] < min:
        min = integer[i]

print(min, max)


