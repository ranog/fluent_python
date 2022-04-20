list_1 = [3, [66, 55, 44], (7, 8, 9)]
list_2 = list(list_1)
list_1.append(100)
list_1[1].remove(55)
print('list_1:', list_1)
print('list_2:', list_2)

list_2[1] += [33, 22]
list_2[2] += (10, 11)
print('list_1:', list_1)
print('list_2:', list_2)
