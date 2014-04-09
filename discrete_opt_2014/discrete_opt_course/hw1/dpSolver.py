'''
Created on Mar 10, 2014

@author: Domingo
'''

class MyClass(object):
    '''
    classdocs
    '''



    def __init__(self):
        '''
        Constructor
        '''  
    
    def solveIt(self, capacity, items):
        
        self.weightTaken = 0
        self.itemsToPic = items
        
        output = ""
        return output
    
    def getComputeVal(self, maxCap , indexOfItemsToSelect):
        if indexOfItemsToSelect == 0:
            return 0
        else:
            itemToSelect = self.itemsToPic[indexOfItemsToSelect]
            weightOfExtraItem = itemToSelect.weight
            
        #    if w <= maxCap:
        #        return max( self.getComputeVal(maxCap, indexOfItemsToSelect-1) , v + self.getComputeVal(maxCap-w, indexOfItemsToSelect-1) )
        #    else:
        #        return self.getComputeVal(maxCap, indexOfItemsToSelect-1)

