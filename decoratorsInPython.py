from functools import wraps

def makebold(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<b>" + fn(*args, **kwargs) + "</b>"
    return wrapper

def makeitalic(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return "<i>" + fn(*args, **kwargs) + "</i>"
    return wrapper

@makebold
@makeitalic
def hello():
    return "hello world"

@makeitalic
@makebold
def log(s):
    return s

print( hello())        # returns "<b><i>hello world</i></b>"
print( hello.__name__ )# with functools.wraps() this returns "hello"
print( log('hello'))   # returns "<b><i>hello</i></b>"