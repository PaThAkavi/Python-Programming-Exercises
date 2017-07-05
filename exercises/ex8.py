formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
     "I had this thing.", # the comma is used so as to connect or join the next line with this one
     "That you could type up right.", # this is why we have used the comma here too..
     "But it didn't sing.",
     "So I said goodnight."
)
