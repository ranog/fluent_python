import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
memory_view = memoryview(numbers)

print(len(memory_view))
print(memory_view[0])

memory_view_octets = memory_view.cast('B')
print(memory_view_octets.tolist())
memory_view_octets[5] = 4

print(numbers)
