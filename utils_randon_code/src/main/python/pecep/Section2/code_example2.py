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

my_list [1] = 'zzzzzz'

print(my_list)

my_list = ['a','b','c',['apple','banana'],'c','c']

index_pos = my_list.index('c')
print(index_pos)

c_count = my_list.count('c')
print(c_count)

####################################################################
#tuples = inmutable 

my_tuple = (1,2,3,"some date",[1,2,3])

print(my_tuple[4])
print(my_tuple.count("some date"))
print(my_tuple[:3])
print(my_tuple[3:])


####################################################################
#Dictionaries

dict = {'k1':'some data',7:'other data'}

print(dict['k1'])
print(dict[7])
dict[7] = 'DATA CHANGED'
print(dict)

peolple_weight_dict = {'john':134,'mike':170,'robert':165}
print(peolple_weight_dict)
peolple_weight_dict['john']= 19
print(peolple_weight_dict)

print(peolple_weight_dict.pop('mike'))
print(peolple_weight_dict)

peolple_weight_dict.clear()
print(peolple_weight_dict)

peolple_weight_dict['99'] = '99 new data'
print(peolple_weight_dict)
           
peolple_weight_dict = {'john':134,'mike':170,'robert':165,'items':['banana','orange',{'banana2':'banana2 value','lemon':'lemnon value'}]}
print(peolple_weight_dict['items'][1])
print(peolple_weight_dict['items'][2]['banana2'])
print(peolple_weight_dict['items'][2]['lemon'])