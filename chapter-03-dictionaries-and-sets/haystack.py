haystack = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs', 'burguer', 'spam', 'spam', 'eggs', 'bacon', 'fruit']
needles = ['eggs', 'spam', 'bacon', 'salad', 'fruit']

found = len(set(needles) & set(haystack))  # Ex 3-12. Count occurrences of needles in a haystack, both of type set
print(f'ex 3-12: {found}')

found = 0  # Ex 3-13. Count occurrences of needles in a haystack (same end result as Ex 3-12)
for n in needles:
    if n in haystack:
        found += 1
print(f'ex 3-13: {found}')

# another way:
found = len(set(needles).intersection(haystack))    # Ex 3-14. Count occurrences of needles in a haystack;
print(f'ex 3-14: {found}')                          # these lines work for any iterable types
