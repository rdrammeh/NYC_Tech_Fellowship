# Question 1 -- sortByStrings(s,t):
# Sort the letters in the string s by the order they occur in the string t.
# You can assume t will not have repetitive characters.
# For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw".
# For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".

def sortByStrings(s, t):
    sorted = []
    for t_letter in t:
        for s_letter in s:
            if s_letter == t_letter:
                sorted.append(s_letter)
            else:
                continue
    print(*sorted)

sortByStrings('weather', 'therapyw')
sortByStrings('good', 'odg')
