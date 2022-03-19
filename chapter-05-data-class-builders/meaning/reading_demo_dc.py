from demo_dc import DemoDataClass

print(DemoDataClass.__annotations__)
print(DemoDataClass.__doc__)

print(DemoDataClass.b)
print(DemoDataClass.c)
# print(DemoDataClass.a)

dc = DemoDataClass(a=9)
print(dc.a)
print(dc.b)
print(dc.c)

dc.a = 10
dc.b = 'oops'
dc.c = 'whatever'
dc.z = 'secret stash'
print(dc.a, dc.b, dc.c, dc.z)
