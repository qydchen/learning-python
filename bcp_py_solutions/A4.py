def array_builder(count):
    new_array = []
    for k, v in count.iteritems():
        for i in range(0, v):
            new_array.append(k)
    return new_array

# print(array_builder({'cats': 2, 'dogs': 1})) # //=> ['cats', 'cats', 'dogs']
# print(array_builder({})) # //=> []

def longest_word(sentence):
    longest = ''
    for word in sentence.split(" "):
        if len(word) >= len(longest):
            longest = word
    return longest


# print(longest_word('app academy is cool'))# => 'academy'
# print(longest_word('hate having hungry hippos'))# => 'hippos'
# print(longest_word('bootcamp'))# => 'bootcamp'
# print(longest_word(''))# => ''

def least_common_multiple(num1, num2):
    begin = max(num1, num2)
    for i in range(begin, num1 * num2 + 1):
        if ((i % num1 == 0) & (i % num2 == 0)):
            return i

# print(least_common_multiple(2, 3)) #=> 6
# print(least_common_multiple(6, 10)) #=> 30
# print(least_common_multiple(24, 26)) #=> 312

def silly_cipher(sentence, cipher):
    ciphered = ''
    for char in sentence:
        ciphered += cipher.get(char, ".")
    return ciphered

# print(silly_cipher("apple" , { "a" : "c", "p" : "x", "l" : "r", "e" : "o"})) # //=> 'cxxro'
# print(silly_cipher("apple", { "a" : "c", "p" : "x"})) # //=> 'cxx..'
# print(silly_cipher("bootcamp prep?", { "o" : "e", "p" : "q" , "?" : "!"})) # //=> '.ee....q.q..q!'
# print(silly_cipher("twmce", { "m" : "n", "t" : "d", "w" : "a"})) # //=> 'dan..''

# Write a function `hipsterfy(sentence)` that takes takes a string containing
# several words as input. Remove the last vowel from each word. 'y' is not a vowel.
#
# Examples:
def hipped(word):
    reverse = word[::-1]
    for idx, char in enumerate(reverse):
        if char in "aeiou":
            return (reverse[:idx] + reverse[idx + 1:])[::-1]


def hipsterfy(sentence):
    words = sentence.split(" ")
    hipsterfied = []
    for word in words:
        hipsterfied.append(hipped(word))
    return " ".join(hipsterfied)


# print(hipped("anaconda"))
# print(hipped("cheeseburger"))

# print(hipsterfy("proper")) # => "propr"
# print(hipsterfy("proper tonic panther")) # => "propr tonc panthr"
# print(hipsterfy("towel flicker banana")) # => "towl flickr banan"
# print(hipsterfy("runner anaconda")) # => "runnr anacond"
# print(hipsterfy("turtle cheeseburger fries")) # => "turtl cheeseburgr fris"
