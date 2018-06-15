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
    coded_list = [l for l in s]

    coded_list
    i = 0
    x = 1
    multipler = ""

    while i < len(coded_list):
        if coded_list[i] in '0123456789':
            k = int(coded_list[i])
            if coded_list[x] == '[':
                coded_list.remove(coded_list[x])
                while x < len(coded_list):
                    if coded_list[x] != ']':
                        multipler += coded_list[x]
                        x += 1
                    else:
                        multipler += coded_list[x]
                        break
            new_list = k * multipler
            print(new_list)
            # if new_list in '0123456789':
            #     decodeString(new_list)
            # else:
            #     decode = [l for l in new_list if l != '[' and l != ']']
            #     print(''.join(decode))
        i += 1



#Runner Code
#decodeString('4[ab]')
decodeString('2[b3[a]]')
