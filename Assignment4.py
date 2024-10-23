# SOURCE: MIT OCW ALGORITHMS LECTURE 9 and 10 -> use of dfs and queues to traverse non weighted graphs
class City:
    def __init__(self,name,pop):
        self.name = name
        self.population = pop 
        self.connection = []
    
    def edge(self, city2):
        self.connection.append(city2)

# create a hashmap for the graph traversal
newMap = {}
f = open("city_population.txt","r")
for line in f:
    name, pop = line.strip().split(" : ")
    newMap[name] = City(name,int(pop))
f.close()

f = open("road_network.txt","r")
for line in f:
    name1, name2 = line.strip().split(" : ")
    name1 = newMap[name1]
    name2 = newMap[name2]
    name1.edge(name2)
    name2.edge(name1)
f.close()

# for city_name, city in newMap.items():
#     print(city.name,city.population, city.connection)

def numIsland(newMap):
    visited = set()
    numIslands = 0

    def dfs(city):
        visited.add(city)
        for edge in city.connection:
            if edge not in visited:
                dfs(edge)
    
    for city in newMap.values():
        if city not in visited:
            dfs(city)
            numIslands += 1

    return numIslands

def islandPeople(newMap):
    visited = set()
    numPeople = []

    def dfs(city):
        visited.add(city)
        pop = city.population
        for edge in city.connection:
            if edge not in visited:
                pop += dfs(edge)
        return pop
    
    for city in newMap.values():
        if city not in visited:
            pop = dfs(city)
            numPeople.append(pop)

    return numPeople

def minDistance(cities,A,B):
    if A == B:
        return 0
    visited = set()
    queue = [(A,0)]

    while queue:
        curr = queue.pop(0)
        distance = curr
        if curr == B:
            return distance
        visited.add(curr)
        for adjacent in curr.connection:
            if adjacent not in visited:
                queue.append(adjacent, distance + 1)
    return -1

# print(numIsland(newMap))
# print(islandPeople(newMap))
print(minDistance(newMap, "Pacifica", "York"))