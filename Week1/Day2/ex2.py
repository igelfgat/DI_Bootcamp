a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a)
print(b)
print(c)
print(d)

name, age = "Ilya", 25
print(name)
print(age)


letter_lower = ["a", 'b', 'c', 'd']
letters_upper = [char.upper() for char in letter_lower]
print(letters_upper)