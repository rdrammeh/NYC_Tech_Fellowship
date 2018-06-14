# Question 2 -- decodeString(s):
# Given an encoded string, return its corresponding decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
# Note: k is guaranteed to be a positive integer.
# For s = "4[ab]", the output should be decodeString(s) = "abababab"
# For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"


#Successful run for decodeString('4[ab]'). Will you this as guide for the second runner code
# def decodeString(s):
#     coded_string = []
#     for value in s:
#         coded_string.append(value)
#
#     k = int(coded_string[0])
#     coded_string.remove(coded_string[0])
#     coded_string *= k
#     decoded_string = [l for l in coded_string if l != '[' and l != ']']
#     print(''.join(decoded_string))


def decodeString(s):
    coded_string = []
    for value in s:
        coded_string.append(value)

    decoded = []
    try:
        for i in range(0, len(coded_string)):
            if type(int(coded_string[i])) == int:
                k = int(coded_string[i])
                if coded_string[i + 1] == '[':
                    decoded.append(k * coded_string[i + 1:])
                else:
                    continue
            else:
                continue
    except ValueError:
        pass

    print(decoded)



#Runner Code
#decodeString('4[ab]')
decodeString('2[b3[a]]')
