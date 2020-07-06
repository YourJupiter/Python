def function():
    var = 'локальна змінна'
    print(var)
var = 'глобальна змінна'
function()
print(var)

def function():
    global var
    print(var)
    var = 'нове значення'
    print(var)
var = 'глобальна змінна'
function(); print(var)

def function(c, d):
    global a, b
    a = 5;
    b = 7
    c = 10
    d = 12
a, b, c, d = 1, 2, 3, 4
print(a, b, c, d) 
function(c, d)
print(a, b, c, d)
