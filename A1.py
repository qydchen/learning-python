
def py_range(start, end):
    nums = []
    for x in range(start, end):
        nums.append(x)
    return nums

# print(pyRange(1,4))
# print(pyRange(4,2))

def reverse_sentence(sentence):
    result = []
    words = sentence.split(" ")
    for ele in reversed(words):
        result.append(ele)
    return " ".join(result)

# print(reverseSentence("Go to the store")) # => "store the to Go"
# print(reverseSentence("Jump, jump for joy")) # => "joy for jump Jump,"

def unique(arr):
    result = []
    for ele in arr:
        if ele not in result:
            result.append(ele)
    return result


# print(unique([1, 1, 2, 3, 3])) # => [1, 2, 3]


def fizzbuzz(max):
    result = []
    for i in range(1, max):
        if (((i % 3 == 0) & (i % 5 != 0)) | ((i % 3 != 0) & (i % 5 == 0))):
            result.append(i)
    return result

# print(fizzbuzz(20))

def string_range(start, end, step):
    string = ''
    for i in range(start, end + 1, step):
        string += str(i)
    return string

# print(string_range(0, 12, 2)) # => '024681012'
# print(string_range(3, 20, 5)) # => '381318'
