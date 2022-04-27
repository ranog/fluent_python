from twilightbus import TwilightBus

basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
bus = TwilightBus(basketball_team)
bus.drop('Tina')
bus.drop('Pat')

print(f'basketball team list: {basketball_team}')
print(f'bus passengers list: {bus.passengers}')
