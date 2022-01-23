fruits = ['grape', 'raspberry', 'apple', 'banana']
print(f'no sorted(): {fruits}')
print(f'with sorted(): {sorted(fruits)}')
print(f'after sorted(): {fruits}')
print(f'with sorted() and reverse=True: {sorted(fruits, reverse=True)}')
print(f'with sorted() and key=len: {sorted(fruits, key=len)}')
print(f'with sorted(), key=len, and reverse=True: {sorted(fruits, key=len, reverse=True)}')
print(f'no sorted(): {fruits}')
print(f'with sort(): {fruits.sort()}')
print(f'after sort(): {fruits}')