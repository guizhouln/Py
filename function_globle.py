# function_globle.py
x = 50


def func() -> object:
    global x

    print("x is", x)
    x = 2
    print("changed globle x to", x)


func()
print("Value of x is ", x)
