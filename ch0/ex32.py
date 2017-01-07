the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'peenies',2,'dimes',3,'quarters']

for number in the_count:
    print ("This is count %d" % number)
	
for fruit in fruits:
    print("A fruit of type: %s " %fruit)
	
for i in change:
    print ("I got %r" %i)
	
elements = []

#使用范围函数计数
for i in range(0,6):
	print("Adding %d to the list."%i)		
	elements.append(i)
	#加尾巴函数
for i in elements:
    print("ELement was :%d" %i)

print(range(3))
print(type(range(3)))
print(list(range(3)))
#需要注意的是，在python3里，range函数所返回的是可迭代对象，而不是列表。