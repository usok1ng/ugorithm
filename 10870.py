#5. Bronze2 no.10870 피보나치 수 5

n = int(input())

fib = [0, 1]

for i in range(2, n+1):
    next = fib[i-1] + fib[i-2]
    fib.append(next)

print(fib[n])