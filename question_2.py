# Question 2 -- decodeString(s):
# Given an encoded string, return its corresponding decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times.
# Note: k is guaranteed to be a positive integer.
# For s = "4[ab]", the output should be decodeString(s) = "abababab"
# For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"

def decodeString(s):
    coded_list = [l for l in s]
    decode = ""
    factor = ""
    remainder_string = ""

    for i in range(len(coded_list)):
        if coded_list[i] in '0123456789':
            k = int(coded_list[i])
            if coded_list[i + 1] == '[':
                coded_list.remove(coded_list[i])
                for num in range(len(coded_list[i + 1:])):
                    if coded_list[num + 1] != ']':
                        factor += coded_list[num + 1]
                    else:
                        factor += coded_list[num + 1]
                        remainder_string += ''.join(coded_list[num + 1:])
                        break
                decode += k * factor
                decode += remainder_string
            break
        else:
            decode += coded_list[i]
            continue

    moreNumbers = False

    for letter in decode:
        if letter in '0123456789':
            moreNumbers = True

    if moreNumbers:
        return decodeString(decode)
    else:
        answer = [l for l in decode if l != '[' and l != ']']
        print(''.join(answer))




#Runner Code
decodeString('2[b3[a]]')
decodeString('4[ab]')
