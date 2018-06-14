# Question 2 -- decodeString(s):
# Given an encoded string, return its corresponding decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
# Note: k is guaranteed to be a positive integer.
# For s = "4[ab]", the output should be decodeString(s) = "abababab"
# For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"

def decodeString(s):
    decoded_string = []
    k = []
    try:
        for value in s:
            if type(int(value)) == int:
                k.append(value)
            else:
                continue
        print(k)
    except ValueError:
        continue
