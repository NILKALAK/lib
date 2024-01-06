# Use dir() to list functions in a library

def list_functions(module):
    funcs = [func for func in dir(module) if callable(getattr(module, func))]
    print(funcs)