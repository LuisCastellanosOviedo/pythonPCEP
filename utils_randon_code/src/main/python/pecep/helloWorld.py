print('hello')


number = 4344
print(number)

weight = 323

answer = number + weight
print(answer)

name = 'luis'
last_name= 'alejandro'
age = 99

# ojo , hay que castear a str !!!! 
sentence = name + str(age) + last_name

print(sentence)

####################################################################

data_type = type(12)

print(data_type)

float_type = type(12.03)
print(float_type)

#boolean
adult = True
print(type(adult))

####################################################################
# arimethic 

num1 = 3
num2 = 10 

answer = num1 + num2
mod = num1 % num2

print(answer)
print(mod)
####################################################################
# index and slicing 

sentence2 = "I'm coming home"
print(sentence2)

sentence2 = "I'm coming \n home"
print(sentence2)

sentence2 = 'this is a sentence'

print(sentence2[0])
print(sentence2[-1])
print(sentence2[0:4])
print(sentence2[0:])
print(sentence2[5:7])

sentence2='abcdeftre'
print(sentence2[0:7:2])

####################################################################
#string methods

sentence = 'this is a test'

print(sentence.upper())
print((sentence.upper()).lower())

number_value='34343'
print(number_value.isdigit())

print(sentence2.startswith('ab'))
print(sentence2.startswith('is',5))

print(sentence2.endswith('test'))








