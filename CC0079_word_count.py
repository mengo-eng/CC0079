
# Assignment - 007/9 (Letters Count) - Count the number of each letter in a sentence.
# C7185-Elnur
word = "hippo runs to us!"
pairs = {}
[pairs.update({i: list(word).count(i)}) for i in list(word)]
print(pairs)