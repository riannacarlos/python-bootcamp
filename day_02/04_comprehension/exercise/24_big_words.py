# You can use a custom message using input()
sentence = "I like big data and AI models"

# TODO: Find all the words with len > 3
words = sentence.split()
big_words = [sentence for word in words if len > 3]

print(big_words)
