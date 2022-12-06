def absolute_value(num):
    if num > 0:
        return num
    elif num == 0:
        return "Zero is zero."
    else:
        return -num
print(absolute_value(0))

def max_length():
    l = []
    k = []
    for i in range(4):
        word = input(" please enter a word: ")
        l.append(len(word))
        k.append(word)
    return (f"{k[l.index(max(l))]} word is a longer word : {max(l)}")

print(max_length())