
def dfs(visited,graph,x) :
  if x not in visited :
    print(x,end=" ")
    visited.add(x)
    for i in graph[x] :
      dfs(visited,graph,i)

graph = {
    'a' : ['b','c','d'],
    'b' : ['e','f','a'],
    'c' : ['f','a'],
    'd' : ['a'],
    'e' : ['b'],
    'f' : ['b','c']
}
visited = set()
print("Following is the Dfs sequence : ")
dfs(visited,graph,'a')
'''Following is the Dfs sequence : 
a b e f c d 
'''

