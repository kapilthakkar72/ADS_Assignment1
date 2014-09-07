import helper
from constants import nodes, neighborSetLen, leafSetLen

'''A : Existing node
...X : New node'''
from helper import isNodeAlive
def add_node(A, X):
	# Nothing to be done if it's the first node
	if(A == None):
		nodes.append(X)
		return
	
	routePath, Z = route(A, X)
	
	if(Z.nodeKey == X.nodeKey):
		print "node already present"
		return -1
	
	updateRoutingTable(A, X, routePath)
	updateNeighborSet(A, X)
	updateLeafSet(Z, X)
	
	nodes.append(X)
	updateOthers(A, X, routePath)
	
def updateRoutingTable(A, X, routePath):
	i = 0
	X.routingTable.append(A.routingTable[i])	
	for B in routePath:
		X.routingTable.append(B.routingTable[++i])
	

def updateNeighborSet(A, X):
	X.neighborhoodSet = A.neighborhoodSet
	# adding neighbor of X as A
	if(len(X.neighborhoodSet) < neighborSetLen):
		X.neighborhoodSet.append(A)

def updateLeafSet(Z, X):
	X.leafSet = Z.leafSet
	
def updateOthers(A, X, Z, routePath):
	if(len(A.neighborhoodSet) < neighborSetLen):
		A.neighborhoodSet.append(X)
		
	if(len(Z.leafSet) < leafSetLen):
		'''TO-DO: do something'''
		
	'''TO-DO: check if below is required...take example'''
	'''for N in routePath:
		prefixLen = helper.shl(N.nodeKey, X.nodeKey)
		routeTableEntry = N.routingTable[prefixLen][int(X.nodeKey[prefixLen], 16)]
		if(not(isNodeAlive(routeTableEntry))):
			N.routingTable[prefixLen][int(X.nodeKey[prefixLen], 16)] = X
	'''
	
def route(A, X):
	routePath = []
	while(1): 
		'''TO-DO:'''  # need to change the while condition
		'''TO-DO:'''  # Search in leafSet
		prefixLen = helper.shl(A.nodeKey, X.nodeKey)
		routeTableEntry = A.routingTable[prefixLen][int(X.nodeKey[prefixLen], 16)] 
		if(isNodeAlive(routeTableEntry)):
			routePath.append(A)
			A = routeTableEntry
			continue  # forwarded to the closer node
		else:
			'''TO-DO: repair the routingTableEntry'''
			'''TO-DO: send to numerically closer node'''
		
		return routePath, A
	
