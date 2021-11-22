registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__=='__main__':
    main()


"""
running register(<function f1 at 0x7f83babf5670>)
running register(<function f2 at 0x7f83babf5700>)
running main()
registry -> [<function f1 at 0x7f83babf5670>, <function f2 at 0x7f83babf5700>]
running f1()
running f2()
running f3()
"""