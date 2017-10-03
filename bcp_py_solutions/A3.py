def my_index_of(arr, ele):
    for i in range(0, len(arr)):
        if ele == arr[i]:
            return i
    return -1

# print(my_index_of([1,2,3,4,5], 5)) # 4
# print(my_index_of(["a", "b", "c"], "a")) # 0
# print(my_index_of(["a", "b", "c"], "d")) # -1

def min_max_difference(arr):
    return max(arr) - min(arr)

# print(min_max_difference([1,2,3,4,5])) #=> 4
# print(min_max_difference([5,4,3,2,1])) #=> 4
# print(min_max_difference([4,2,5,1,-5]))# => 10

def divisible_by_five_pair_sum(array):
    pairs = []
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if ((array[i] + array[j]) % 5 == 0):
                pairs.append([i,j])
    return pairs

# print(divisible_by_five_pair_sum([1, 5, 2, 0, 4]))# // => [ [ 0, 4 ], [ 1, 3 ] ]
# print(divisible_by_five_pair_sum([13, 22, 8, -3, 12]))# // => [[ 0, 1 ], [ 0, 3 ], [ 0, 4 ], [ 1, 2 ], [ 2, 3 ], [ 2, 4 ]]

def dynamic_fizz_buzz(max, num1, num2):
    result = []
    for i in range(1, max):
        if (((i % num1 == 0) & (i % num2 != 0)) | ((i % num1 != 0) & (i % num2 == 0))):
            result.append(i)
    return result

# print(dynamic_fizz_buzz(20, 5, 3)) # => [3, 5, 6, 9, 10, 12, 18]
# print(dynamic_fizz_buzz(20, 4, 6)) # => [4, 6, 8, 16, 18]

def magic_cipher(sentence, cipher):
    ciphered = ''
    for i in range(0, len(sentence)):
        ciphered += cipher.get(sentence[i], sentence[i])
    return ciphered

# print(magic_cipher("add me on facebook" , { "a" : "c", "d" : "q"})) # => "cqq me on fccebook"
# print(magic_cipher("where are you?" , { "v" : "l", '?' : "!"})) # => "where are you!"
# print(magic_cipher("twmce" , { "m" : "n", "t" : "d", "w" : "a"})) # => "dance"
