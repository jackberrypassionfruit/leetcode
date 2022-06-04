s = ["s", "a", "u", "c", "e"]

def reverseString(string):
    for i in range(len(string) // 2):
        string[i], string[-i - 1] = string[-i - 1], string[i]

reverseString(s)

print(s)