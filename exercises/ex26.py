from sys import argv

print "How old are you?"
age =  raw_input()
print "How tall are you?"
height =  raw_input()
print "How much do you weigh?"
weight =  raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print(txt.read())

print "Type the filename again:"
file_again = raw_input("->")

txt_again = open(file_again)

print(txt_again.read())


print "Let's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %r" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print "With a starting point of: {}".format(start_point)
# it's just like with an f"" string
print "We'd have %r beans, %r jars, and %r crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print "We'd have {} beans, {} jars, and {} crates.".format(*formula)

people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "people are dogs."
    
