from functools import partial
from tag import tag

print(tag)

picture = partial(tag, 'img', class_='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture.func)
print(picture.args)
print(picture.keywords)
