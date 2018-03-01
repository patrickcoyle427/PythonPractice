#!/usr/bin/python3

'''
Takes a list containing lists/tuples and creates a new list that contains no lists/tuples, but with the values of those lists/tuples intact.
'''

def listFlattener(L):
    
  flattenedList = []
    
  tempList = []
  
  for i in L:
        
    if type(i) is list or type(i) is tuple:
        
      tempList = listFlattener(i)
      #Recursive call to listFlattener. Keeps getting called as long
      #As the for loops keeps finding a list/tuple
        
      for j in tempList:
            
        flattenedList.append(j)
        #Once no more lists are found, any data is appened to
        #flattenedList to be returned.
      
    else:.
        
      flattenedList.append(i)
      #Needed in case i isn't a list/tuple
        
  return flattenedList

if '__name__' == '__main__':
    
    L = [1, [[2]], (3,), [4,5], [[6, [7]]]]
    
    print(listFlattener(L))