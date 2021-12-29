# Printing lengthiest string in a list in descending order
# List of words with highest length
s = input("Enter the sentence:")
words = s.split()
d = {}
for w in words:
    if w not in d:
        d[w] = len(w)
print(d)
x = []
for k, v in d.items():
    x.append((v, k))
x.sort(reverse=True)
print(x)
# print("Printing top 10 longest words in a list in descending order : ")
# print(x[0:10])