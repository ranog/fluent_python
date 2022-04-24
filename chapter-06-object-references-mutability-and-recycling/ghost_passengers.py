from danger_of_a_mutable_default import HauntedBus

bus1 = HauntedBus(passengers=['Alice', 'Bill'])
print(f'Bus One: {bus1.passengers}')

bus1.pick(name='Charlie')
bus1.drop(name='Alice')
print(f'Bus One: {bus1.passengers}')

bus2 = HauntedBus()
bus2.pick(name='Carrie')
print(f'Bus Two: {bus2.passengers}')

bus3 = HauntedBus()
print(f'Bus Three: {bus3.passengers}')

bus3.pick(name='Dave')
print(f'Bus Two: {bus2.passengers}')

print(f'Bus Two is Bus Three? {bus2.passengers is bus3.passengers}')
print(f'Bus One: {bus1.passengers}')
