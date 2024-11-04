a, b = 0, 1 # Multiple assignment

# while a < 10:
#     print(a)
#     a, b = b, (a + b)

i = 20
print('The value of i is', i) # Strings are printed without quotes, a space is inserted between items.
# The value of i is 20

# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:

while a < 10:
    # print(a, end=',') # 0,1,1,3,5,8
    print(a, end='') # 0112358
    a, b = b, (a + b)