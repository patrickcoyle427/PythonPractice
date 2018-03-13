'''
awfuldict.py - an implementaion of dictionaries that uses tuples
               instead of making actual dictionaries

'''

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.mydict = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.mydict.append((k, v))
        
    def getval(self, k):
        """ k, immutable object  """
        matches = []
        del matches[:]
        
        for keyval in self.mydict:
            if k == keyval[0]:
                matches.append(keyval)
                
        if matches == []:
            raise KeyError('No Key Found to Return')
                
        else:
            return matches[-1][1]
        
    def delete(self, k):
        """ k, immutable object """
        matches = []
        del matches[:]
        
        for keyval in self.mydict:
            if k == keyval[0]:
                matches.append(keyval)
        if matches == []:
            raise KeyError('Key not found. Nothing deleted.')

        else:
            toDelete = matches[-1]
            toDeleteIndex = self.mydict.index(toDelete)
            del self.mydict[toDeleteIndex]

