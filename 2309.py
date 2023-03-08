#6. Bronze2 no.2309 일곱 난쟁이

from itertools import combinations

cowards = []

for i in range(9):
    i = int(input())
    cowards.append(i)

cowards.sort()

combi = list(combinations(cowards, 7))

for i in range(len(combi)):
    if sum(combi[i]) == 100:
        for j in range(len(combi[i])):
            print(combi[i][j])
