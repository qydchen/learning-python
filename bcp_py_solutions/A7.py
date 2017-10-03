def number_primes(n):
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return len(result)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# print(number_primes(10)) # => 4
# print(number_primes(12)) # => 5
# print(number_primes(20)) # => 8
# print(number_primes(100)) # => 25

def longest_bigram(sentence):
    longest = ''
    words = sentence.split(' ')
    for idx, word in enumerate(words[0:-1]):
        bigram = '{0} {1}'.format(word, words[idx + 1])
        if len(longest) < len(bigram):
            longest = bigram
    return longest

# print(longest_bigram('measure twice cut once')) # => 'measure twice'
# print(longest_bigram("One must have a mind of winter")) # => 'must have'
# print(longest_bigram("go home to eat")) # => 'go home'
# print(longest_bigram("his last assessment is fun")) # => 'last assessment'

def longest_letter_streak(str, search_letters):
    longest_streak = 0
    current_streak = 0
    for (idx, char) in enumerate(str):
        if char in search_letters:
            current_streak += 1
            if current_streak > longest_streak:
                longest_streak = current_streak
        else:
            current_streak = 0
    return longest_streak

# print(longest_letter_streak("ACCA", ["C"])); # => 2
# print(longest_letter_streak("YACCADCA", ["C", "A"])); # => 4
# print(longest_letter_streak("ZTKZQRKKZ", ["Z", "K", "Y"])); # => 3
# print(longest_letter_streak("YYYYY", ["Z", "K", "Y"])); # => 5

def previous_prime_array(array):
    result = []
    for num in array:
        if is_prime(num):
            previous_prime = get_previous_prime(num)
            result.append(previous_prime)
        else:
            result.append(num)
    return result

def get_previous_prime(num):
    for i in reversed(range(2, num)):
        if is_prime(i):
            return i

# print(previous_prime_array([10, 12, 11, 7, 16])); # => [ 10, 12, 7, 5, 16 ]
# print(previous_prime_array([17, 24, 29, 5, 2, 4])); # => [ 13, 24, 23, 3, null, 4 ]
