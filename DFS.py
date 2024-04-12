graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

visited = set() 

def dfs(visited, graph, node): 
    if node not in visited:
        print (node)
        visited.add(node)
        for i in graph[node]:
            dfs(visited, graph, i)

print("Depth-First Search of the Graph is")
dfs(visited, graph, '1')