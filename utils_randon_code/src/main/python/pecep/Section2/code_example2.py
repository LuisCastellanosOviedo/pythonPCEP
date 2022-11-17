####################################################################
#list 

my_list = [1,2,3,4]
print(my_list)
print(type(my_list))

print(my_list.pop())
print(my_list)

print(my_list.pop(0))
print(my_list)

my_list = [1,2,3,4]
my_list[0]='S'
print(my_list)

my_list[1]=['is a ','list']
print(my_list)

my_list.append('this is a sentence')
print(my_list)


my_list = [3,2,7,5,9,7,4,7,]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list[2:])


length = len(my_list)
print(length)

string_text = 'fkjdqwfjqw'
print(len(string_text))

second_list = ['a','b','c']
print(my_list+second_list)

my_list = ['a','b','c',['apple','banana']]
print(my_list[3][1])
           