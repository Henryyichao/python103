my_name = 'Henry hou'
my_age = 24 # not a lie
my_height = 1.78 # cm
my_weight = 65 # lbs
my_eyes = 'brown'
my_teeth = 'White'
my_hair = 'black'

print "Let's talk about %s." % my_name
print "Let's talk ablut %s." % my_name
print "He's %d inches tall." % (my_height*3.28)
print "He's %d pounds heavy." % (my_weight*2.2)
print "he's %r name is wonderful" % my_name 
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)