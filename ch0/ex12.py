
#在Python 3.2.3中  input和raw_input 整合了，没有了raw_input
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")
#python2.7 的话，print是一个表达式，要写 print i
#而在python3 的话，print是一个函数，所以要写 print(i)
print ("so you are %r old ,%r tall and %r heavy." %(age,height,weight))
#而且也影响到了赋值的过程，原本两个并列的括号结构变成包含的括号结构。