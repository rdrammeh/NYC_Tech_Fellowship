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
    coded_list = [value for value in s if value != '[' and value != ']']


    current_list = coded_list
    i = 0

    # for value in reversed(current_list):
    #     if value in '0123456789':
    #         k = int(value)
    #         current_index = current_list.index(value)
    #         word = k * current_list[current_index:]
    #         print(''.join(word))
    #     else:
    #         pass


    while i < len(coded_list):
        print("The current string is ", ''.join(current_list))
        if current_list[i] in '0123456789':
            k = int(current_list[i])
            if current_list[i + 1] == '[':
                decoded_list = k * current_list[i + 1:]
                current_list = []
                current_list += decoded_list
                i += 1
            else:
                i += 1
        else:
            i += 1


#Runner Code
#decodeString('4[ab]')
decodeString('2[b3[a]]')
