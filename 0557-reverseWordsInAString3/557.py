string = "Let's take LeetCode contest"



def reverseWords(string):
    s = list(string)
    i = 0
    j = 0
    endl = len(s)
    while i < endl:
        while j < endl and s[j] != " " :
            j += 1
        j -= 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        while i < endl and s[i] != " ":
            i += 1
        i += 1
        while j < endl and s[j] != " ":
            j += 1
        j += 1
    return "".join(s)

        
print(reverseWords(string))