##Square Of Number
def SquarOfNum(a):
    return a**a
res=SquarOfNum(5)
print(res)

# return

# Sends value back

# Can be reused

# Used in interviews & real projects

# FUNCTIONAL ARGUMENTS

# Positional Argumets
def greet(name, city):
    print (name, city)
greet("Rishi,", "Hyderabad")

# Default Argument
def greet(name, city="Hyderabad"):
    print(name,city)
greet("Rishi")

# *args Multiple Arguments

def multiples(*numbers):
    total=1
    for n in numbers:
        total*=n
    return total
print(multiples(1,2,3,4,5))
