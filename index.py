print "Find Characters"
'''
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
'''

def findChar(list, char):
    arr= []
    for element in list:
        if element.find(char) == -1:
            continue
        else:
            arr.append(element)
    print arr
        
# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output: new_list = ['hello','world']

findChar(word_list, char)