from sys import argv

script, filename = argv

txt = open(filename)
print "Here is your file named %r." % filename
print txt.read()
print txt.close()
print "really good things are written in it."


txt = open(filename)
print txt.readline()
print txt.close()
