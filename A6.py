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

# def passing_students(students):
#
#
# def laligat_array(array):
#
#
# def disemvowel(string):
