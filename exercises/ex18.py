def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("Avaneesh","Pathak")
print_two_again("Avaneesh","Pathak")
print_one("First!")
print_none()

def squirrel(class1, class2):
    print "class1: %r, class2: %r" % (class1, class2)
    def squirrel_two(class1):
        print "class1: %r" % class1

squirrel("Kumar", "Avaneesh")
