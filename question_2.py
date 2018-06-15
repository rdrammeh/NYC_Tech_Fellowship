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
    coded_list = [value for value in s]
    print(coded_list)

    while i < len(coded_list):
        if current_list[i] in '0123456789':
            k = int(current_list[i])
            if current_list[i + 1]



    # current_list = coded_list
    # i = 0
    # x = 1
    # repeat = ""
    # decoded = ""
    #
    # while i < len(coded_list):
    #
    #         k = int(current_list[i])
    #         repeat += ''.join(current_list[i + 1:])
    #         new = k * repeat
    #         current_list = []
    #         current_list += new
    #         break
    #     else:
    #         i += 1
    # print(current_list)

    #decodeString(current_list)



#Runner Code
#decodeString('4[ab]')
decodeString('2[b3[a]]')
