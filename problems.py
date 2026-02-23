
# variables
age = 21
print(age)

a = 10
b = 20

print(a + b)

name = "my name is sudeep"
print(name)
# strings

city = "bengeluru"
print(city.upper())
print(city.lower())
print(city.capitalize())

s = "python"
print(s[0])

s1 = "sudeep"
s2 = "talawar"
print(s1 + " " + s2)

# Lists
list = [1, 2, 3, 4, 5]
print(list[2])

list.append(6)
list.remove(3)
list.insert(2, 10)
print(list)

# Tuples
tuple = ("yellow", "green", "blue")
print(tuple[1])

t = (1, 3, 5, 7, 9, 5)
print(t.count(5))
print(t.index(7))
print(t[2:5])

# Data types
x = 10
y = 3.14
z = "hello"
print(type(x))
print(type(y))
print(type(z))

x = "50"
print(int(x) + 10)

x = 25
print(str(x) + " is a number")

# operatos
a = 10
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# dictionaries
dict = {
    "name": "sudeep", 
        "age": 21, 
        "city": "bengeluru"
        }
print(dict["age"])
print(dict.get("name"))

dict["grade"] = "A"
dict["age"] = 22
print(dict)

# conditional statements
number = 0
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

vote = 17
if vote >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")

number = 33
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")

signal = "green"
if signal == "red":
    print("stop")
elif signal == "yellow":
    print("wait")
else:
    print("go")


