# print("Hello")

# print("Hello world")

# * Variables in python
# a = 5
# b = "apple"
# pi = 3.14

# print(a)
# print(b)
# print(type(pi))

# * Input in python
# a = int(input("Enter fitst number: "))
# b = int(input("Enter second number: "))

# print(a+b)

# name = input("Enter your name")
# print(name)


# * Conditionals in python

# a = 20
# b = 20

# if a > b:
#     print("A is bigger")
# elif a == b:
#     print("Both are same")
# else:
#     print("B is bigger")


# * Strings in python
# a = "Hello, World!"
# replaced = a.replace("H", "J")
# print(a)
# print(replaced)

# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']

# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59.00
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x == y)  #True
# print(x is y)  # False


#* Loop on list
fruits = ["apple", "mango", "banana"]

for i in fruits:
    print(i)

length = len(fruits)
print(length)

for i in range(3):
    print(i)

for i in range(len(fruits)):
    print(fruits[i])