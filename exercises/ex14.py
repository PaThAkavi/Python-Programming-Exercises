from sys import argv

script, user_name = argv

print "Hi %s, I'm %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input()

print "Where do you live %s?" % user_name
lives = raw_input()

print "What kind of computer do you have %s?" % user_name
computer = raw_input()

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer, nice.
""" % (likes, lives, computer)
