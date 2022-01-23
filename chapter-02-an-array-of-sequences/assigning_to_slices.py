example_list = list(range(10))
print(f'example_list = list(range(10)) == {example_list}')

example_list[2:5] = [20, 30]
print(f'example_list[2:5] = [20, 30] == {example_list}')

del example_list[5:7]
print(f'del example_list[5:7] == {example_list}')

example_list[3::2] = [11, 22]
print(f'example_list[3::2] = [11, 22] == {example_list}')

example_list[2:5] = [100]
print(f'example_list[2:5] = [100] == {example_list}')

example_list[2:5] = 100
