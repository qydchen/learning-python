def reverse_range(start, end):
    result = []
    for i in range(end - 1, start, -1):
        result.append(i)
    return result

# print(reverse_range(2,7)) # => [6, 5, 4, 3]
# print(reverse_range(4,2)) # => []

def is_prime(num):
    if (num < 2):
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

# print(is_prime(-7)) # => false
# print(is_prime(2)) # => true
# print(is_prime(11)) # => true
# print(is_prime(15)) # => false

def magic_numbers(num):
    result = []
    for i in range(1, num):
        if (((i % 4 == 0) & (i % 6 != 0)) | ((i % 4 != 0) & (i % 6 == 0))):
            result.append(i)
    return result


# print(magic_numbers(20)) # [4, 6, 8, 16, 18]


def first_and_last(arr):
    if (len(arr) % 2 == 0):
        return arr[0] + arr[len(arr) - 1]
    if (len(arr) % 2 != 0):
        return arr[0] - arr[len(arr) - 1]

# print(first_and_last([1, 2, 3, 4])) # => 5
# print(first_and_last([1, 2, 3, 4, 5])) # => -4
# print(first_and_last([12, 5])) # => 17
# print(first_and_last([12])) # => 0
# print(first_and_last([7, 11, 3])) # => 4

def royal_we(sentence):
    dict = { 'I': 'we', 'mine': 'ours', 'my': 'our', 'me': 'us' }
    words = sentence.split(' ')
    result = []
    for i in range(0, len(words)):
        result.append(dict.get(words[i], words[i]))
    return " ".join(result)

# print(royal_we("I want to go to the store")) # "we want to go to the store"
# print(royal_we("This is my house and you will respect me")) # "This is our house and you will respect us"
# print(royal_we("This is mine")) # "This is ours"
# print(royal_we("Jump for my love")) # "Jump for our love"
