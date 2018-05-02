# Implicit Data Type Conversion of primitives

a = 1
print("Type is {} \t value is {}".format(type(a), a))

b = 9.0000
print("Type is {} \t value is {}".format(type(b), b))

c = 'string'
print("Type is {} \t value is {}".format(type(c), c))

d = False
print("Type is {} \t value is {}".format(type(d), d))


# Explicit Data type conversion of primitives
# Type conversion of Float to Integers
e = 9.0544
print("Type is {} \t value is {}".format(type(e), e))

f = int(e)
print("Type is {} \t value is {}".format(type(f), f))

# Type conversion of Integers to Float
g = 544
print("Type is {} \t value is {}".format(type(g), g))

h = float(g)
print("Type is {} \t value is {}".format(type(h), h))

# Type conversion of Integers to String
var_a = 10
var_b = 20
var_c = var_a + var_b
print("Type is {} \t value is {}".format(type(var_c), var_c))

# Type conversion of String to Integers
var_i = '15'
var_j = '25'
var_k = int(var_i) + int(var_j)
print("Type is {} \t value is {}".format(type(var_k), var_k))

# Type conversion of String to Float
var_x = '15'
var_y = '25'
var_z = float(var_x) + float(var_y)
print("Type is {} \t value is {}".format(type(var_z), var_z))

# Type conversion of Non Primitive data types

# convert tuple to list
a_tuple = (1,2,3,4,5,6,7,8,9,10)
a_list = list(a_tuple)
print("Type is {} \t value is {}".format(type(a_list), a_list))

# convert list to tuple
b_list = [1,2,3,4,5]
b_tuple = tuple(b_list)
print("Type is {} \t value is {}".format(type(b_tuple), b_tuple))

# convert String to tuple
a_string = "Shakir Gooty"
a_tuple = tuple(a_string)
print("Type is {} \t value is {}".format(type(a_tuple), a_tuple))

# convert String to list
c_string = "Shakir Gooty"
c_list = list(a_string)
print("Type is {} \t value is {}".format(type(c_list), c_list))
c_list.append(list("Love of my life - wife"))
print("Type is {} \t value is {}".format(type(c_list), c_list))

# Convert to Binary Number
a_int = 100
a_binary = bin(100)
print("Type is {} \t value is {}".format(type(a_binary), a_binary))

# Convert Binary to Decimal Numbers
b_binary = '1100100'
b_int = int(b_binary,2)
print("Type is {} \t value is {}".format(type(b_int), b_int))


# Convert to Octal  Number
a_int = 100
a_oct = oct(100)
print("Type is {} \t value is {}".format(type(a_oct), a_oct))

# Convert Octal to Decimal Numbers
b_oct = '144'
b_int = int(b_oct,8)
print("Type is {} \t value is {}".format(type(b_int), b_int))

