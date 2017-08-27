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


def min_value_callback(array, cb):
    return cb(min(array))


# // abs is a built in function to get the absolute value of anumber
array1 = [-2, -7, 0, 8]
# print(min_value_callback(array1, abs)) # // => 7

# // example cb
def double(n):
    return n * 2

array2 = [12, 9, 20, 13, 14]
# print(min_value_callback(array2, double)) # => 18

def my_select(arr, cb):
    result = []
    for el in arr:
        if cb(el):
            result.append(el)
    return result

def is_upper(str):
    return str.upper() == str;

def is_even(n):
    return n % 2 == 0;

result1 = my_select(['BOOTCAMP', 'prep', 'iS', 'COOL'], is_upper);
# print(result1) # => [ 'BOOTCAMP', 'COOL' ]

result2 = my_select([1, 2, 4, 7, 8], is_even);
# print(result2) # => [ 2, 4, 8 ]
