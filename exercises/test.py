from sys import argv

script, filename = argv
txt = open(filename)
print "The file which you want is %r. Am I right?" % filename
ans = raw_input('-->')
print "So! here it is:"
print open(filename).read()
txt.close()
