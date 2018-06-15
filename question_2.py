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



# def decodeString(s):
#     coded_list = [l for l in s]
#
#     coded_list
#     i = 0
#     x = 1
#     multipler = ""
#
#     while i < len(coded_list):
#         if coded_list[i] in '0123456789':
#             k = int(coded_list[i])
#             if coded_list[x] == '[':
#                 coded_list.remove(coded_list[x])
#                 while x < len(coded_list):
#                     if coded_list[x] != ']':
#                         multipler += coded_list[x]
#                         x += 1
#                     else:
#                         multipler += coded_list[x]
#                         break
#             new_string = k * multipler
#             print(type(new_string))
#         break
#
#     if additional_numbers(new_string):
#         decodeString(new_string)
#     else:
#
#     new_list = [l for l in new_string]
#     z = 0
#
#     while z < len(new_list):
#         if new_list[z] in '0123456789':
#             decodeString(new_string)
#     else:
#         decode = [l for l in new_string if l != '[' and l != ']']
#         print(''.join(decode))


def additional_numbers(l):
    new_list = [a for a in l]
    z = 0

    while z < len(new_list):
        if new_list[z] in '0123456789':
            return True
            break
        else:
            z += 1
    return False


#Runner Code
# decodeString('4[ab]')
# decodeString('2[b3[a]]')
print(additional_numbers('4[ab]'))
print(additional_numbers('2[b3[a]]'))
print(additional_numbers('[b[a]]'))
