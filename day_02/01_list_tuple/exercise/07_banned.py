banned_words = ("moist", "break", "raise")

# TODO: Ask the user for a word
# TODO: If the word is in banned_words, say "Banned"
var=input()
print("Given Word:",var)
has_banned= var in banned_words
print("Banned")
if var not in banned_words:
    print("Not Banned")
