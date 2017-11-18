print "Welcome to the PIG LATIN CONVERTER"

a = raw_input("Enter a word: ")
if len(a) > 0 and a.isalpha():
    print a

else:
    print "empty"
suff = "ay"
word = a.lower()
first = word[0]
new_word = word + first + suff
print new_word
