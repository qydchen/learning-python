def my_map(arr, cb):
    result = []
    for idx, el in enumerate(arr):
        new_el = cb(el, idx)
        result.append(new_el)
    return result

def multiply(num1, num2):
    return num1 * num2;

# print(my_map([2, 4, 6, 6], multiply)) # => [ 0, 4, 12, 18 ]

def is_palindrome(sentence):
    i = 0
    while i < len(sentence)/2:
        if sentence[i] != sentence[-i - 1]:
            return False
        i += 1
    return True

# print(is_palindrome('racecar'))

def passing_students(students):
    passers = []
    for student in students:
        if get_avg(student['grades']) >= 70:
            passers.append(student['name'])
    return passers

def get_avg(grades):
    total = 0
    for grade in grades:
        total += grade['score']
    return total/len(grades)

students = [
  {
    "name": "Kush",
    "id": 12345,
    "grades": [{"id": 0, "score": 65}, {"id": 1, "score": 75}, {"id": 2, "score": 85}]
  },
  {
    "name": "Ned",
    "id": 55555,
    "grades": [{"id": 0, "score": 100}, {"id": 1, "score": 100}, {"id": 2, "score": 100}]
  },
  {
    "name": "Haseeb",
    "id": 94110,
    "grades": [{"id": 0, "score": 65}, {"id": 1, "score": 60}, {"id": 2, "score": 65}]
  }
]

# print(passing_students(students)) # => [ 'Kush', 'Ned' ]

def laligat_array(array):
    return list(map(lambda num: laligat_sum(num), array))

def laligat_sum(num):
    total = 0
    for i in range(2, num + 1):
        if is_prime(i):
            total += i
    return total

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))

# print(laligat_array([10, 11, 20, 15])); # => [ 17, 28, 77, 41 ]
# print(laligat_array([1, 2, 3, 4, 5])); # => [ 0, 2, 5, 5, 10 ]

def disemvowel(string):
    result = ''
    for char in string:
        if char.lower() not in 'aeiou':
            result += char
        return result

# print(disemvowel('bootcamp')); # => 'btcmp'
# print(disemvowel('PREP')); # => 'PRP'
# print(disemvowel('hello world')); # => 'hll wrld'
