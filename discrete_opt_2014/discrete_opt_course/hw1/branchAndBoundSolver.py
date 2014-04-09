'''
Created on Apr 8, 2014

@author: domingolara
'''

from collections import namedtuple
from operator import attrgetter

Item = namedtuple("Item", ['index', 'value', 'weight'])

def parse_data(input_data):
    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    
    return (capacity, items)


def solve_it_via_bb(input_data):
    (capacity, items) = parse_data(input_data)
    # prepare the solution in the specified output format

    value = 0
    weight = 0
    taken = [0]*len(items)
    
    import branchAndBoundNode
    root = branchAndBoundNode.ProblemNode([],items,None)
#     root.showKnapSack()
#     print "cur val: " + str(root.getCurrentKnapSackValue())
#     print "opt est.:"  + str(root.getOptimisticEstimate(capacity))
#     
#     print "left child"
#     leftChild = root.getLeftChildNode()
#     leftChild.showKnapSack()
#     print "cur val: " + str(leftChild.getCurrentKnapSackValue())
#     print "opt est.:"  + str(leftChild.getOptimisticEstimate(capacity))
#     
#     print "left child's children"
#     print "left left"
#     leftleft = leftChild.getLeftChildNode()
#     leftleft.showKnapSack()
#     print "cur val: " + str(leftleft.getCurrentKnapSackValue())
#     print "opt est.:"  + str(leftleft.getOptimisticEstimate(capacity))
# 
#     print leftChild.getLeftChildNode().getCurrentKnapSackValue()
#     print "left right"
#     leftChild.getRightChildNode().showKnapSack()
#     
#     
#     print "right child"
#     rightChild = root.getRightChildNode()
#     rightChild.showKnapSack()
#             
# 
#     print "root"
#     root.showKnapSack()
#     print root.getCurrentKnapSackValue()
#     print root.getOptimisticEstimate(10000)
    
    maxNodes=15000
    i=0
    
    maxiterations = 500000
    iter = 0
    
    nodesToVisit = []
    nodesToVisit.append(root)
    bestValueSoFar = 0;
    bestNodeSoFar = root
    
    print "Starting DFS Search"
    while len(nodesToVisit) != 0:
        curNode = nodesToVisit.pop()
        curNode.showKnapSack()
        
        if(i > maxNodes):
            break
        
        if(iter > maxiterations):
            break
        iter += 1
        
        if curNode.getCurrentKnapSackWeight() > capacity:
            curNode.labelAsInFeasible()
            
        if curNode.isLeafNode() == False:
            if curNode.isSolutionFeasible() == True:
                nodesOptimisticVal = curNode.getOptimisticEstimate(capacity)
                if nodesOptimisticVal >= bestValueSoFar :
                    nodesToVisit.append(curNode.getRightChildNode())
                    nodesToVisit.append(curNode.getLeftChildNode())
        else:
            curNodeValue = curNode.getCurrentKnapSackValue()
            if curNodeValue > bestValueSoFar:
                if curNode.isSolutionFeasible() == True:
                    bestValueSoFar = curNodeValue
                    bestNodeSoFar = curNode
                    i+=1
                    print bestValueSoFar
            #else:
               # print "bounded tree";

    print " iter count: " + str(iter)
    print "Good solns found: " + str(i)
    print('final answer: ') + str(bestValueSoFar)
    print('final knapsack: ') + str(bestNodeSoFar.showKnapSack())
    
    output_data = str(bestValueSoFar) + ' ' + str(0) + '\n'
 #   output_data += ' '.join(map(str, taken))
    output_data += bestNodeSoFar.showKnapSack()

    return output_data

def evaluatePossibleSolution(items, itemsTaken):
    value = 0
    for itemIndex in itemsTaken:
            value += items[itemIndex].value
    return value


import sys

if __name__ == '__main__':
#        file_location = './data/ks_30_0'
        file_location = './data/myProb'
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print "Default"
        print solve_it_via_bb(input_data)
        print "End"
        
