# SOURCE: MIT OCW ALGORITHMS LECTURE 9 and 10 -> use of dfs and queues to traverse non weighted graphs

# TASK 1
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

def minDistance(cities,city1,city2):
    A = cities.get(city1)
    B = cities.get(city2)
    if not A or not B:
        raise ValueError("One of those cities does not exist")
    if A == B:
        return 0
    visited = set()
    queue = [(A,0)]

    while queue:
        curr, distance = queue.pop(0)
        # print(f"Visiting {curr.name}, distance: {distance}")
        if curr == B:
            return distance
        visited.add(curr)
        for adjacent in curr.connection:
            if adjacent not in visited:
                queue.append((adjacent, distance + 1))
    return -1

print("Testing Task 1")
newCity1 = City("Irvine", 307760)
newCity2 = City("Pasadena", 138699)
newCity3 = City("Vancouver", 662248)
print(f"Initializing city object {newCity1.name} with population: {newCity1.population}")
print(f"Initializing city object {newCity2.name} with population: {newCity2.population}")
print(f"Initializing city object {newCity3.name} with population: {newCity3.population}\n")

print("Testing Task 3")
print(f"The number of islands inside the hashmap is: {numIsland(newMap)}\n")

print("Testing Task 4")
print(f"The population on each island is {islandPeople(newMap)}\n")

print("Testing Task 5")
result1 = minDistance(newMap, "Pacifica", "York")
print(f"The minimum distance to reach Pacifica and York is: {result1}\n")

print("Custom testcases")
print("Attempting to make a test where there is at least more than one island so I know the answer is right")

testMap = {}
testPopulation = [
    "New York : 8405837",
    "Los Angeles : 3884307",
    "Chicago : 2718782",
    "Houston : 2195914",
    "Philadelphia : 1553165",
    "Phoenix : 1513367",
    "Arcadia : 1231233"
]

testRoad = [
    "New York : Los Angeles",
    "Chicago : Houston",
    "Philadelphia : Phoenix",
    "Houston : Arcadia"
]

for line in testPopulation:
    name, pop = line.strip().split(" : ")
    testMap[name] = City(name, int(pop))

# Create road connections
for line in testRoad:
    name1, name2 = line.strip().split(" : ")
    city1 = testMap[name1]
    city2 = testMap[name2]
    city1.edge(city2)
    city2.edge(city1)

print("Number of islands:", numIsland(testMap))
print("Population of each island:", islandPeople(testMap)) 

print("Minimum distance from New York to Los Angeles:", minDistance(testMap, "New York", "Houston"))
print("Minimum distance from New York to Chicago:", minDistance(testMap, "New York", "Chicago"))
print("Minimum distance from Chicago to Arcadia:", minDistance(testMap, "Chicago", "Arcadia"))