registry = []


def register(func):
    print(f'running register({func})')
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


@register
def f3():
    print('running f3()')


def main():
    print('running main()')
    print('registry ->', registry)


if __name__ == '__main__':
    main()
