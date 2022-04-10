class Gizmo:
    def __init__(self) -> None:
        print(f'Gizmo id: {id(self)}')


x = Gizmo()
try:
    y = Gizmo() * 10
except TypeError:
    print(dir())
    print('* But variable y was never created.')
