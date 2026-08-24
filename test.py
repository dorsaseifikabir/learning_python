""" sum=5
print("the sum is $" , sum , sep = '' )
name = "dorsa"
num = len(name)
print("dorsa" , str(num))
print(name.replace("d", "p"))
print(name) 

num = [1 , 4 , 7 , 3 , 8 , 11]
pokemon = ["snivy" , "fennekin" , "popplio" , "ponyta" , "zacian"]
num.reverse()
print(num) 

poke_types = {'snivy':'grass',
              'fennenin':'fire',
              'popplio':'water',
              'sylveon':'fairy',
              'latias':'dragon'
              }

poke_types['zamazenta'] = 'fighting'

print(poke_types)
print(

)
pokemon = poke_types.get('cyndaquil')
if pokemon:
    print('nice choice!')
else:
    print('that one is not available') 

contacts = {
    'number': 4,
    'students':
    [
        {'name':'dorsa' , 'email':'dorsa@gmail.com'} ,
        {'name':'sadaf' , 'email':'sadaf@gmail.com'} ,
        {'name':'jojo' , 'email':'jojo@gmail.com'} ,
        {'name':'mehrdad' , 'email':'mehrdad@gmail.com'}
    ]
}

for student in contacts['students']:
    print(student['email']) 

def raise_to_power (base_num , pow_num):
    resault = 1
    for index in range(pow_num):
        resault = resault * base_num
    return resault


print(raise_to_power(3 , 0))"""

from student import Student

student1 = Student('Dorsa', 4.2)
print(student1.name, student1.gpa)

fruits = {'apple', 'banana', 'orange'}

print(fruits)

poke_types = {'snivy': 'grass',
              'fennenin': 'fire',
              'popplio': 'water',
              'sylveon': 'fairy',
              'latias': 'dragon'
              }

poke_types['zamazenta'] = 'fighting'

print(poke_types)

# title = 'fennekin:a fire fox pokemon'
# num =
# colon_position = title.index(':')
# pre_colon, post_colon = title[:colon_position], title[colon_position+1:]
# print(pre_colon)
# print(post_colon)
# pre_colon_text, _, post_colon_text = title.partition(":")
# print(pre_colon_text)
# print(post_colon_text)
# post_colon_text_2 = post_colon_text.replace(" ", "7")
# print(post_colon_text_2)
# print("hello")
# print('dorsa\teifi')
# print('dorsa\\teifi')

title = 'menu'.upper()

print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$2".rjust(4))
print("tea".ljust(16, ".") + "$1".rjust(4))
print("cheesecake".ljust(16, ".") + "$5".rjust(4))
