# To get max word length in a string

s = input("Enter a sentence:")
words = s.split()
maxlen = 0
maxw = None
for w in words:
    if len(w) > maxlen:
        maxlen = len(w)
        maxw = w
print("The longest word is", maxw, "and it has", maxlen, "letters.")