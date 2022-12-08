
G = [[ 0, 1, 1, 0, 1, 0],
     [ 1, 0, 1, 1, 0, 1],
     [ 1, 1, 0, 1, 1, 0],
     [ 0, 1, 1, 0, 0, 1],
     [ 1, 0, 1, 0, 0, 1],
     [ 0, 1, 0, 1, 1, 0]]
node = "abcdef"
t={} 
degree =[] 
colorDict = {}
for i in range(len(G)):
  t[node[i]] = i
  degree.append(sum(G[i]))
  colorDict[node[i]]=["Blue","Red","Yellow","Green"]

sortedNode=[]
indeks = []
for i in range(len(degree)):
  max = 0
  for j in range(len(degree)):
    if j not in indeks:
      if degree[j] > max:
        max = degree[j]
        idx = j
  indeks.append(idx)
  sortedNode.append(node[idx])

theSolution={}
for n in sortedNode:
  setTheColor = colorDict[n]
  theSolution[n] = setTheColor[0]
  adjacentNode = G[t[n]]
  for j in range(len(adjacentNode)):
    if adjacentNode[j]==1 and (setTheColor[0] in colorDict[node[j]]):
      colorDict[node[j]].remove(setTheColor[0])

for i,j in sorted(theSolution.items()):
  print("Node",i," = ",j)

  '''Node a  =  Yellow
Node b  =  Blue
Node c  =  Red
Node d  =  Yellow
Node e  =  Blue
Node f  =  Red'''
