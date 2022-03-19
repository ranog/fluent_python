from demo_nt import DemoNTClass

print(DemoNTClass.__annotations__)
print(DemoNTClass.a)
print(DemoNTClass.b)
print(DemoNTClass.c)
print(DemoNTClass.__doc__)

nt = DemoNTClass(8)
print(nt.a)
print(nt.b)
print(nt.c)
