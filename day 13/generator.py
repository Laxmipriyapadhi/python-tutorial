# while loop
def creater():
    i=1
    while i<= 100:
        yield i
        i += 1
print(creater())
x=creater()
print(list(x))

# for loop

def fibonacci_generator():
    a=0
    b=1
    for i in range(10):
        yield b
        a,b = b,a+b

obj = fibonacci_generator()

print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
