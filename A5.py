# Write a function highestScore(students) that takes in an array of student objects
# as a parameter. It should return a string that corresponds to the student with
# the highest score. The string should contain that student's initials
# concatenated with their id. Assume the array contains at least 1 student object and
# the student with the highest score is unique (there are no ties).
# Example:

def highest_score(students):
    best_score = None
    for student in students:
        if ((best_score is None) | (best_score < student['score'])):
            best_score = student['score']
            best_student = get_initials(student['name']) + str(student['id'])
    return best_student

def get_initials(name):
    names = name.split(" ")
    first_initial = names[0][0]
    last_initial = names[1][0]
    return first_initial + last_initial

students = [
 {"name": 'Alvin Zablan', "id": 128, "score": -42},
 {"name": 'Eliot Bradshaw', "id": 32, "score": 57},
 {"name": 'Tommy Duek', "id": 2, "score": 99},
 {"name": 'Fred Sladkey', "id": 256, "score": 94}
];

# print(highest_score(students)) #//=> 'TD2'

# Write a function snakeToCamel(str) that takes in a snake_cased string and returns
# the string CamelCased. snake_case is a string where each word is separated with
# underscores (_). CamelCase is a string where the first char of each word
# is capitalized, all other characters lowercase.
#
# Examples:

def snake_to_camel(str):
    camel = ''
    words = str.split("_")
    for word in words:
        camel += word[0].upper() + word[1:].lower()
    return camel

# print(snake_to_camel('snakes_go_hiss')) # // => 'SnakesGoHiss'
# print(snake_to_camel('say_hello_world')) # // => 'SayHelloWorld'
# print(snake_to_camel('bootcamp_prep_is_cool')) # // => 'BootcampPrepIsCool'
# print(snake_to_camel('BOOtcamp_PREP_iS_cOol')) # // => 'BootcampPrepIsCool'

# Write a function sum2Darray(array) that takes in a 2-Dimensional array of numbers.
# The function should return the total sum of all numbers in the 2D array.
#
# Examples:

def sum_2d_array(arr):
    sum = 0
    for subarr in arr:
        sum += reduce(lambda x, y: x + y, subarr)
    return sum


arr1 = [
  [1,2,3],
  [4,5],
  [6],
];
# print(sum_2d_array(arr1)) # => 21

arr2 = [
  [-10, 2, 3],
  [1],
  [10, -5],
  [2]
];
# print(sum_2d_array(arr2)) # => 3

# Write a funtion minValueCallback(array, cb) that takes in an array of numbers and
# a callback. The function should call `cb`, passing in the minimum number of the array.
# `minValueCallback` should return the return value of `cb`. If the array is empty,
# then pass `null` into `cb`.
#
# Examples:

# def min_value_callback(array, cb):

# // Math.abs is a built in function to get the absolute value of anumber
# array1 = [-2, -7, 0, 8];
# minValueCallback(array1, Math.abs); // => 7

# // example cb
# def double(n):
#     return n * 2
#
# array2 = [12, 9, 20, 13, 14];
# print(min_value_callback(array2, double)) # => 18

# Write a function mySelect(arr, cb) that accepts an array and a callback.
# It should pass the callback every element, its corresponding index, and the array
# itself. Returns an array containing all elements of `arr` for which the given callback
# returns a truthy value.
#
# Examples:

# def my_select(arr, cb):
#
# def is_upper(str):
#     return str.upper() === str;
#
# def is_even(n):
#     return n % 2 === 0;
#
# result1 = my_select(['BOOTCAMP', 'prep', 'iS', 'COOL'], is_upper);
# result1 # => [ 'BOOTCAMP', 'COOL' ]
#
# result2 = my_select([1, 2, 4, 7, 8], is_even);
# result2 # => [ 2, 4, 8 ]
