mutable_sequence = [1, 2, 3]
print(f'mutable sequence: {mutable_sequence}; id: {id(mutable_sequence)}')

mutable_sequence *= 2
print(f'mutable sequence: {mutable_sequence}; id: {id(mutable_sequence)}')

immutable_sequence = (1, 2, 3)
print(f'immutable sequence: {immutable_sequence}; id: {id(immutable_sequence)}')

immutable_sequence *= 2
print(f'immutable sequence: {immutable_sequence}; id: {id(immutable_sequence)}')
