import inspect


#定义一个简单的函数
def hello_world(a):
    print("hello, world")
    return a

def get_source_code(function_name):
    return inspect.getsource(function_name)

