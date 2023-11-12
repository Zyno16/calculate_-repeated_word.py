counts = dict()
line = input("enter the text")
words = line.split()
print("the words is ",words)
print("counting")

for word in words:
    counts[word]=counts.get(word,0) + 1
print("counts",counts)