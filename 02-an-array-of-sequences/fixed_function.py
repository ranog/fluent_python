def fixed(any_object):
    try:
        hash(any_object)
    except TypeError:
        return False
    return True


tuple_fixed = (10, 'alpha', (1, 2))
tuple_mutable = (10, 'alpha', [1, 2])

print(fixed(tuple_fixed))
print(fixed(tuple_mutable))
