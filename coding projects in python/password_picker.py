import random
import string
from tokenize import Special
from urllib import response

adjective=['sleepy','slow','smelly',
            'wet','fat','red',
            'blue','orange','yellow',
            'green','purple','fluffy']
nouns=['apple','dinosour','ball',
        'toaster','goat','dragon',
        'hammer','duck','panda']

print ('welcome to password picker')

while True:
 adjective = random.choice(adjective)
 noun = random.choice(nouns)
 number = random.randrange(0, 100)
 special_char = random.choice(string.punctuation)

 password = adjective + noun + str(number) + special_char
 print('Your new password is: %s' % password)

 response = input('Would you like another password? Type y or n: ')
 if response == 'n':
     break