'''
Created on 11 Dec 2015

@author: Harry
'''
#This game will guess a number that you have in your head. Quite crudely
import random
import time

print 'Think of a number between 1 - 100.'

HighLow = [1, 100]
print
    

time.sleep(1)

while True:
    
    number = random.randint(HighLow[0], HighLow[1])
    print
    print 'My guess is: {0} '.format(number)
    print
    question = input('Enter a number, 1(This is my number), 2(My number is higher), 3(My number is lower): ')
    
    if question == 1:
        print 'Number found'
        playagain = raw_input('Want to play again? y/n.')
        while playagain.upper() not in ['Y', 'YES', 'N', 'NO']:
            print 'Invalid input!'
            playagain = raw_input('Want to play again? y/n.')

        if playagain.upper() in ['Y', 'YES']:
            HighLow = [0, 100]
            print 'Think of a number between 1 - 100.'
            print
            time.sleep(1)
        else:
            break
    
    if question == 2:
        
        HighLow[0] = number + 1
        
    if question == 3:
        
        HighLow[1] = number - 1


