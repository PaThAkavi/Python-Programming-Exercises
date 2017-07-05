from sys import argv

script, user_name, father = argv
prompt = "$"

print "Hello, I'm %s script." % script

print "What is your name?"
name = raw_input(prompt)

print "Oh! It is a really very good name %s." % user_name

print "Can you tell me your age %s?" % user_name
age = raw_input(prompt)

print "Oh! I think you are just going to join the first year college, HUH?"
ans = raw_input(prompt)

print "Are you the son of %s?" % father
jawab = raw_input(prompt)

print "I know everything, %s!!" % user_name

print """
I know a lot of things about you %r and.
your family cuz I'm an ISI agent.
HE.HE.HA.HA.HA.HA.HA.HA.....
""" % user_name
