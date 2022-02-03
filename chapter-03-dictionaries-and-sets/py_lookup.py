import builtins
from collections import ChainMap

pylookup = ChainMap(locals(), globals(), vars(builtins))
print(pylookup)
