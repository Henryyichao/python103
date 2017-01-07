from sys import argv
#注意运行的时候要代入变量
script,user_name = argv
promt = '>'

print ("Hi %s,I'm the %s script." %(user_name,script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" %user_name)
likes = input()

print ("where do you live %s?" %user_name)
lives = input()

print ("what kind of computer do you have? %s" %user_name)
computer = input()
#由于python3取消了raw_input ，所以原先括号里的prompt也可以省掉了
print ('''
Alright,so you said %r about liking me.
You live in %r.Not sure is there have smog or not.
And you have a %r computer. NIce.
'''%(likes,lives,computer))