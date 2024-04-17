'''# nested list

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])


#list comprehension

square = [x ** 2 for x in range (1,5)]
print(square)

#membership testing

fruits = ["mango", "banana", "kivi","apple"]
print("mango" in fruits) # this is used to check the elements are there or not


# list methods

numbers =[2,4,1,3,6,5,8,7,9,]
append =numbers.append(10) # append is used to add "string" or integer
numbers.sort()
numbers.remove(1)
print(numbers)


# list insert method
#eg-1
fruits = ["apple","mango","grape"]
fruits.insert(2,"orange")
print(fruits)# list_name.insert(index, element) /(this method is used to store the element in specific location)

#eg-2
num = [1,2,3,4,5]
num.insert(3,7) # u see this element(7) is store the index(3) its mean location
print(num)

# list extend

list_1 = [1,2,3,4]
list_2 = [5,6,7,8]

list_1.extend(list_2)
print(list_1) 

#list pop

alpha = ["a","b","c","d"]
poped_element = alpha.pop(2)
print(alpha)
print(poped_element)

# list index

alpha = ["a","b","c","d"]
index = alpha.index("b")
print(index)

# list count

toy = ["ball","bat","video game","car","car","truck","truck","car"]
count = toy.count("car")
print(count)

# list reverse

number = [1,2,3,4,5,6]
number.reverse()
print(number)

# list copying
list_1 = [1,2,3,4,5]
list_3 = list_1
list_3[0] = 8
print(list_3)


# Implementing the bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Sorted array:", numbers)

numbers = [64, 34, 25, 12, 22, 11, 90]
numbers.sort()
print(numbers)'''











