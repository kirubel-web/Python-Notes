#if statement
def max_num(a,b,c):
    if a > b and a > c:
        print("a is larger")
        return a
    elif b > a and b > c:
        print("b is larger")
        return b
    elif c > a and c > b:
        print("c is larger")
        return c 
    else:
        print("invalid entry")
x = int(input("Enter a: "))
y = int(input("Enter b: "))
z = int(input("Enter c: "))
print(max_num(x,y,z))