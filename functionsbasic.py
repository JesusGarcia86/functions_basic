#1 Predicted output 5, Actual output 5
def a():
    return 5
print(a())

#2 Predicted output 10, Actual output 10
def a():
    return 5
print(a()+a())

#3 Predicted output 5, Actual output 5
def a():
    return 5
    return 10
print(a())

#4 Predicted Outpot 5, Actual output 5, only the first value prints which is return 5
def a():
    return 5
    print(10)
print(a())

#5 Predicted output 5, Actual output shows 5, none. Don't actually get where the none comes from.
def a():
    print(5)
x = a()
print(x)

#6 Predicted output 8, Actual output 3,5. Thought it would be 3+5 which is 8.
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7 Predicted output 25, Actual output 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 Predicted output 10, Actual output showed a syntax error on line 7 which is the else:, couldn't figure it out.
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
	else:
		        return 10
return 7
print(a())

#9 Predicted output 7, 14, 21. Actual output 7, 14, 21.
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#10 Predicted output 8. Actual output 8.
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11 Predicted output 500,500,300,500. Actual output 500,500,300,500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 Predicted output 500,500,300,500. Actual output 500,500,300,500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

#13 Predicted output 500,500,300,300. Actual output 500,500,300,300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#14 Predicted output 1,3,2. Actual output 1,3,2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#15 Predicted output 1,3,10,5. Actual output 1,3,5,10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)