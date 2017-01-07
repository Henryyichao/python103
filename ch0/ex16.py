from sys import argv
# This variable holds the arguments you pass to your Python script when you run it. 
#之前对于python里的argument variable一直缺乏理解，可以暂且记为变量存储器。那么script放在里面是什么意思呢？
#argv作为一个变量，是list类型的。其含有两个元素（都是字符串），第一个元素是“test2.py”即所执行的python脚本的名字；第二个元素才是我们想要的“第一个”命令行参数。

script,filename = argv

print ("We're going to erase %r."% filename)
print ("If you don't want that,hit CTRL-C（^C）.")
print ("If you do want that,hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print ("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally,we close it.")
target.close()