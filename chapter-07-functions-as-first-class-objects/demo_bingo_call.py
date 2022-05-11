from bingo_call import BingoCage

bingo = BingoCage(range(3))

print(bingo.pick())
print(bingo())
print(callable(bingo))
