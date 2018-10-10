#!usr/bin/python3

'''
Task

You are given a string s. 
Your task is to find out if the string s contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if s has any alphanumeric characters.
Otherwise, print False. 
In the second line, print True if s has any alphabetical characters.
Otherwise, print False. 
In the third line, print True if s has any digits. Otherwise, print False. 
In the fourth line, print True if s has any lowercase characters.
Otherwise, print False. 
In the fifth line, print True if s has any uppercase characters.
Otherwise, print False.
'''

def see_string_methods(s):
    
   for i in range(len(s)):

        if s[i].isalnum():
            
            print(True)
            break
            # Statement only needs to be True once

        elif i + 1 == len(s):
            
            print(False)
            break
            # breaks when the end of the list is reached
    
    for i in range(len(s)):

        if s[i:i+1].isalpha():
            # Checks if the current string and the next one are
            # in alphabetical order.
            
            print(True)
            break

        elif i + 1 == len(s):
            
            print(False)
            break
    
    for i in range(len(s)):

        if s[i].isdigit():
            
            print(True)
            break

        elif i + 1 == len(s):
            
            print(False)
            break
    
    for i in range(len(s)):

        if s[i].islower():
            
            print(True)
            break

        elif i + 1 == len(s):
            
            print(False)
            break
    
    for i in range(len(s)):

        if s[i].isupper():
            
            print(True)
            break

        elif i + 1 == len(s):
            print(False)
            
        elif i == s[-1]:
            print(False)
            break

if __name__ == '__main__':

    string = '''
    #$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo
    ;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3
    L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNN
    NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNK
    KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
    KKKK333333333333333333333333333333333333333333333333333333333333333333333333
    333333333333333333333333300000000000000000000000000000000000000000000000000
    0000000000000000000000000
    '''
    see_string_methods(string)
