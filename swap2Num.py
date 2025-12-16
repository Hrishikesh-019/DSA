# Swap Two Numbers
# a=int(input("Enter a number:"))
# b=int(input("Enter b number:"))
# a,b=b,a
# print('After Swapping:')
# print("a=",a)
# print("b=",b)

# Reverse a String With slicing.

# a="Rishi"
# print(a[::-1])
# print(a[1::])
# print(a[::-2])
# print(a[::3])
# print(a[2::-2])

# Reverse a String Without slicing.
s="Rishi"
rev=''
for i in s:
    rev=i+rev
print(rev)