#4. Bronze3 no.2460 지능형 기차

station = []
people = 0

for i in range(10):
    a, b = map(int, input().split())
    people = people - a + b
    station.append(people)

print(max(station))