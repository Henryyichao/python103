#add features to my script from feature set(moudule)
from sys import argv
#gagv is the "argument variable"
script, filename =argv
#unpack
txt = open(filename)
#new command
print "Here's your file %r:" %filename
print txt.readline(1)

print "Type the filename again:"
file_again = raw_input(">")
#prompt
txt_again = open(file_again)

print txt_again.read()