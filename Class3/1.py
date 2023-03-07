def fun1():
    fun1.var = 100
    print(fun1.var)

def fun2():
    return fun1()

fun1()
fun2()

