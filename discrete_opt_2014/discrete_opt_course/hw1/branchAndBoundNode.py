'''
Created on Apr 8, 2014

@author: domingolara
'''

from collections import namedtuple

class Decision(object):
    
    def __init__(self, item, decision):
        self.item = item
        self.decision = decision
        


class ProblemNode(object):
    '''
    classdocs
    '''


    def __init__(self, previouslyDecidedItems, pendingItemDecisions, parentNode):
        '''
        Constructor
        '''
        self.previouslyDecidedItems = previouslyDecidedItems
        self.parent = parentNode
        self.isFeasible = True
        self.pendingItemDecisions = pendingItemDecisions
        
        self.leftChildNode = None
        self.rightChildNode = None

    def labelAsInFeasible(self):
        self.isFeasible = False
        
    def isSolutionFeasible(self):
        return self.isFeasible
        
    def isLeafNode(self):
        if( len(self.pendingItemDecisions)==0):
            return True
        else:
            return False

    def getLeftChildNode(self):
        
        if( self.isLeafNode() ):
            self.leftChildNode = None
        else:
            
            childsPendingDecisions = list(self.pendingItemDecisions)
            
            takeIt = Decision(childsPendingDecisions.pop(),1)
            itemsInSackAfterTakingIt = list(self.previouslyDecidedItems)
            itemsInSackAfterTakingIt.append(takeIt)
            
            self.leftChildNode = ProblemNode(itemsInSackAfterTakingIt, childsPendingDecisions , self) 
            
        return self.leftChildNode

    def getRightChildNode(self):
        
        if( self.isLeafNode() ):
            self.rightChildNode = None
        else:
            childsPendingDecisions = list(self.pendingItemDecisions)

            dontTakeIt = Decision(childsPendingDecisions.pop(),0)
            itemsInSackAfterNoTTakingIt = list(self.previouslyDecidedItems)
            itemsInSackAfterNoTTakingIt.append(dontTakeIt)
            
            self.rightChildNode = ProblemNode(itemsInSackAfterNoTTakingIt, childsPendingDecisions , self)
        
        return self.rightChildNode 
    
    def showKnapSack(self):
        size = len(self.pendingItemDecisions) + len(self.previouslyDecidedItems)
        knapSack = []
        
        for i in range(0,size):
            knapSack.append(0)
            
        for d in self.previouslyDecidedItems:
            knapSack[d.item.index] = d.decision 

        outStr = ""
        for i in range(0,size):
            outStr += " "+ str(knapSack[i])
        
        return outStr.strip()
        
    def getOptimisticEstimate(self, capacity):
        
        curVal = self.getCurrentKnapSackValue()
        curWgt = self.getCurrentKnapSackWeight()
        sortedItemList = sorted(list(self.pendingItemDecisions), key= lambda x : ((x.value*1.0)/x.weight)*1.0, reverse=True)
        if(len(sortedItemList) == 0):
            return curVal
        
        while curWgt < capacity:
            
            if(len(sortedItemList) == 0 ):
                break
            
            nextItem = sortedItemList.pop(0)
            wgtIncrease = nextItem.weight
            if((curWgt + wgtIncrease) < capacity ):
                curVal += nextItem.value
                curWgt += wgtIncrease
            else:
                amtToTake = ((capacity - curWgt)*1.0)/(wgtIncrease*1.0)
                curVal += amtToTake*nextItem.value
                curWgt = capacity
        return curVal;
                

        
    def getCurrentKnapSackValue(self):
        val = 0
        for d in self.previouslyDecidedItems:
            val += d.decision*d.item.value
        return val 

    def getCurrentKnapSackWeight(self):
        wgt = 0
        for d in self.previouslyDecidedItems:
            wgt += d.decision*d.item.weight
        return wgt 
