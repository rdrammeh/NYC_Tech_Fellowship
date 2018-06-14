# Question 2 -- decodeString(s):
# Given an encoded string, return its corresponding decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
# Note: k is guaranteed to be a positive integer.
# For s = "4[ab]", the output should be decodeString(s) = "abababab"
# For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"

def decodeString(s):
    coded_string = []
    for value in s:
        coded_string.append(value)

    k = int(coded_string[0])
    coded_string.remove(coded_string[0])
    new_string = k * coded_string
    decoded_string = [l for l in new_string if l == '[' or l == ']' new_string.remove(l)]
    print(decoded_string)


#Runner Code
decodeString('4[ab]')
#decodeString('2[b3[a]]')
