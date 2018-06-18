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
    decode = ""
    factor = ""
    remainder_string = ""
    decoded_string = ""
    loop = 0
    for i in range(len(coded_list)):
        if coded_list[i] in '0123456789':
            k = int(coded_list[i])
            print("k is ", k)
            if coded_list[i + 1] == '[':
                print("Index of ", coded_list[i],  coded_list.index(coded_list[i]))
                print(" after 'k' is ", coded_list[i + 1])
                coded_list.remove(coded_list[i])
                for x in range(len(coded_list)):
                    if coded_list[x + 1] != ']':
                        factor += coded_list[x + 1]
                    else:
                        factor += coded_list[x + 1]
                        remainder_string += ''.join(coded_list[i + 2:])
                        print("coded_list[x + 1:] is ", coded_list[x + 2:])
                        print("remainder string is now ", remainder_string)
                        break
                decoded_string += decode.replace('[', "")
                print("decode is ", decoded_string)
                print("factor is ", factor)
                product = k * factor
                print("product is ", product)
                decoded_string += k * factor
                decoded_string += remainder_string
                print("The new coded list is", decoded_string)
                loop += 1
            break
        else:
            decoded_string += coded_list[i]

    moreNumbers = False

    for letter in decoded_string:
        if letter in '0123456789':
            moreNumbers = True

    if moreNumbers:
        return decodeString(decoded_string)
        print(" we're getting here!")
    else:
        answer = [l for l in decoded_string if l != '[' and l != ']']
        print(''.join(answer))
        print("we looped ", loop)


# def decoderLoop(a):
#     coded_list = [l for l in a]
#
#     i = 0
#     x = 1
#     multipler = ""
#     decode = ""
#     new_string = ""
#
#     while i < len(coded_list):
#         if coded_list[i] in '0123456789':
#             k = int(coded_list[i])
#             if coded_list[i + 1] == '[':
#                 coded_list.remove(coded_list[x])
#                 while x < len(coded_list):
#                     if coded_list[x] != ']':
#                         multipler += coded_list[x]
#                         x += 1
#                     else:
#                         multipler += coded_list[x]
#                         leftover = ''.join(coded_list[x + 1:])
#                         break
#                 new_string = k * multipler
#                 decode += k * multipler
#                 decode += leftover
#                 return decode
#             break
#         else:
#             decode += coded_list[i]
#             i += 1
#
#
#
#
#
#
#
#
# def decodeString(s):
#     if moreNumbers(s):
#         print("HIT more number true")
#         return decoderLoop(s)
#     else:
#         print("NOT hit more number true")
#         decode_string = [l for l in s if l != '[' and l != ']']
#         print("Decoded words is ", ''.join(decode_string))
#     # coded = decodeLoop(s)
#     # print(type(coded))
#     # print("Run decode loop and return is ", coded)
#     # if moreNumbers(coded):
#     #     print("Yes there are more numbers...")
#     #     again = decodeLoop("b3[a]b3[a]")
#     #     print(again)
#     #     #decodeString(again)
#     # else:
#     #     print("No more numbers")
#     #     decode = [l for l in coded if l != '[' and l != ']']
#     #     print("Decoded words is ", ''.join(decode))
#
#
# def moreNumbers(l):
#     new_list = [a for a in l]
#     z = 0
#
#     while z < len(new_list):
#         if new_list[z] in '0123456789':
#             return True
#             break
#         else:
#             z += 1
#     return False


#Runner Code
decodeString('2[b3[a]]')
# decodeString('4[ab]')
# print(additional_numbers('4[ab]'))
# print(additional_numbers('2[b3[a]]'))
# print(additional_numbers('[b[a]]'))
