squares = [1, 4, 9, 16, 25]

print(squares[-3:]) # slicing returns a new list
print(squares + [36, 49]) # support concatenation

# Unlike strings, which are immutable, lists are a mutable type, i.e. it's possible to change their content:
squares[-1] = 50
print(squares)

# add new items at the end of the list, by useing the 'list.append()' method
squares.append(7 ** 3)
print(squares)

# Python never copies data. when we assign a list to a variable, the variable refers to the existing list.
# 가변 객체에 대한 참조 개념
# 즉 두 변수는 동일한 리스트를 참조하고, 한 변수를 통해 리스트 내용을 변경하면 다른 변수에도 변경사항이 반영된다. 변경사항의 공유

rgb = ["Red", "Green", "Blue"] # Original list
rgba = rgb # Referencing the same object
print(id(rgba) == id(rgb)) # True
rgba.append('Alph')
print(id(rgba) == id(rgb)) # True ( both variables reference the same object)
print(rgb, rgba) # ['Red', 'Green', 'Blue', 'Alph'] ['Red', 'Green', 'Blue', 'Alph']


incorrect_rgba = rgba[:] # Create a new list through 'shallow copy'
print(id(incorrect_rgba) == id(rgba)) # False
incorrect_rgba[-1] = "Alpaca"
print(incorrect_rgba)
print(rgba)

# Assignment to slices is also possible, can change the size of the list or clear it entirely
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(len(letters)) # 7

# replace some values
letters[:3] = ['A', 'B', 'C', 'D']
print(letters)
print(len(letters)) # 8

letters[:4] = [] # remove them
print(letters)
letters[:] = [] # remove entirely
print(letters)


# del keyword can be used to delete almost any object(int, str, lists, attributes of obj)
letters_2 = ['A', 'B', 'C', 'D']
print(letters_2)
del letters_2[:]
print(letters_2)

# Nest lists
a = ['mimi', 'riri']
b = ['11', '12']
x = [a, b]
print(x)
print(x[0][0]) # mimi
print(x[1][1]) # 12

# 3D list
three_d_list = [1, 2, ['a', 'b', ['Life', 'is']]]
print(three_d_list[2][2][0]) # Life

# Slicing a nested list
s_n_list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(s_n_list[2:5]) # [3, ['a', 'b', 'c'], 4]
print(s_n_list[3][:2]) # ['a', 'b']

# sort
num = [1, 4, 3, 2]
# print(num.sort()) # 정렬된 리스트는 반환하지 않음
num.sort()
print(num) # [1, 2, 3, 4]

# revers
num.reverse()
print(num) # [4, 3, 2, 1]

# index
print(num.index(2)) # 2의 위치 반환 output: 2 (= num[2])

# insert
num.insert(0, 2) # insert(a, b) a=index 위치 b=추가할 리스트 요소 혹은 삽입하는 함수
print(num)

def my_function():
    return "Hello"

num.insert(1, my_function) # [2, <function my_function at 0x100392340>, 4, 3, 2, 1]
print(num[1]()) # 해당 인덱스의 함수 호출, output : Hello

# remove
r_num = [1, 2, 3, 1, 2, 3]
r_num.remove(3)
print(r_num) # 첫 번째 3만 제거됨

r_num.remove(3)
print(r_num) # 전부 제거 완료


# pop : 리스트 맨 마지막 요소 리턴하고 리턴된 요소는 삭제
pop_num = [1, 2, 3]
print(pop_num.pop()) # 3
print(pop_num) # [1, 2]

# count
print(pop_num.count(2)) # 1

# extend : 리스트 요소가 개별적으로 추가됨 append와 차이가 있음, append는 하나의 요소로만 추가
# list_3.extend(), list_3 += [4, 5] , list_3 = list_3 + [4, 5] 모두 동일한 표현식
list_3 = [1, 2, 3]
list_3.extend([4, 5])
print(list_3) # [1, 2, 3, 4, 5]
